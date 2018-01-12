from gpiozero import MotionSensor

pir = MotionSensor(23)

while True:
        pir.wait_for_motion()
        print("You moved")
        pir.wait_for_no_motion()
