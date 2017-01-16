#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle
import os

font_folder = "/usr/share/fonts/truetype/"
font_type = "/usr/share/fonts/truetype/fireflysung.ttf"
sample_text = u"Hello World. by 江遲 (tsuân pōo tàn lo̍h khì)"


def update_rect(instance, value):
	instance.rect.pos = instance.pos
	instance.rect.size = instance.size

class FontsList(GridLayout):
	def __init__(self, **kwargs):
		super(FontsList, self).__init__(**kwargs)
		self.cols=2
		self.spacing=2
		#self.size_hint_y=None
		self.bind(minimum_height=self.setter('height'))
		self.show_fonts_list()

	def show_font(self, s_text, f_type, color):
		#lbl = Label(text=s_text, font_name=f_type, font_size=16, size_hint_y=None, halign='left')
		lbl = Label(text=s_text, font_name=f_type, font_size=16, size_hint_y=None, width=Window.width, text_size=(Window.width/self.cols, None))
		lbl.texture_update()
		lbl.size = lbl.texture_size

		with lbl.canvas.before:
			Color(*color)
			lbl.rect = Rectangle(pos=lbl.pos, size=lbl.size)
			lbl.bind(pos=update_rect, size=update_rect)
		self.add_widget(lbl)

	def show_fonts_list(self):
		font_files = os.listdir(font_folder)

		for f in font_files:
			self.show_font(f, font_folder+f, [0.4, 0.4, 0.4])
			self.show_font(sample_text, font_folder+f, [0.2, 0.2, 0.8])
		

class TestApp(App):
	def build(self):
		self.Flist = FontsList()
		return self.Flist

if __name__ == '__main__':
	TestApp().run()
