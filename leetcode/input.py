

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

print('Enter your Real Number')
realNumber = input()
print('Enter your Imaginary Number')
imaginaryNumber = input()


x = Complex(realNumber, imaginaryNumber)

print(x.r)
print(x.i)


