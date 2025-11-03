import winsound
import random
import time


freq = 200

while freq < 2100:
    winsound.Beep(freq, 500)
    freq += 100

#winsound.Beep(freq, 500)
#time.sleep(0.3) #pause between beeps
