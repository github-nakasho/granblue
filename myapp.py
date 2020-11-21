#!/usr/bin/env python3

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty


class MyLabel(Label):
    time = NumericProperty(0)
    def on_time(self, *args):
        self.text = str(self.time)

class MyButton(Button):
    evt = None
    def on_press(self):
        if self.text == 'start':
            self.evt = Clock.schedule_interval(self.cb, 0.2)
            self.text = 'stop'
        else:
            self.evt.cancel()
            self.text = 'start'
    def cb(self, dt):
        self.parent.lbl.time = round(self.parent.lbl.time+0.2, 1)

class StopWatchApp(App):
    def build(self):
        layout = BoxLayout()
        layout.lbl = MyLabel(text='0')
        layout.btn = MyButton(text='start')
        layout.add_widget(layout.lbl)
        layout.add_widget(layout.btn)
        return layout
