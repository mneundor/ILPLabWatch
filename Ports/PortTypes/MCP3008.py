from Ports.abstractPort import abstractPort

#Klasse zum Auslesen und Manipulieren der GPIOs
import RPi.GPIO as GPIO
import time
# Ein Port zur Kommunikation mit dem MCP3008 AD-Wandler

class MCP3008(abstractPort):
	description = "Ein Port zur Kommunikation mit dem MCP3008 AD-Wandler."
	options = {
	}
	def __init__(self, externalPort, settings):
		super().__init__(externalPort, settings)
	def getState(self):
		#Pinbelegung auf der Prototypplatine
		dout = 23
		din = 24
		cs = 25
		clk = 18
		retval = list(range(8))
		#GPIO Einstellungen vornehmen
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(clk,GPIO.OUT)
		GPIO.setup(din,GPIO.OUT)
		GPIO.setup(dout,GPIO.IN)
		GPIO.setup(cs,GPIO.OUT)
		#Folgende Routine dient dem Auslesen aller acht Kanäle:        
		for ind in range(8):
			#Pins "resetten"
			GPIO.output(cs,True)
			GPIO.output(cs, False)
			GPIO.output(clk, False)
			cmd = ind  
			cmd |= 0b00011000
			for i in range(5):
				if(cmd & 0x10):
					GPIO.output(din, True)
				else:
					GPIO.output(din, False)
				GPIO.output(clk, True)
				GPIO.output(clk, False)
				cmd <<= 1
			adchvalue = 0
			for i in range(11):
				GPIO.output(clk, True)
				GPIO.output(clk, False)
				adchvalue <<=1
				if(GPIO.input(dout)):
					adchvalue |= 0x01
		
			retval[ind] = adchvalue		
		#time.sleep(0.5)
		#print(retval)
		return retval
	def getValueRange(self):
		return [0, 1023, 1]
	def getOptions(self):
		options = super().superOptions.copy()
		options.update(self.options)
		return options
 
