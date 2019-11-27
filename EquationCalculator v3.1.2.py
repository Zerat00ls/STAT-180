#EquationCalculator.py
#Version. 3.1.2
#020317
#Siyul Byun


#Welcome message
print("""Welcome to my Equation Calculator!
      """)

#Instruction
print("""My EquationCalculator can 
    	add: +,
    	subtract: -,
    	multiply: *, and 
    	divide: / (result is a float).
    	
The equation you enter must follow this syntax:
 <operand><space><operator><space><operand>.
An <operand> is any float you wish.
An <operator> is any of the above 4 operators this Calculator can deal with.
A <space> is an empty space. :)
""")

#Ask the equation to the user.
equation = input("Please, enter your equation: ")

#Double check the equation
print("""The equation you etered is'%s'.
""" %equation)

#Check the equation is valid
#In case, user simply pressed the Enter key
if equation is '':
    print("""Have you simply pressed the Enter key? Please, enter an equation next time! :)
""")
else :
    #Slice the user input.
    eQuation = equation.split()
    #Make sure the equation is valid: <operand> <operator> <operand> (length = 3)
    if len(eQuation) != 3:
        #the equation is not valid. check what's problem with the equation.
        #Does the equation contains the letter?
        if eQuation[0].isalpha():
            print("""You have entered the sequence of letters '%s' which is not an equation. Please, try again.
""" %equation)
        #Does the equation only contains the operator?
        elif len(eQuation) == 1 and (eQuation[0] is '+' or eQuation[0] is '-' or eQuation[0] is '*' or equation[0] is '/'):
            print("""You have entered the equation '%s' which is not a complete equation
since it only contains the operator %s. Please, try again.
""" %(equation, equation))
        #Does the equation contains second operand?
        elif len(eQuation) == 2 and (eQuation[1] is '+' or eQuation[1] is '-' or eQuation[1] is '*' or equation[1] is '/'):
            print("""You have entered the equation '%s' which is not a complete equation
since it only contains the operand %s and the operator %s. Please, try again.
""" %(equation, eQuation[0], eQuation[1]))
        #Does the equation only contains the operand?
        elif len(eQuation) == 1 and float(eQuation[0]):
            print("""You have entered the equation '%s' which is not a complete equation
since it only contains the operand %s . Please, try again.
""" %(equation, equation))
        #Does the equation contains operator?
        elif len(eQuation) == 2 and float(eQuation[0]) and float(eQuation[1]):
            print("""You have entered the equation '%s' which is not a complete equation
since it only contains the operand %s and the operand %s. Please, try again.
""" %(equation, eQuation[0], eQuation[1]))
    else :
        #Set the variable
        number1 = eQuation[0]
        operator = eQuation[1]
        number2 = eQuation[2]

        #Let's solving the equation.
        if operator is '+':
            ans = float(number1) + float(number2)
            print("""The equation is %s = %g.
""" %(equation, ans))
        elif operator is '-':
              ans = float(number1) - float(number2)
              print("""The equation is %s = %g.
""" %(equation, ans))
        elif operator is '*':
              ans = float(number1) * float(number2)
              print("""The equation is %s = %g.
""" %(equation, ans))
        elif operator is '/':
            if number2 is '0':
                print("""The equation has 0 as denominator. The equation cannot be evaluated. Please, try again.
""")
            else :
                ans = float(number1) / float(number2)
                print("""The equation is %s = %g.
""" %(equation, ans))

print("---!")
