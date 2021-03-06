#Abstract port already implements all neccessary funcitons to deal with ports. The real functionality of the ports is implemented in the ports classes which are child classes of the abstract port.
import ConfModule.confAdapter as confAdapter
import LogModule.logWriter as logWriter

class abstractPort():
    #the Port Number on the Connector Box
    externalNumber = 0
    #The internal Rasberry Pi Port.
    internalPort = 0
    # the actual settings of the Port
    settings = {}
    #the settings of the Port.
    superSettings = {}
    #super Options
    superOptions = {
        "name": {
            "type": "text",
            "tab": -4,
            "name": "Portbezeichnung",
            "description": "Der Name des Ports bestehend aus a-z, A-Z und 0-9. Keine Leer- oder Sonderzeichen.",
            "standard": "",
            "final": True
        },
        "logCycle": {
            "type": "number",
            "name" : "Logintervall",
            "description": "Das Loginterval in Sekunden",
            "standard": 5,
            "min": 1,
            "max": 3600,
            "step": 1,
            "tab": -2,
            "final": False
        },
        "logging": {
            "type": "boolean",
            "name": "Logging",
            "description": "Wenn diese Einstellung aus ist, so wird der Port nicht geloggt.",
            "standard": 1,
            "tab": -3,
            "final": False
        }
    }

   #initialise the Instance and Class Constants
    def __init__(self, externalNumber, settings):
        self.externalNumber = externalNumber
        self.settings = self.superSettings.copy()
        self.settings.update(settings)
        self.internalPort = confAdapter.getInternalPort(self.getType(), externalNumber)

    def getExternalPort(self):
        return self.externalNumber

    def getInternalPort(self):
        return self.internalPort

    def getName(self):
        return self.settings["name"]

    def getType(self):
        return self.__class__.__name__

    def getLogCycle(self):
        return self.settings["logCycle"]

    #The logging setting is true if the port is monitored by the logging protocols.
    def getLoggingSetting(self):
        return self.settings["logging"]

    #writes the state of the port in the log file.
    def writeLog(self):
        logWriter.writeLog(self)

    #retuns the description of a port. Should be implemented in the child class
    def getDescription(self):
        return self.description

    #returns the state of a port. has to be implemented in child class
    def getState(self):
        raise NotImplementedError("Method not implemented in child class.")

    def getCurrentInformation(self):
        info = self.getSettings()
        info["port"] = self.externalNumber
        info["type"] = self.__class__.__name__
        info["state"] = self.getState()
        return info

    # returns the possible options of the Port.
    def getOptions(self):
        raise NotImplementedError("Method not implemented in child class.")

    # returns all settings related to the port.
    def getSettings(self):
        return self.settings

    # returns the range of available Values (important for charts and alerts). The return is a list with the format: [lowest,highest,step]
    def getValueRange(self):
        raise NotImplementedError("Method not implemented in child class.")