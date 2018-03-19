#THE FOLLOWING SENDS TO TRASH (SAFER THAN PERMANENT DELETE)
#I'll need to install send2trash
import send2trash
send2trash.send2trash('c:\\delicious\\importantFile.txt')

#THE FOLLOWING PERMANENTLY DELETES
import os
#delete a single file
os.unlink('bacon.txt')

#delete a whole folder (folder must be empty)
os.rmdir('c:\\delicious')

#delete a folder including its contents
import shutil
shutil.rmtree('c:\\delicious')

#delete .txt file extensions
os.chdir('c:\\delicious')
for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
