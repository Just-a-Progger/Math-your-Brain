# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
import random
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.core.window import Window


Right=0
Wrong=0

class mainApp:
    def __init__(self):
        self.Right = 0
        self.Wrong = 0

class MainWindow(Screen, mainApp):
    pass


class EzyWindow(Screen):
    def get_rang(self):
        return str(random.randrange(1, 10))

    def get(self):
        return str(random.randrange(-1, 1))

    r1c1 = StringProperty(str(2))
    r1c2 = StringProperty(str(2))
    r2c1 = StringProperty(str(2))
    int = 0


    def upda(self):
        global Right
        global Wrong
        self.int = self.int + 1
        if self.sum+int(self.r2c1)==int(self.r1c1)+int(self.r1c2):
            Right = Right+ 1
        else:
            Wrong = Wrong + 1

        if self.int == 5:
            self.manager.current = "qwe"

        else:
            self.r1c1 = str(random.randrange(1, 10))
            self.r1c2 = str(random.randrange(1, 10))
            self.r2c1 = str(random.randrange(-1, 1))

    def upd(self):
        global Right
        global Wrong
        self.int = self.int + 1
        if self.sum + int(self.r2c1) != int(self.r1c1) + int(self.r1c2):

            Right = Right + 1
        else:
            Wrong = Wrong + 1
        if self.int == 5:
            self.manager.current = "qwe"

        else:
            self.r1c1 = str(random.randrange(1, 10))
            self.r1c2 = str(random.randrange(1, 10))
            self.r2c1 = str(random.randrange(-1, 1))


class SecondWindow(Screen):
    pass


class QWEWindow(Screen):

    def get_rang(self):
        return str(random.randrange(2, 120))

    def get(self):
        return str(random.randrange(-3, 3))

    r1c1 = StringProperty(str(2))
    r1c2 = StringProperty(str(2))
    r2c1 = StringProperty(str(2))
    int = 0



    def upda(self):
        global Right
        global Wrong
        self.int = self.int + 1
        if self.sum + int(self.r2c1) == int(self.r1c1) + int(self.r1c2):
            Right = Right + 1
        else:
            Wrong = Wrong + 1

        if self.int == 5:
            self.manager.current = "multiplication"

        else:
            self.r1c1 = str(random.randrange(2, 120))
            self.r1c2 = str(random.randrange(2, 120))
            self.r2c1 = str(random.randrange(-2, 2))
    def upd(self):
        global Right
        global Wrong
        self.int = self.int + 1
        if self.sum + int(self.r2c1) != int(self.r1c1) + int(self.r1c2):
            Right = Right + 1
        else:
            Wrong = Wrong + 1
        if self.int == 5:
            self.manager.current = "multiplication"

        else:
            self.r1c1 = str(random.randrange(2, 120))
            self.r1c2 = str(random.randrange(2, 120))
            self.r2c1 = str(random.randrange(-2, 2))

class MultiWindow(Screen):
    global Right
    global Wrong
    def get_rang(self):
        return str(random.randrange(2, 20))

    def get(self):
        return str(random.randrange(-2, 2))

    r1c1 = StringProperty(str(2))
    r1c2 = StringProperty(str(2))
    r2c1 = StringProperty(str(2))
    int = 0
    text = StringProperty('')
    text2 = StringProperty('')
    def upda(self):
        global Right
        global Wrong
        self.int = self.int + 1
        if self.sum + int(self.r2c1) == int(self.r1c1) * int(self.r1c2):
            Right = Right + 1
        else:
            Wrong = Wrong + 1

        if self.int == 5:
            self.manager.current = "end"
            self.text = str(Right)
            self.text2 = str(Wrong)

        else:
            self.r1c1 = str(random.randrange(2, 20))
            self.r1c2 = str(random.randrange(2, 20))
            self.r2c1 = str(random.randrange(-2, 2))
    def upd(self):
        global Right
        global Wrong
        self.int = self.int + 1
        if self.sum + int(self.r2c1) != int(self.r1c1) + int(self.r1c2):
            Right = Right + 1
        else:
            Wrong = Wrong + 1
        if self.int == 5:
            self.manager.current = "end"
            self.text=str(Right)
            self.text2 = str(Wrong)
        else:
            self.r1c1 = str(random.randrange(2, 20))
            self.r1c2 = str(random.randrange(2, 20))
            self.r2c1 = str(random.randrange(-2, 2))
class EndWindow(Screen):
    global Right
    global Wrong

    qw=StringProperty("")
    s=StringProperty("")






with open("App.kv", encoding='utf8') as f:
    presentation = Builder.load_string(f.read())
class TestApp(App):

    def build(self):
        return presentation


if __name__ == '__main__':
    TestApp().run()