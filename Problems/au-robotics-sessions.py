class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def add(self,other):
        sum = Complex(0,0)
        sum.real = self.real + other.real
        sum.imag = self.imag + other.imag
        return sum
    def subtract(self,other):
        diff = Complex(0,0)
        diff.real = self.real - other.real
        diff.imag = self.imag - other.imag
        return diff
    def magnitude(self):
        mag = Complex(0,0)
        mag =(self.real**2 + self.imag**2)**0.5
        return mag

c1 = Complex(4,5)
c2 = Complex(5,6)
c4=c1.subtract(c2)
print(c4.real,end="")
if c4.imag > 0:
    print(f"+{c4.imag}i")
else:
    print(f"{c4.imag}i")



