import flet as ft 
from Props import *

def main(page: ft.Page):
    
    props = Graph_props()
    #Specs
    page.title = "Semester Planer"
    page.window_width = props.width
    page.window_height = props.height
    page.window_resizable = props.resizable
    page.padding = 0
    
    container = ft.Container(props.height , props.width)
    
    list_view = ft.ListView(expand=True, spacing= 10)        
    for i in range(5000):
        list_view.controls.append(ft.Text(f"Line {i}"))
    page.add(list_view)
        
ft.app(target=main)