import sys
import time
import emoji

def animation(process, num):
    symbol = "|/-\\"
    for i in range(num):
        time.sleep(0.1)
        sys.stdout.write("\r" + symbol[i % len(symbol)])
        sys.stdout.flush()
    if process == 'start':
        print('Start!' + emoji.emojize(':+1:', use_aliases=True))
    else:
        print('Bye!' + emoji.emojize(':heart_eyes:', use_aliases=True))
