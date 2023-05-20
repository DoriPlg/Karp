import kivy
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
    )
from kivy.vector import Vector
from kivy.app import App
from kivy.uix.widget import Widget



class KarpoolApp(App):
    def build(self):
        mode = Menu()
        return mode


class MainScreen(Widget):
    def openmenu(self):
        print("~~~~")
        

class Menu(Widget):
    pass



if __name__ == "__main__": 
    KarpoolApp().run()

