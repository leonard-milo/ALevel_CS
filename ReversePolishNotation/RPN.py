from stacks import Stack
operators = ['+', '-', '*', '/']

def calpostfix(eq):
    stack = Stack(10)
    for c in eq:
        if c.isdigit():
            stack.push(c)
        elif c in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            code = op1 + c + op2
            result = str(eval(code))
            stack.push(result)
        print(stack.stack)

def test():
    postfix = ["34*9-", "512+4*3-+"]
    calpostfix(postfix[1])

def main():
    test()

if __name__ == "__main__":
    main()