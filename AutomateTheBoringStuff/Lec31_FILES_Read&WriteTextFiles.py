
#open text file (no a real file path)
helloFile = open('c:\\users\\cesar\\hello.txt')

#returns contents of file into a single string (can only use once. open again to re-read)
helloFile.read()
#create variable for content of file
content = helloFile.read()
#close file
helloFile.close()
#returns contents of file into multiple strings (one per line)
helloFile.readlines()

#open file in write mode
helloFile = open('c:\\users\\cesar\\hello.txt','w')
#open file in append mode (does not overwrite contents that are already there)
helloFile = open('c:\\users\\cesar\\hello.txt','a')
#write to file
helloFile.write('hellooooo!!!')

#you can also store values in a binary file
import shelve
#returns a dictionary-like shelf value
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon']
shelfFile.close()

