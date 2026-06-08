from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

# Set up the size of the window
Window.size = (600, 400)
Window.minimum_width = 600
Window.minimum_height = 400


def flo_convert(flo: str):
    base_flo = 0.5
    result = 0
    flo_arr = flo.split('.')
    int_part = int(flo_arr[0], 2)
    flo_part = flo_arr[1]
    for each in flo_part:
        if each == '1':
            result += base_flo
        base_flo /= 2
    result += int_part
    return result


# The main class of the app
class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.kivy_input.text = "Enter a Decimal number"
            self.converted.text = ""
            self.label.text = ""
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.kivy_input.text = "Enter a Binary number"
            self.converted.text = ""
            self.label.text = ""
        print("working")

    def convert(self, args):
        try:
            if self.state == 0:
                val = int(self.kivy_input.text, 2)
                self.converted.text = str(val)
                self.label.text = "in decimal is:"
            else:
                val = bin(int(self.kivy_input.text))
                self.converted.text = val[2:]
                self.label.text = "in binary is:"
        except ValueError:
            if self.state == 0:
                self.label.text = "Please enter correct binary number"
            else:
                self.label.text = "Please enter correct decimal number"

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "BlueGray"
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-left", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # Logo
        screen.add_widget(Image(
            source="kivy_logo.png",
            pos_hint={"center_x": 0.5, "center_y": 0.7}
        ))

        # Collect user input
        self.kivy_input = MDTextField(
            text="Enter a binary number",
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size=38
        )
        screen.add_widget(self.kivy_input)

        # secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Secondary"
        )

        self.converted = MDLabel(
            # text="888",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="Button"
        )

        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size=40,
            font_style="H6",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.convert  # Connect the button to a function
        ))

        return screen


if __name__ == '__main__':
    ConverterApp().run()
