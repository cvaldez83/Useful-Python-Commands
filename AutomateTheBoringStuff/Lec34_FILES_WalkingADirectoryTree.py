#You can "walk" thru a folder and all of its contents.
#In this example, 'delicious' is a parent folder that has bunch of sub-files & sub-folders

import os
for folderName, subfolders, filenames in os.walk('F:\\Google Drive\\5.0 Programming\\Python'):
    print("The folder is " + folderName)
    print('The subfolders in ' + folderName + ' are:' + str(subfolders))
    print('The filenames in ' + folderName + ' are:' + str(filenames))
    print()

    #if you wanted to remove certain folder
    for subfolder in subfolders:
        if 'fish' in subfolder:
            #os.rmdir(subfolder)  <--Commented out for safety
    #if you wanted to copy only files that end with .py
    for file in filenames:
        if file.endswith('.py')
            shuttil.copy(os.join(folderName,file), os.join(folderName,file + '.backup'))