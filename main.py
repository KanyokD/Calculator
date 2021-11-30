from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('calculator.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.text_input.text = '0'

    def button_press(self, button):
        value = self.ids.text_input.text

        if "The operation is faulty" in value:
            value = ''

        if value == "0":
            self.ids.text_input.text = ''
            self.ids.text_input.text = f'{button}'
        else:
            self.ids.text_input.text = f'{value}{button}'

    def remove(self):
        value = self.ids.text_input.text
        value = value[:-1]
        self.ids.text_input.text = value

    def minus(self):
        value = self.ids.text_input.text
        if "-" in value:
            self.ids.text_input.text = f'{value.replace("-", "")}'
        else:
            self.ids.text_input.text = f'-{value}'

    def dot(self):
        value = self.ids.text_input.text
        num_list = value.split("+")

        if "+" in value and "." not in num_list[-1]:
            value = f'{value}.'
            self.ids.text_input.text = value

        elif "." in value:
            pass
        else:
            value = f'{value}.'
            self.ids.text_input.text = value

    def math_sign(self, sign):
        value = self.ids.text_input.text

        self.ids.text_input.text = f'{value}{sign}'

    def equals(self):
        value = self.ids.text_input.text
        try:
            answer = eval(value)
            self.ids.text_input.text = str(answer)
        except:
            self.ids.text_input.text = "The operation is faulty"


class Calculator(App):
    def build(self):
        return MyLayout()


Calculator().run()