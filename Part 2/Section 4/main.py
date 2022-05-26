from tkinter import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


#interface
class Inti(FloatLayout):
    layout = BoxLayout()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="Hello", size_hint=(0.25, 0.25), pos=(200, 100))
        self.layout.add_widget(b1)
        self.add_widget(self.layout)
    pass


#app  creation
class TestApp(App):
    pass


TestApp().run()