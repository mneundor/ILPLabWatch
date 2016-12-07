from Ports.abstractPort import abstractPort

#Klasse zum Auslesen und Manipulieren der GPIOs
import Adafruit_DHT as DHTx 

# Ein Port zur Kommunikation mit dem MCP3008 AD-Wandler

class DHT22(abstractPort):
	description = "Ein Port zur Kommunikation mit dem DHT22."
	options = {
	}
	def __init__(self, externalPort, settings):
		super().__init__(externalPort, settings)
	def getState(self):
		#Welcher Pin?
		pin = 5
		sensor = DHTx.DHT22
		humtemp = DHTx.read_retry(sensor,pin)
		return list(humtemp)
	def getValueRange(self):
		return [0, 1023, 1]
	def getOptions(self):
		options = super().superOptions.copy()
		options.update(self.options)
		return options
 
