from stacks import Stack
operators = {'+':1, '-':1, '*':2, '/':2}

def InToPos(Infix):
    opstack = Stack(len(Infix))
    result = ""
    for c in Infix:
        if c.isdigit():
            result += c
        elif c in operators:
            if opstack.stptr != -1 and opstack.stack[opstack.stptr] in operators:
                if operators[opstack.stack[opstack.stptr]] >= operators[c]:
                    result += opstack.pop()
            opstack.push(c)
        elif c == '(':
            opstack.push(c)
        elif c == ')':
            while opstack.stack[opstack.stptr] != '(':
                result += opstack.pop()
            opstack.pop()
    while opstack.stptr != -1:
        result += opstack.pop()
    return result

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
    postfix.append(InToPos("5+((1+2)*4)-3"))
    calpostfix(postfix[2])

def main():
    test()

if __name__ == "__main__":
    main()