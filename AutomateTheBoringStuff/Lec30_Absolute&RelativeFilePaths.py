#since Windows, Apple, Linux use different folder path separators (i.e. \ vs / ) python has a module called "os"

import os

#joins path to file called file.png
os.path.join('folder1','folder2','folder3','file.png')

#gets current working directory
os.getcwd()

#change working directory
os.chdir('C:\\')

#provides complete path
os.path.abspath('spam.png')

#detects if something is an absolute path
os.path.isabs('C:\\folder\\folder')

#provides relative path.  Note: second argument is the current path
os.path.relpath('c:\\folder1\\folder2\\spam.png','c:\\folder1')

#provides folder path
os.path.dirname('c:\\folder1,folder2,spam.png')
#provides filename path
os.path.basename('c:\\folder1,folder2,spam.png')

#checks if path exists
os.path.exists('c:\\folder1\\folder2\\spam.png')
#checks if file exists
os.path.isfile('c:\\folder1\\folder2\\spam.png')
#checks if the directory exists
os.path.isdir('c:\\folder1\\folder2')

#returns size
os.path.getsize('c:\\folder1\\folder2\\spam.png')

#returns file & folder names inside path
os.listdir('c:\\folder1,folder2')

#make a new folder
os.makedirs(''c:\\folder1\\folder2\\newfolder')