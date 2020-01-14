import RPi.GPIO as GPIO
import time

class UltraSonic(object):
	def __init__(self, trig_pin, echo_pin, failsafe_distance = 8):
		GPIO.setmode(GPIO.BCM) # set BCM mode

		# ultrasonic setup
		GPIO.setup(trig_pin, GPIO.OUT)#trig
		GPIO.setup(echo_pin, GPIO.IN)#echo
		
		self.trig_pin = trig_pin
		self.echo_pin = echo_pin
		self.failsafe_distance = failsafe_distance
	
	def startMonitor(self):
		print("start monitoring ultrasonic")
		
		GPIO.output(self.trig_pin, False)
		print("Waiting sensor...")
		time.sleep(0.5)
		
		GPIO.output(self.trig_pin, True)
		time.sleep(0.0001)
		GPIO.output(self.trig_pin, False)
		
		while GPIO.input(self.echo_pin) == False:
			start = time.time()
			
		while GPIO.input(self.echo_pin) == True:
			end = time.time()
			
		time_dif = end-start
		
		## for cm:
		# multiply with sound/sonic speed (34300 cm/s)
		#  then divide by 2(because travel time go and back)
		distance = (time_dif*34300)/2
		return distance
					
	def ultraClearGPIO(self):
		print("clearing ultrasonic gpio...")
		GPIO.cleanup()


trig=16 #GPIO pin number for trig
echo=20 #GPIO pin number for echo

Usonic = UltraSonic(trig, echo)

try:
	while distance > True:	
		distance = Usonic.startMonitor()
		print("distance in cm: {}".format(distance))
					
except Exception as ex:
	print(ex)
	GPIO.cleanup()
except KeyboardInterrupt as ke:
	print("Keyboard Interupted")
finally:
	GPIO.cleanup()

