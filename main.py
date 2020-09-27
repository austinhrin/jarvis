from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial


import application

class MainApp(App):
    def build(self):
        main_layout = GridLayout(cols=2)

        # Master text
        self.master_text = Label(
            text='Master: ', font_size=30)
        main_layout.add_widget(self.master_text)

        # Master input
        self.master_input = TextInput(
            text='Austin', multiline=False, readonly=False, halign='right', font_size=30
        )
        main_layout.add_widget(self.master_input)

        # use clock to schedule a loop with kivy
        # when setting up a loop in kivy with a function you need to use the partial command
        # when using the partial command you need to set your function to have two arguments
        #Clock.schedule_interval(partial(self.update), 1/2)

        return main_layout

    def update(self, instance):
        a = application.main_loop()
        if a == 'break':
            app.stop()


if __name__ == '__main__':
    app = MainApp()
    app.run()
