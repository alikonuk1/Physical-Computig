 from gpiozero import LED
 from time import sleep

led = LED(17)
led1 = LED(14)
led2 = LED(15)

while True:
    led.on()
    sleep(1)
    led.off()
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(1)
    led2.off()
    sleep(0)

    
    
