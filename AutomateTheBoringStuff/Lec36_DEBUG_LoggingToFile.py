import logging

#logs to text file called "myProgramLog.txt" in working directory
logging.basicConfig('myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')