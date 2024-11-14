# calculator.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        # Define the layout
        layout = GridLayout(cols=4)
        
        # Define the input field
        self.display = TextInput(multiline=False, readonly=True, halign="right", font_size=32)
        layout.add_widget(self.display)

        # Define buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+',
            '='
        ]

        for button in buttons:
            btn = Button(text=button, font_size=24, on_press=self.on_button_press)
            layout.add_widget(btn)

        return layout

    def on_button_press(self, instance):
        if instance.text == "C":
            self.display.text = ""
        elif instance.text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except Exception:
                self.display.text = "Error"
        else:
            self.display.text += instance.text

# Run the app
if __name__ == '__main__':
    CalculatorApp().run()
