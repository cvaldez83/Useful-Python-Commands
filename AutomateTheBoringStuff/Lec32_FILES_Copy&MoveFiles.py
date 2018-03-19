
import shutil

#copy a file from c:\ to c:\delicious
shutil.copy('c:\\spam.txt','c:\\delicious')

#copy file AND rename
shutil.copy('c:\\spam.txt','c:\\delicious\\spam_v2.txt')

#copy an entire folder (and its contents)
shutil.copytree('c:\\delicious','c:\\delicious_backup')

#move file to new location  (use this to rename files as well)
shutil.move('c:\\spam.txt','c:\\delicious\\walnut')

