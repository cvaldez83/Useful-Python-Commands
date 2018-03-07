import time
import webbrowser

total_breaks = 3
break_count = 0

print('this program started on ' + time.ctime())

while break_count < total_breaks:
    time.sleep(15)
    webbrowser.open('https://www.youtube.com')
    break_count += 1
    