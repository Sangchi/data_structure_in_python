'''
2. Evaluate Reverse Polish Notation
Problem: Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN). Valid operators are +, -, *, and /.

Example:

Input: ["2", "1", "+", "3", "*"]
Output: 9 (because (2 + 1) * 3 = 9)

'''
def reverse_polish_notation(tokens):

    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in operators:

            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


array_list = ["2", "1", "+", "3", "*"]
print(reverse_polish_notation(array_list))
