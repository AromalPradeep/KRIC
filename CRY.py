# Imports

# Kivy
import kivy
from kivy.app import App

from kivy.lang import Builder

kvfile = Builder.load_string(""" 
Label: 
    text: 'Hello '
    markup: True 
    font_size: '64pt' 
""") 

# App
class CryApp(App):
    
    def build(self):
        return kvfile

# Call
if __name__ == "__main__":
    CryApp().run()
    