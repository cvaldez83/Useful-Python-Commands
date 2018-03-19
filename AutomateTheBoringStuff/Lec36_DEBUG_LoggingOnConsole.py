import logging

#logging levels:
    #logging.DEBUG
    #logging.INFO
    #logging.WARNING
    #logging.ERROR
    #logging.CRITICAL

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# EXAMPLE: Buggy Factorial Program

#If you want to disable logging:
logging.disable(logging.CRITICAL)   #comment out to show logging in console

logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial (%s)')
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    return total

print('The factorial is: ' + str(factorial(3)))

logging.debug('End of program')