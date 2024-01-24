# -*- coding: utf-8 -*-
"""Converting_infix_postfix _and _Evaluation_of_Postfix_expression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZXwhyJnoUy28fUSbwyjIGs0AyaMPXXNU
"""

def precedence(a):
    if a=="+" or a=="-":
        return 1
    if a=="*" or a=="/":
        return 2

a = list(input("Enter the infix notation separated by space: ").split(" "))
postfix = ""
opstack = []
for i in a:
    if i in ["+", "-", "*", "/"]:
        if((len(opstack)==0) or (precedence(i)>precedence(opstack[-1]))):
            opstack.append(i)
        else:
            postfix+=opstack.pop()
            opstack.append(i)
    elif i==" ":
        continue
    else:
        postfix+=i
while(len(opstack)!=0):
    postfix+=opstack.pop()
print(postfix)

a = list(input("Enter the postfix expression: ").split(" "))
stack = []
for i in a:

    if(i in ["+", "-", "*", "/"]):
        b = stack.pop()
        c = stack.pop()
        if(i=="+"):
            stack.append(c+b)
        elif(i=="-"):
            stack.append(c-b)
        elif(i=="*"):
            stack.append(c*b)
        elif(i=="/"):
            stack.append(c/b)
    elif i==" ":
        continue
    else:
        stack.append(int(i))
print("The result of the expression: ",stack[0])