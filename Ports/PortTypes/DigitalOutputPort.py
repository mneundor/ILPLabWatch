#IOInputPort is a port that only reads a on/off signal from a port.
import Ports.abstractPort as AbstractPort
import os


class DigitalOutputPort(AbstractPort.abstractPort):
    #IO Ports can be inverted. That means, 1 -> 0 and 0 -> 1
    inverted = False

    #port description
    description = "Anschlus eines digitalen Verbrauchers."

    #creates the port and set it up in the GPIO settings.
    def __init__(self, externalPort, settings):
        self.inverted = settings["inverted"]
        super.__init__(int(externalPort), settings)
        self.inputPort = False
        #TODO: in production uncomment the following line
        #os.system("gpio -g mode " + str(self.getInternalPort()) + " out")

    def getCurrentInformation(self):
        info = super.getCurrentInformation()
        info["inverted"] = self.inverted
        return info

    #cheks the actual state of the port and returns 0 for an open switch and 1 for a colsed switch
    def getState(self):
        value = 0
        #TODO: In production uncomment the following line and comment the random line.
        #value = int(os.popen("gpio -g read " + str(self.getInternalPort())).read().rstrip())

        if self.inverted == True:
            if value == 1:
                value = 0
            else:
                value = 1
        return value

    def getDescription(self):
        return self.description

    #set the state of the port to 1 or 0. if inverted is on the system respects that
    def setState(self, state):
        if self.inverted == True:
            if state == 1:
                state = 0
            else:
                state = 1
        #TODO: In production uncomment the following line.
        #os.system("gpio -g write " + str(self.getInternalPort()) + " " + str(state))