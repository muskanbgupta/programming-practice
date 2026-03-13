
def linear_equation():
    
    print("**Solves linear equation simultaneously**")
    user=input("you will enter equation with variable? yes/no:")
    #takes user input with varibles
    if (user.lower()=="yes"): #convert user input to lower
        x1=input("enter x1 :")
        if(x1=="x"):
            x1="1x" #convert single varible to 1
        a1= int(x1[:-1]) #convert to int minus the last value cause it string
        for i in range(1,4):
            o1=input("enter operator:")  #if user enter everything expect operator
            if (o1 == '-' or o1 =='+'):
             break
            else:
                print("Enter operator please!(+/-)")
        y1=input("enter y1 :")
        if(y1=="y"):
            y1="1y" #convert single varible to 1
        b1=int(y1[:-1]) #convert to int minus the last value cause it string
        if(o1=="-"):
            b1=-b1  #if the operator is minus than value of second coffi will be negative
        c1=int(input("enter 1st constant :"))
        print(f'First equation:{x1}{o1}{y1}={c1}')
        
        x2=input("enter x2 :")
        if(x2=="x"):
            x2="1x" #convert single varible to 1
        a2=int(x2[:-1]) #convert to int minus the last value cause it string
        for i in range(1,4):
           o2=input("enter operator:") 
           if (o2 == '-' or o2 =='+'):
             break
           else:
                print("Enter operator please!(+/-)")
        y2=input("enter y2 :")
        if(y2=="y"):
            y2="1y" #convert single varible to 1
        b2=int(y2[:-1]) #convert to int minus the last value cause it string
        if(o2=="-"): #if the operator is minus than value of second coffi will be negative
         b2=-b2
        
        c2=int(input("enter 2nd constant  :"))
        print(f'Second equation:{x2}{o2}{y2}={c2}')
        
        #without varibles 
        #directly converted to int
    else:
        a1=int(input("enter x1 :"))
        for i in range(1,4):
            o1=input("enter operator:") #if user enter everything expect operator
            if (o1 == '-' or o1 =='+'):
             break
            else:
                print("Enter operator please!(+/-)")
        b1=int(input("enter y1 :"))
        if(o1=="-"):
            b1=-b1 
        c1=int(input("enter 1st constant :"))
        print(f'First equation:{a1}x{o1}{b1}y={c1}') #added varibles 
        a2=int(input("enter x2 :"))
        for i in range(1,4):
            o2=input("enter operator:")#if user enter everything expect operator
            if (o2 == '-' or o2 =='+'):
             break
            else:
                print("Enter operator please!(+/-)")
        b2=int(input("enter y2 :"))
        if(o2=="-"):
            b2=-b2 
        c2=int(input("enter 2nd constant  :"))
        print(f'Second equation:{a2}x{o2}{b2}y={c2}')#added varibles 
    denominator=(a1*b2 - a2*b1) #if denominator is zero the equation can't be find
    if(denominator==0):
        print(f"Error in Equation")
        return
    #formula to find value of x and y
    x=(c1*b2- c2*b1)/denominator
    y=(a1*c2- a2*c1)/denominator
    print(f"SOLUTION:\nx={x}\ny={y}")

linear_equation()