import time
import webbrowser

count = 0
print('Program started at', time.ctime())
while count < 3:
    time.sleep(2*60*60)
    webbrowser.open('https://www.youtube.com/watch?v=nIjVuRTm-dc')
    count += 1
