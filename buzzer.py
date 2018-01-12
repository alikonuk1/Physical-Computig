from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(2)

buzzer.on()
buzzer.off()

while True:
   buzzer.beep()
   
   
