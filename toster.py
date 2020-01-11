a = int(input())
mode = input()
b = int(input())
if mode == '+':
    print(a+b)
elif mode == '-':
    print(a-b)
elif mode == '*':
    print(a*b)
elif mode == '/':
    print(a/b)
elif mode == '//':
    print(a//b)
elif mode == '%':
    print(a%b)
else:
    print('Check, that you wrote only numbers at first and second str, and that you wrote only sign at second str')
