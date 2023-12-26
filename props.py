from Test_database import *
    
class User:
    pass # Se añade en actualizaciones futuras

class Subjet:
    def __init__(self, subjet):
        self.subjet = subjet
        self.status = self.SetStatus()
        self.Fails = 0
        self.Passed = False
        
    #----Get zone----#
    def setStatus(self, new_status):
        if self.Passed != new_status:
            self.status = new_status
    
    #----Get zone----#
    def getStatus(self):
        return self.status
    
    def getFails(self):
        return self.Fails 

class Graph_props:
    def __init__(self):
        self.width = 720
        self.height = 1280
        self.resizable = False