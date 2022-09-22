class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None for _ in range(self.size)]
        self.stptr = -1

    def push(self, value):
        if self.stptr < self.size - 1:
            self.stptr += 1
            self.stack[self.stptr] = value
        else:
            print("Stack Overflow")

    def pop(self):
        if self.stptr >= 0:
            value = self.stack[self.stptr]
            self.stack[self.stptr] = None
            self.stptr -= 1
            return value
        else:
            print("Stack Underflow")

def test():
    stack = Stack(10)
    for n in range(11):
        stack.push(n)
    print(stack.pop())
    for _ in range(10):
        stack.pop()
    print(stack.stack)

def main():
    test()

if __name__ == "__main__":
    main()