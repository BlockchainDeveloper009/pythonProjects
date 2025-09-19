use anchor_lang::prelude::*;

// This is the entry point for your Solana program.
declare_id!("Fg6PaFpoGXkYsidMpWTK6W2ZwyqDth2WssEw9rXoHbrb");

// This macro defines the main program module.
#[program]
pub mod agreement_program {
    use super::*;

    // An instruction to initialize a new agreement account on the blockchain.
    // It now accepts a fixed-size array of witness public keys.
    pub fn create_agreement(
        ctx: Context<CreateAgreement>,
        party_a: Pubkey,
        party_b: Pubkey,
        witnesses: [Pubkey; 2],
    ) -> Result<()> {
        let agreement = &mut ctx.accounts.agreement;
        
        // Store the public keys of the two main parties.
        agreement.party_a = party_a;
        agreement.party_b = party_b;
        
        // Store the public keys of the two witnesses.
        agreement.witnesses = witnesses;
        
        // Initialize the signature status for all parties and witnesses to false.
        agreement.signed_a = false;
        agreement.signed_b = false;
        agreement.signed_witnesses = [false; 2];
        
        // The program ID is automatically derived by Anchor.
        msg!("Agreement account created for parties {} and {}", party_a, party_b);
        msg!("Witnesses for this agreement are: {:?} and {:?}", witnesses[0], witnesses[1]);
        Ok(())
    }

    // An instruction that allows a main party to sign the agreement.
    pub fn sign_agreement(ctx: Context<SignAgreement>) -> Result<()> {
        let agreement = &mut ctx.accounts.agreement;
        let signer = &ctx.accounts.signer;

        // **New Logic:** First, check if both witnesses have signed.
        require!(agreement.signed_witnesses[0] && agreement.signed_witnesses[1], AgreementError::WitnessesNotSigned);

        // Check if the current signer is Party A.
        if signer.key() == agreement.party_a {
            require!(!agreement.signed_a, AgreementError::AlreadySigned);
            agreement.signed_a = true;
            msg!("Party A has signed the agreement.");
        } 
        // Or check if the current signer is Party B.
        else if signer.key() == agreement.party_b {
            require!(!agreement.signed_b, AgreementError::AlreadySigned);
            agreement.signed_b = true;
            msg!("Party B has signed the agreement.");
        } 
        // If the signer is neither party, return an error.
        else {
            return err!(AgreementError::InvalidSigner);
        }

        Ok(())
    }
    
    // **New Instruction:** Allows a witness to sign the agreement.
    pub fn witness_sign(ctx: Context<SignAgreement>) -> Result<()> {
        let agreement = &mut ctx.accounts.agreement;
        let signer = &ctx.accounts.signer;

        // Check if the signer is a valid witness and update their status.
        if signer.key() == agreement.witnesses[0] {
            require!(!agreement.signed_witnesses[0], AgreementError::AlreadySigned);
            agreement.signed_witnesses[0] = true;
            msg!("Witness 1 has signed the agreement.");
        } else if signer.key() == agreement.witnesses[1] {
            require!(!agreement.signed_witnesses[1], AgreementError::AlreadySigned);
            agreement.signed_witnesses[1] = true;
            msg!("Witness 2 has signed the agreement.");
        } else {
            return err!(AgreementError::InvalidWitness);
        }

        Ok(())
    }
}

// Defines the accounts required for the 'CreateAgreement' instruction.
#[derive(Accounts)]
#[instruction(party_a: Pubkey, party_b: Pubkey, witnesses: [Pubkey; 2])]
pub struct CreateAgreement<'info> {
    // This is the account that will store the agreement data.
    // 'init' creates the account, 'payer' specifies who pays for it,
    // 'space' defines the size, and 'seeds' are used to derive a unique address.
    #[account(
        init, 
        payer = signer, 
        space = 8 + Agreement::LEN, 
        seeds = [b"agreement", signer.key().as_ref(), party_a.key().as_ref(), party_b.key().as_ref()],
        bump
    )]
    pub agreement: Account<'info, Agreement>,
    
    // The signer is the account that initiates the transaction (e.g., Party A).
    #[account(mut)]
    pub signer: Signer<'info>,
    
    // The Solana system program is required for creating new accounts.
    pub system_program: Program<'info, System>,
}

// Defines the accounts required for the 'SignAgreement' instruction.
#[derive(Accounts)]
pub struct SignAgreement<'info> {
    // The agreement account to be signed. 'mut' indicates it will be modified.
    #[account(mut, seeds = [b"agreement", agreement.party_a.as_ref(), agreement.party_b.as_ref()], bump)]
    pub agreement: Account<'info, Agreement>,
    
    // The party who is signing the agreement.
    pub signer: Signer<'info>,
}


// This is the data structure for our agreement. It's stored on the blockchain.
#[account]
pub struct Agreement {
    pub party_a: Pubkey,
    pub party_b: Pubkey,
    pub signed_a: bool,
    pub signed_b: bool,
    pub witnesses: [Pubkey; 2],
    pub signed_witnesses: [bool; 2],
}

// Defines the total size of the Agreement account.
// 8 is for the Anchor account discriminator.
impl Agreement {
    // Pubkey (32) * 4 + Bool (1) * 4 = 132
    // Let's refine the calculation for the new fields.
    // party_a: 32, party_b: 32
    // signed_a: 1, signed_b: 1
    // witnesses: [Pubkey; 2] -> 32 * 2 = 64
    // signed_witnesses: [bool; 2] -> 1 * 2 = 2
    // total = 32 + 32 + 1 + 1 + 64 + 2 = 132
    const LEN: usize = 32 + 32 + 1 + 1 + (32 * 2) + (1 * 2);
}

// Custom error messages for the program.
#[error_code]
pub enum AgreementError {
    #[msg("This party has already signed the agreement.")]
    AlreadySigned,
    #[msg("The signer is not a valid party to this agreement.")]
    InvalidSigner,
    // New error for witness-specific checks.
    #[msg("The signer is not a valid witness for this agreement.")]
    InvalidWitness,
    // New error to enforce signing order.
    #[msg("The main parties cannot sign until all witnesses have signed.")]
    WitnessesNotSigned,
}
