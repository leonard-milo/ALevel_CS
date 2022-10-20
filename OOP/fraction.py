import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, otherOb):
        lcm = math.lcm(self.denominator, otherOb.denominator)
        numerator = int(self.numerator*(lcm/self.denominator) + otherOb.numerator*(lcm/otherOb.denominator))
        denominator = lcm
        return Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __sub__(self, otherOb):
        lcm = math.lcm(self.denominator, otherOb.denominator)
        numerator = int(self.numerator*(lcm/self.denominator) - otherOb.numerator*(lcm/otherOb.denominator))
        denominator = lcm
        return Fraction(numerator, denominator)

    def __mul__(self, otherOb):
        numerator = self.numerator * otherOb.numerator
        denominator = self.denominator * otherOb.denominator
        gcd = math.gcd(numerator, denominator)
        return Fraction(int(numerator/gcd), int(denominator/gcd))

    def __truediv__(self, otherOb):
        numerator = self.numerator * otherOb.denominator
        denominator = self.denominator * otherOb.numerator
        gcd = math.gcd(numerator, denominator)
        return Fraction(int(numerator/gcd), int(denominator/gcd))

    def __eq__(self, otherOb):
        ob1 = self.numerator/self.denominator
        ob2 = otherOb.numerator/otherOb.denominator
        if ob1 == ob2:
            return "=="
        elif ob1 > ob2:
            return ">"
        else:
            return "<"

    def __gt__(self, otherOb):
        ob1 = self.numerator/self.denominator
        ob2 = otherOb.numerator/otherOb.denominator
        if ob1 > ob2:
            return ">"
        else:
            return "<="

    def __lt__(self, otherOb):
        ob1 = self.numerator/self.denominator
        ob2 = otherOb.numerator/otherOb.denominator
        if ob1 < ob2:
            return "<"
        else:
            return ">="

def test():
    fracOb1 = Fraction(1,3)
    fracOb2 = Fraction(1,3)
    method = '=='
    match method:
        case '+':
            fracOb3 = fracOb1 + fracOb2
            print(f"{fracOb1} + {fracOb2} = {fracOb3}")
        case '-':
            fracOb3 = fracOb1 - fracOb2
            print(f"{fracOb1} - {fracOb2} = {fracOb3}")
        case '*':
            fracOb3 = fracOb1 * fracOb2
            print(f"{fracOb1} * {fracOb2} = {fracOb3}")
        case '/':
            fracOb3 = fracOb1 / fracOb2
            print(f"{fracOb1} / {fracOb2} = {fracOb3}")
        case '==':
            fracOb3 = fracOb1 == fracOb2
            print(f"{fracOb1} {fracOb3} {fracOb2}")
        case '>':
            fracOb3 = fracOb1 > fracOb2
            print(f"{fracOb1} {fracOb3} {fracOb2}")
        case '<':
            fracOb3 = fracOb1 < fracOb2
            print(f"{fracOb1} {fracOb3} {fracOb2}")
        
def main():
    test()

if __name__ == "__main__":
    main()