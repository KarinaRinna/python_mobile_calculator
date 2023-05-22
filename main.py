from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class CalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Calculator", halign="center")


CalculatorApp().run()