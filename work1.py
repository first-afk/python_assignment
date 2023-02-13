
# assignment: ask a user for a first and second number input and then an operator input. let the function return an arithemetic based on thr operator entered

def main(): 
    x,y,Operator = '','',''
    while x <= '' and y <= '' and Operator != '-' and Operator != '+' and Operator != '/':
        x = input('Enter a value: ')
        y = input('Enter a value: ')
        Operator = input('input operand: ')
    x, y = int(x), int(y)
    if Operator == '+':
       added(x, y)
    elif Operator == '-':
     sub(x, y)
    elif Operator == '/':
        print('operator not recognized')
    


def added(x, y,):
   print(f"the sum of {x} + {y} = {x + y}")
def sub(x,y,):
    print(f"the sub of {x} - {y} = {x - y}")
   
    
main()
