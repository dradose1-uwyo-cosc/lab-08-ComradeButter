# Rylan Galloway
# UWYO COSC 1010
# Submission Date 11/4/2024
# Lab 8
# Lab Section: 14
# Sources, people worked with, help given to: Danny Keuning 
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
##use this function in the third part and wait until the user types exit to print values

def Int_Or_Not(string):
    try:
        string = float(string)
        string = int(string)
        return True
    except ValueError:
        pass
    return False
print(Int_Or_Not("45"))
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def point_Slope_Equation(m, b, xlower, xhigher):
    m_actual = Int_Or_Not(m)
    b_actual = Int_Or_Not(b)
    xl_actual = Int_Or_Not(xlower)
    xh_actual = Int_Or_Not(xhigher)
    if (m_actual and b_actual and xl_actual and xh_actual):
        x=[]
        y=[]
        for number in range(xl_actual,xh_actual):
            x.append(number)
    
            n = ((m_actual*number) + (b_actual))
            y.append(n)
        return y
print(point_Slope_Equation(2,4,6,9))
print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadratic_equation (a,b,c):
    discriminate = b**2 - 4*a*c
    if discriminate <0:
        return 'Null Value'
    else:
        x1 = round((-b +((b**2 -4*a*c)**(1/2))/(2*a)))
        x2 = round((-b -((b**2 -4*a*c)**(1/2))/(2*a)))
        return x1, x2
while(True):
    a= int(input('Value A: '))
    b= int(input('Value B: '))
    c= int(input('Value C: '))
    break
answers = quadratic_equation(a,b,c)
print(f'Solutions: {answers}')