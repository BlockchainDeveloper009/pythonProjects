class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If number of rows is 1 or string length is shorter than or equal to the number of rows,
        # the zigzag conversion doesn't change the string, so return the string as is.
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list with one empty string for each row. This will hold the characters for each row.
        rows = [''] * numRows

        # 'step' controls whether we move "down" or "up" through the rows.
        # We start with -1 so that the first step changes it to 1 (down).
        step = -1

        # Current row we are placing characters into, starting at the top (0).
        curr_row = 0

        # Loop through each character in the input string
        for char in s:
            # Add the current character to the current row
            rows[curr_row] += char

            # If we are at the top or bottom row, change the direction (reverse step)
            if curr_row == 0 or curr_row == numRows - 1:
                step = -step

            # Move to the next row in the current direction (down if step=1, up if step=-1)
            curr_row += step

        # Join all rows into one string and return it as the final zigzag converted string
        return ''.join(rows)

        # Example usage:

sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s, numRows))  # Output: "PAHNAPLSIIGYIR"

