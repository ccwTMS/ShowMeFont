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
sample_text = u"Hello World. by 台語八聲 (sai hóo pà pih kâu káu tshiūnn lo̍k)"


def update_rect(instance, value):
	instance.rect.pos = instance.pos
	instance.rect.size = instance.size

class FontsList(GridLayout):
	def __init__(self, **kwargs):
		super(FontsList, self).__init__(**kwargs)
		self.cols=2
		self.spacing=2
		self.size_hint_y=None
		self.bind(minimum_height=self.setter('height'))
		self.show_fonts_list()

	def show_font(self, s_text, f_type, color, col_width, f_size):
		lbl = Label(text=s_text, font_name=f_type, font_size=f_size, size_hint_y=None, size_hint_x=None, text_size=(col_width, None))
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
			self.show_font(f, font_folder+f, [0.4, 0.4, 0.4], Window.width/(self.cols)*0.6, 12)
			self.show_font(sample_text, font_folder+f, [0.2, 0.2, 0.8], Window.width/self.cols*1.4, 16)
		

class FontsView(ScrollView):
	layout = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		self.size_hint=(1, None)
		self.size=(Window.width, Window.height)
		super(FontsView, self).__init__(**kwargs)
		self.display_view()

	def display_view(self):
		if self.layout:
			self.remove_widget(self.layout)
		self.layout = FontsList()
		self.add_widget(self.layout)

class TestApp(App):
	def build(self):
		self.FView = FontsView()
		return self.FView

if __name__ == '__main__':
	TestApp().run()
