'''
Codes for MP3 player Raspberry Pi
library needed: subprocessor / mpg321 (sudo apt-get install mpg321 / pip3 install mpyg321)

Take note to test the Library within console prior to using it.
mpg321 sample.mp3 #sample.mp3 is included within the repository
'''
import subprocess,time

while True:
    subprocess.call(["/usr/bin/mpg321", "sample.mp3"])
    time.sleep(10)