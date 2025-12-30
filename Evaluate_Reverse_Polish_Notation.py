def evalRPN(tokens):
    stack = []          
    for char in tokens:
        match char:
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b - a)
            case "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b / a))
            case "*":
                stack.append(stack.pop() * stack.pop())
            case _:
                stack.append(int(char))

    return stack.pop()
# testcase
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))