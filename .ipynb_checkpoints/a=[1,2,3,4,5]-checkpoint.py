def calculator():
    i=input('enter your expression:')
    return eval(i)

while True:

    print("MENU,\n1:Calculate,\n2:Exit\n")

    c=int(input("ENTER THE OPTIONS FOR OPERATION:\n"))

    if c==1:
        print('RESULT:',calculator())
        
    elif c==2:
        break