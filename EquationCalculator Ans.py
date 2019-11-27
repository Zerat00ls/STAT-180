# EquationCalculator.py - Assignment 2
#
# This program is an equation calculator. This calculator asks the user for a complete equation
# for example, 2.3 + 5.92. Once the program has read the equation the user entered as a string,
# it "manipulates" the string in order to figure out the operands and the operator of the equation,
# then, it executes the equation and displays its result, for example, 2.3 + 5.92 = 8.22.
# 
# Anne Lavergne
# Modified in February 2017

opList = ["+", "-", "*", "/"]

# Welcome and instruct the user
print("Welcome to my Equation Calculator!\n")
print("""My EquationCalculator can 
    \tadd: +,
    \tsubtract: -,
    \tmultiply: *, and 
    \tdivide: / (result is a float).""")
print("""\nThe equation you enter must follow this syntax:
 <operand><space><operator><space><operand>.""")
print("An <operand> is any float you wish.")
print("An <operator> is any of the above 4 operators this Calculator can deal with.")
print("A <space> is an empty space. :)")

# Read user's equation as a string
equation = input("\nPlease, enter your equation: ")

# Echo to the screen what the user has entered
print("The equation you entered is '%s'." %equation)

# If the user has entered a sequence of letters
if equation.isalpha( ) :
    print("\nYou have entered the sequence of letters '%s' which is not an equation. Please, try again." %equation)
else :  
    # Parse the equation into a list
    theParts = equation.split() # default is whitespace
   # print("Here is a list containing the operands and operator of the equation: ", theParts) # For debug purposes

    if len(theParts) == 0 :
        print("\nHave you simply pressed the Enter key? Please, enter an equation next time! :)")
    elif len(theParts) == 1 :
        print("\nYou have entered the equation '%s' which is not a complete equation" %equation )
        if theParts[0] in opList :
            print("since it only contains the operator %s . Please, try again." %theParts[0])
        else :
            print("since it only contains the operand %s . Please, try again." %theParts[0])    
    elif len(theParts) == 2 :
        print("\nYou have entered the equation '%s' which is not a complete equation" %equation )
        if theParts[1] in "+-*/" :
            print("since it only contains the operand %s and the operator %s. Please, try again."
                  %(theParts[0],theParts[1]))
        else :
            print("since it only contains the operand %s and the operand %s. Please, try again."
                  %(theParts[0],theParts[1])) 

    elif len(theParts) == 3 :  # Valid equation, compute it and prints its result.
        
        # For debug purposes - We can index a list just like a string using [index] 
        # print("\nThe equation entered by the user is %s %s %s." %(theParts[0], theParts[1], theParts[2]))

        # Detecting division by 0.0 (or 0)
        if theParts[1] == '/' and float(theParts[2]) == 0.0 :
                print("The equation has %s as denominator. The equation cannot be evaluated. Please, try again." %theParts[2])                                   
        else :
            if theParts[1] == '+' :
                result = float(theParts[0]) + float(theParts[2])
            elif theParts[1] == '-' :
                result = float(theParts[0]) - float(theParts[2])
            elif theParts[1] == '*' :
                result = float(theParts[0]) * float(theParts[2])
            else : # theParts[1] == '/'
                result = float(theParts[0]) / float(theParts[2])             

            print("The equation is %g %s %g = %g" %(float(theParts[0]), theParts[1], float(theParts[2]), result))
            
print("\n----!")
