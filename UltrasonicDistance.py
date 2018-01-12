from gpiozero import DistanceSensor
 
ultrasonic = DistanceSensor(echo=21, trigger=20, threshold_distance=0.5, max_distance=2)
 
#ultrasonic.distance()
#ultrasonic.threshold_distance = 0.5
#ultrasonic.max_distance = 2
 
while True:
      print(ultrasonic.distance)

while True:
      ultrasonic.wait_for_in_range()
      print("In range")
      ultrasonic.wait_for_out_of_range()
      print("Out of range")
      
     
