M = '\033[031m'
H = '\033[032m'

import os
import random
import sys
import time
from time import sleep
os.system('clear')
def mengetik(s):
    for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(random.random() + 0.4)
print (M +'loading.....')
sleep (0.1)
mengetik (H +'》》》》》》》》》》》》100%')
os.system('clear')
