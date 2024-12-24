from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from datetime import datetime
from kivy.uix.popup import Popup
from kivy.utils import platform
import time

if platform not in ["android", "ios"]:
    Window.size = (350, 600)


class Dashboard(Screen):
    day = datetime.today().strftime('%A')


class Cameraa(Screen):
    timestr = time.strftime("%Y%m%d_%H%M%S")
    fileName = f'IMG_{format(timestr)}.png'

    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("captures/IMG_{}.png".format(self.timestr))

        popup = Popup(title='Test popup',
                      content=MDLabel(text=f'{self.fileName} is saved successfully. \n\nYou look beautiful!'),
                      auto_dismiss=True, size_hint=(None, None), size=(300, 200))
        popup.open()


class Calculator(Screen):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, num):
        if self.ids.calc_input.text == '0':
            self.ids.calc_input.text = ''
        self.ids.calc_input.text += f'{num}'

    def add(self):
        self.ids.calc_input.text += '+'

    def substract(self):
        self.ids.calc_input.text += '-'

    def multiply(self):
        self.ids.calc_input.text += '*'

    def devide(self):
        self.ids.calc_input.text += '/'

    def equal(self):
        prior = self.ids.calc_input.text

        if '+' in prior:
            num_list = prior.split('+')
            answer = 0
            for num in num_list:
                answer += int(num)
            self.ids.calc_input.text = f'{answer}'

        if '-' in prior:
            num_list = prior.split('-')
            answer = 0
            for num in num_list:
                answer -= int(num)
            self.ids.calc_input.text = f'{answer}'

        if '*' in prior:
            num_list = prior.split('*')
            answer = 1
            for num in num_list:
                answer *= int(num)
            self.ids.calc_input.text = f'{answer}'

        if '/' in prior:
            num_list = prior.split('/')
            answer = 0
            for num in num_list:
                answer /= int(num)
            self.ids.calc_input.text = f'{answer}'

    class FileManagerr(Screen):
        pass


class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return Builder.load_file('styles/style.kv')


if __name__ == '__main__':
    MyApp().run()
