#equationCalculator.py
#Version. 1.0.0
#020217
#Siyul Byun

#Welcome message
print("Welcome to my Equation Calculator!")

#Instroction
print("""My EquationCalculator can 
    	add: +,
    	subtract: -,
    	multiply: *, and 
    	divide: / (result is a float).
    	
The equation you enter must follow this syntax:
 <operand><space><operator><space><operand>.
An <operand> is any float you wish.
An <operator> is any of the above 4 operators this Calculator can deal with.
A <space> is an empty space. :)""")

#Ask the equation to the user.
equation = input("Please, enter your equation: ")

#Double check the equation
print("The equation you etered is'%s'." %equation)

#Slice the user input.
eQuation = equation.split()

#Set the variouble
number1 = eQuation[0]
operator = eQuation[1]
number2 = eQuation[2]

#Let's solving the equation.
if number 1 != float
    print("You have entered the sequence of letters '%g' which is not an equation. Please, try again." %equation)
