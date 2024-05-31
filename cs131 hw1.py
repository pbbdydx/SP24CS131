################################################################################
# 1.) Hello, Me!
# 
# Implement the following:
#   - A variable named 'first' and assign it a literal string containing your first name.
#   - A variable named 'last' and assign it a literal string containing your last name.
#   - Using these two variables print out "Hello first last".

# TODO: 
first = "Prajwal"
last = "Bhandari"
print( "Hello", first, last)

################################################################################
# 2.) Operator Practice
# 
# Print out the result of each of the following equations:
#   p2_1: 'a' plus 'b' raised to the second power.
#   p2_2: 'b' plus 'c' all modulo by 'x'.
#   p2_3: The sum of 'a', 'b', and 'c' subtracted from 'x' divided by 'y'.
#   p2_4: The remainder (integer division) of x by y.
#   p2_5: The product of all the variables divided by the remainder of ('a' to the 'b' power) by 7.
# 

# Use these variables to control your algorithms.
a = 1
b = 2
c = 3
x = 4
y = 5
z = 7

# TODO:
p2_1 = a + b**2 
p2_2 = (b + c)% x
p2_3 = x / y - (a + b +c)
p2_4 = x % y
p2_5 = (a *b * c * x * y * z) / (a**b % z)

print( p2_1, p2_2, p2_3, p2_4, p2_5, sep=", ")


################################################################################
# 3.) Bottle Factory
# 
# Implement the algorithm from Problem 3 of the Design Document.
#   For your inputs and outputs, create the following variables:
#       - `b` should be called 'bottlesPerHour'
#       - `r` should be called 'lbOfMaterial'
#       - `t` should be called 'numOfMinutes'
#       - The required ounces of material should be called 'ozOfMaterial'
#       - The produced number of bottles should be called 'numBottles'
#
# After you've implemented the algorithm, make sure that all three tests produce
# the expected outputs.
# 

# TODO: 
bottlesPerHour = 100        
lbOfMaterial = 500
numOfMinutes = 12

ozOfMaterial = 16*lbOfMaterial*(bottlesPerHour/numOfMinutes)
numBottles = bottlesPerHour/numOfMinutes



# These print statements will display your inputs and outputs.
# TODO: When you are ready, uncomment the next two lines.
print("For", bottlesPerHour, "bottles/hr,", lbOfMaterial, "lb/100-bottles, and running for", numOfMinutes, "minutes,")
print("    the factory produces", numBottles, "bottles and consumes", ozOfMaterial, "oz of material")

################################################################################
# 4.) Snowy Lot
# 
# Implement the algorithm from Problem 4 of the Design Document.
#   For your inputs and outputs, create the following variables:
#       - `l` should be called 'lotLengthFt'
#       - `s` should be called 'minutesPerIn'
#       - `t` should be called 'numHoursSnowed'
#       - The total volume of snow should be called 'cubicYdOfSnow'
# 
# Print out the final result with the message "The lot contains cubicYdOfSnow yd^3 of snow"
# 
# After you've implemented your algorithm, make sure to use your tests to verify
# that your algorithm produces the expected results.
# 

# TODO: Your Code Here
