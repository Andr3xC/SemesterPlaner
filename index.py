from props import *

class User:
    pass # Se añade en actualizaciones futuras

class Materia:

    def __init__(self, subject):
        self.subject = subject
        self.status = None
        self.value = self.set_value()

    def set_value(self):
        if self.subject not in  subjet_list:
            raise Exception("materia no encontrada")

        for objetive_subject in subjet_list:
            if self.subject == objetive_subject:
                self.value = subjet_list[self.subject]

    def get_value(self):
        return self.value

    def set_status(self, subjet):
        for 

    def get_status(self, subjet):
        pass
    
    
materia = Materia("AYED")
print(materia.get_value())