expression = str(input("Enter a mathematical expression: "))

openParenthesis = []
closedParenthesis = []
for pos, i in enumerate(expression):
    if(i == "("):
        openParenthesis.append(pos)
        for j in range(pos, len(expression)):
            if(expression[j] == ")" and j not in closedParenthesis):
                closedParenthesis.append(j)
if(len(openParenthesis) == len(closedParenthesis)):
    print("This expression is written correctly!")
else:
    print("This expression isn't written correctly!")
