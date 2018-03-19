
#raise Exception('This your custom error message.')  <--Commented out to avoid raising error

"""
The function will create a box like this:
*************
*           *
*           *
*           *
*************

"""

#THIS CODE WORKS BUT IS SUSCEPTIBLE TO BUGS
def boxPrint(symbol, width, height):
    print(symbol*width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
boxPrint('*',20,5)

#THIS CODE IS THE SAME BUT WITH BUG FIXES
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a single character')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2')

    print(symbol*width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
boxPrint('*',20,5)
