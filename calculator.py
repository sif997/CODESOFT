print('----------------------------------------------------------------------')
print('                              Calculator                              ')
print('----------------------------------------------------------------------')
print('1. Addition')
print('2. subraction')
print('3. Divition')
print('4. Multiplication')
op=int(input('Choose the operation 1 or 2 or 3 or 4 : '))
n1=int(input('Enter 1st no : '))
n2=int(input('Enter 2nd no : '))

if(op==1):
    add=n1+n2
    print('Addition = ',add)
    
elif(op==2):
    sub=n1-n2
    print('Subraction = ',sub)

elif(op==3):
    div=n1/n2
    print('Divition = ',div)

else:
    mul=n1*n2
    print('Multiplication = ',mul)
    



