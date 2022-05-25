from kivy.app import App
from kivy.uix.widget import Widget


#interface
class Interface(Widget):
    def on_enter_pressed(self):
        print("Enter has been pressed!")


#app  creation
class TestApp(App):
    pass


TestApp().run()