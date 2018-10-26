#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  build_ai_car.py
#
#  Copyright 2018 Jed Unalivia <jaunalivia@jaunalivia-X540UP>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import time

# CLASSES
# The Car class
class Car_ai_upgrade():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def assess_order(self):

		print("Order assessment initiate...")
		print("Progress: 0 %")
		time.sleep(1)

		print("\tMake: " + self.make.title())
		time.sleep(1)
		print("\tModel: " + self.model.title())
		time.sleep(1)
		print("\tYear: " + str(self.year))
		time.sleep(2)

		progress = 0.0
		for x in range(0,101):
			print("\n" *100)
			print("Assessment ongoing...")
			print("Stage progress: " + str(progress + x) + " %")
			time.sleep(0.25)

		print("Order assessment complete!")
		print("Progress: 25 %")
		time.sleep(2)

	def read_odometer(self):
		print("\nThis car has " + str(self.odometer_reading) + " miles on it.")

	def build_hardware(self):
		print("\nAssemby line operation initiate...")
		time.sleep(3)
		print("\nNow building hardware matching the following specs...")
		print("\tMake: " + self.make.title())
		print("\tModel: " + self.model.title())
		print("\tYear: " + str(self.year))

		progress = 0.0
		for x in range(0,50):
			print("\n" *100)
			print("Setting up assembly line...")
			print("Stage progress: " + str(progress + x) + " %")
			time.sleep(0.25)

		time.sleep(5)
		print("\nApplying mechanical modifications...")
		time.sleep(2)

		progress = 0.0
		for x in range(50,76):
			print("\n" *100)
			print("Mechanical modification ongoing...")
			print("Stage progress: " + str(progress + x) + " %")
			time.sleep(0.25)

		time.sleep(5)
		print("\nApplying electrical and electronic modifications...")
		time.sleep(2)

		progress = 0.0
		for x in range(75,101):
			print("\n" *100)
			print("Electrical and electronic modification ongoing...")
			print("Stage progress: " + str(progress + x) + " %")
			time.sleep(0.10)

		time.sleep(5)
		print("\nHardware assembly complete!")
		print("Progress: 50 %")
		time.sleep(2)

	def install_AIsoftware(self):

		progress = 0.0
		for x in range(0,50):
			print("\n" *100)
			print("\nAI software installation initiate...")
			print("Stage progress: " + str(progress + x) + " %")
			time.sleep(0.20)

		progress = 0.0
		for x in range(50,101):
			print("\n" *100)
			print("\nSoftware installation ongoing...")
			print("Stage progress: " + str(progress + x) + " %")
			time.sleep(0.10)

		time.sleep(5)
		print("\nAI software installation complete!")
		print("Self Driving Car is ready for testing.")
		print("Progress: 100 %")
# Customer Order Details:
print("Customer Order Details:\n")
brand_name = input("Automobile Make: ")
model_name = input("Model Name: ")
year_model = input("Year Model: ")

# Create the module using Car_ai_upgrade class
customer01 = Car_ai_upgrade(brand_name, model_name, year_model)

customer01.odometer_reading = input("Enter Odometer Reading: ")

customer01.assess_order()
customer01.read_odometer()
customer01.build_hardware()
customer01.install_AIsoftware()
