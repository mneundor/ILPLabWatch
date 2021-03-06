#this adapter can be used for working with conf Files. All conf files are keept up to date by this functions
import ConfModule.confReader as confReader

#adds a new port to the configuration
#name: the display name of the port, port: the port on the connector Box, logged: True or False, loginterval: the loginterval in secondes
def addPort(port):
    portConf = confReader.readPortConf()
    portConf[port.getExternalPort()] = port.getSettings()
    confReader.writePortConf(portConf)

#gets the port information of all ports.
def getPortsConf():
    return confReader.readPortConf()

#gets the internal Number of an external Port. nedds also the type of the port.
def getInternalPort(type, externalPort):
    return confReader.readWiringConf()[type][str(externalPort)]

#returns all ports of a type.
def getInternalPorts(type):
    try:
        return confReader.readWiringConf()[type]
    except:
        return {}

#returns the configuration of one port by the external Port number
def getPortConf(externalPort):
    return confReader.readPortConf()[str(externalPort)]