# Using example: 2012 Chrysler 200 Sedan 4D LX, miles per gallon = 25 mpg

import argparse
from tkinter import ttk
from tkinter import *
import tkinter as tk

class parsed:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description='calculate cost of trips')

		self.parser.add_argument('-c', '--cost', metavar='$$/gal', type=float)
		self.parser.add_argument('-r', '--round', action='store_true')
		self.parser.add_argument('-d', '--distance', metavar='mileage', type=float)
		self.parser.add_argument('-m', '--mpg', metavar='FUEL_ECONOMY')

		self.args = parser.parse_args()

class calcmpg(parsed):
	def __init__(self):
		super().__init__()
		self.root = Tk()
		self.root.title("Trip Calculator -- drxjason")
		self.root.geometry('510x380')
		self.root.resizable(False, False)

	def ttkWidgetsInit(self):
		def calcCost(mpg, distance, gasPrice):
			gasUsed = distance / mpg

	def initialize(self):
		self.root.mainloop()



if __name__ == '__main__':
	p = parsed()
	calc = calcmpg()
	calc.ttkWidgetsInit()
	calc.initialize()
