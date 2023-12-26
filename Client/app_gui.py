import tkinter as tk 
from tkinter import ttk

opciones = ["Sistemas", "Civil", "Electrica"]  #pruebas temporales (se reemplaza con la base de datos)

class Multiple_option_menu:
    def __init__(self, options, root):
        self.options = options
        self.root = root
        self.variable = tk.StringVar(self.root)
        self.variable.set(self.options[0])
        self.menu_seleccion = ttk.OptionMenu(self.root, self.variable, self.options, command=self.on_seleccion)
        self.etiqueta_resultado = tk.Label(self.root, text="Opción seleccionada: ")
        
    def on_seleccion(self, event):
        seleccion = self.variable.get()
        self.etiqueta_resultado.config(text="Opción seleccionada: " + seleccion)



class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 1080, height = 720)
        self.root = root
        self.pack() 
        self.config(bg = "grey")
        self.grade_select()

    
    def grade_select(self):
        
        variable = tk.StringVar()
        

        #---- First carrer ----#
        self.labe_grade_1 = tk.Label(self, text = "Primer carrera:")
        self.labe_grade_1.grid(row = 0, column = 0, padx = 10, pady= 10)
        self.labe_grade_1.config(font=("Times New Roman", 12, "bold"))
        
        
        #perate a ver si puedo metr esas vainas del menu como un objeto 
        #aparte y nos ahorramos despus la misma wea de codigo, aparte nos puede servir para mas adelante
        """ self.select_carrer = ttk.OptionMenu(self, variable, opciones)
        self.select_carrer.grid(row = 0, column = 1) """
        
        self.select_carrer = Multiple_option_menu(opciones,self.root)
        
        
        #---- Second carrer ----#
        
        self.labe_grade_2 = tk.Label(self, text = "Segunda carrera:")
        self.labe_grade_2.config(font=("Times New Roman", 12, "bold"))
        self.labe_grade_2.grid(row = 1, column = 0, padx = 10, pady= 10)
    
    def subjets_select(self):
        pass