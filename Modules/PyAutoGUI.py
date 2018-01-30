import pyautogui


# #useful mouse control commands
# click()
# click([x,y])
# doubleClick()
# rightClick()
# moveTo(x,y[, duration=seconds])
# moveRel(x_offset,y_offset[,duration=seconds])
# position()  #returns(x,y) tuple
# size()      #returns (width,height) tuple
# displayMousePosition()

pyautogui.displayMousePosition()


# #useful keyboard control commands
# typewrite('Text goes here'[, interval=secs])
# press('pageup')
# pyautogui.KEYBOARD_KEYS
# hotkey('ctrl','o')

# #image recognition
# pyautogui.locateOnScreen(imageFilename) # returns location (left, top, width, height) tuple or none of image found on screen
# pyautogui.locateCenterOnScreen(imageFilename) # returns location of center of imageFilename
