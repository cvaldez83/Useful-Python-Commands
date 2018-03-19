#To use this code either pass arguments or copy an address.
# This code will open a web browser and open google maps

import webbrowser, sys, pyperclip

sys.argv # ['mapti.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:   # Without arguments, the length is 1
    # # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
print(address)
webbrowser.open("https://www.google.com/maps/place/" + str(address))

