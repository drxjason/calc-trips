# IDEA: Create a CLI Version
# PROGRESS: Incomplete (Finish CLI)

import argparse
from tkinter import ttk
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont # dk if necessary now

class parsed:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description='calculate cost of trips')

		self.parser.add_argument('-c', '--cost', metavar='$$/gal', type=float)
		self.parser.add_argument('-r', '--round', action='store_true')
		self.parser.add_argument('-d', '--distance', metavar='mileage', type=float)
		self.parser.add_argument('-m', '--mpg', metavar='FUEL_ECONOMY')

		self.args = self.parser.parse_args()

class calcmpg(parsed):
	def __init__(self):
		super().__init__()
		self.root = Tk()
		self.root.title("Trip Calculator -- drxjason")
		self.root.geometry('300x450')
		self.root.resizable(False, False)

	def ttkWidgetsInit(self):
		def calcCost(mpg, distance, gasPrice):
			try:
				gasUsed = float(distance) / float(mpg)
				cost = float(gasUsed) * float(gasPrice)
				placeholder_lbl_sv.set("your trip costs: ")
				totalCost_sv.set(f'${round(cost, 2)}')
			except ValueError:
				print('err: missing one or more values')
				pass

		def calcCostRound(mpg, distance, gasPrice):
			try:
				gasUsed = float(distance) / float(mpg)
				cost = float(gasUsed) * float(gasPrice)
				placeholder_lbl_sv.set("your round trip costs:")
				totalCost_sv.set(f'${round(cost*2, 2)}')
			except ValueError:
				print('err: missing one or more values')
				pass

		content = ttk.Frame(self.root, padding=(3, 3, 12, 12))
		content.grid(column=0, row=0, sticky=(N, S, E, W))

		mpg_lbl = ttk.Label(self.root, text='FEconomy')
		mpg_lbl.grid(column=0, row=0, padx=10, pady=10)

		mpg_sv = StringVar()
		mpg = ttk.Entry(self.root, width=5, textvariable=mpg_sv)
		mpg.grid(column=1, row=0, padx=5, pady=10)

		mpg_unit = ttk.Label(self.root, text='mpg')
		mpg_unit.grid(column=2, row=0)

		distance_lbl = ttk.Label(self.root, text='Distance')
		distance_lbl.grid(column=0, row=1, padx=10, pady=10)

		distance_sv = StringVar()
		distance = ttk.Entry(self.root, width=5, textvariable=distance_sv)
		distance.grid(column=1, row=1, padx=5, pady=10)

		distance_unit = ttk.Label(self.root, text='miles')
		distance_unit.grid(column=2, row=1, sticky=W)

		gasPrice_lbl = ttk.Label(self.root, text='PricePerGal $')
		gasPrice_lbl.grid(column=0, row=2)

		gasPrice_sv = StringVar()
		gasPrice = ttk.Entry(self.root, width=5, textvariable=gasPrice_sv)
		gasPrice.grid(column=1, row=2, padx=5, pady=10)

		gasPrice_unit = ttk.Label(self.root, text='gal')
		gasPrice_unit.grid(column=2, row=2, sticky=W)

		calculatebtn = ttk.Button(self.root, text='calculate', command=lambda: calcCost(mpg_sv.get(), distance_sv.get(), gasPrice_sv.get()))
		calculatebtn.place(relx=0.1, rely=0.3)
		calculateRoundbtn = ttk.Button(self.root, text='calculate round trip', command=lambda: calcCostRound(mpg_sv.get(), distance_sv.get(), gasPrice_sv.get()))
		calculateRoundbtn.place(relx=0.5, rely=0.3)

		placeholder_lbl_sv = StringVar()
		placeholder_lbl = ttk.Label(self.root, textvariable=placeholder_lbl_sv)
		placeholder_lbl.config(font=(30))
		placeholder_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

		totalCost_sv = StringVar()
		totalCost = ttk.Label(self.root, textvariable=totalCost_sv)
		totalCost.config(font=20)
		totalCost.place(relx=0.5, rely=0.6, anchor=CENTER)

	def initialize(self):
		self.root.mainloop()

if __name__ == '__main__':
	p = parsed()
	calc = calcmpg()
	calc.ttkWidgetsInit()
	calc.initialize()
