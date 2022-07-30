"""Compound interest calculator.
This calculator takes the starting amount of money, the interest rate and the number of years.
the calculator will return the investment with the compound interest and the principle. The program
will display the amount with the taxes taken out. Call the field the afterTax. Its captial gains at 15% which is
the current US tax rate. The program has two windows, with an image in each window. 
Author Rick Tobin
Version 1.0
date 7/20/2022
"""

# import all classes / functions from the tkinter

from tkinter import *
from PIL import ImageTk, Image
from math import *




"""#data verification
I tried to get this code to work, but it really interfered and i couldn't get it to work
So i couldn't get my security validation of the numbers to work. This is the remniets of the effort.
def callback(input):
    if input.isdigit():
        print(input)
        return True
                        
    elif input is "":
        print(input)
        return True

    else:
        print(input)
        return False"""
        

# Function for clearing the
# contents of all entry boxes
def clear_all() :

	# whole content of entry boxes is deleted
	principle_field.delete(0, END)
	rate_field.delete(0, END)
	time_field.delete(0, END)
	compound_field.delete(0, END)
	afterTax_field.delete(0,END)
	# set focus on the principle_field entry box
	principle_field.focus_set()


# Function from compound interest 
def calculate_ci():

	# get a content from entry box
	principle = int(principle_field.get())
	
	rate = float(rate_field.get())

	time = int(time_field.get())

	
	# This calculates compound interest 
	CI = principle * (pow((1 + rate / 100), time))
	# This calculates after taxes
	afterTax =  CI - (.15 * abs(principle - CI))

	# inserts the CI and After tax values into their fields and rounds them to the near 2 decimal point.
	CI= round(CI, 2)                        # This rounds CI
	afterTax= round(afterTax, 2)     #This rounds aftertax 
	compound_field.insert(10, CI)
	afterTax_field.insert(10,afterTax)
	

#Main first and second window code. 
if __name__ == "__main__" :

	# Create GUI windows
	fw = Tk()         #first window 
	sw = Toplevel()        # second window, make sure you used Toplevel() for the second window
                                                # Toplevel() works better with images, once i used Toplevel insted of Tk()
                                                #The images worked alot better. 

	# Set the background colour of GUI window
	fw.configure(background = 'dark green')
	sw.configure(background=  'dark green')

	# Set the configuration of GUI windows
	fw.geometry("500x400")
	sw.geometry("500x400")

	# set the name of tkinter GUI window
	fw.title("Compound Interest Calculator")
	sw.title("Results displayed")
	# Create a Principle Amount : label
	label1 = Label(fw, text = "Start Amount $",
				fg = 'black', bg = 'light grey')

	# Create a Rate : label
	label2 = Label(fw, text = "Interest Rate(%) : ",
				fg = 'black', bg = 'light grey')
	
	# Create a Time : label
	label3 = Label(fw, text = "Time(years) : ",
				fg = 'black', bg = 'light grey')

	# Create a Compound Interest : label
	label4 = Label(sw, text = "Compound Interest : ",
				fg = 'black', bg = 'light grey')
	#the after tax label, which subtracts 15% of the interest earned, but not the principal. 
	label5= Label(sw, text = "After Captial Gains tax: ",fg='black',bg='light grey')
                        
                  #Images 
	my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\rickt\\python\\dollar.jpg"))
	my_pic = ImageTk.PhotoImage(Image.open("C:\\Users\\rickt\\python\\dollarsign.jpg"))
	label6 =Label(fw, text="my 1st image", image=my_img)
	label7=Label(sw,text="my 2nd image", image = my_pic)
	
        
	
	#This sets up the lables in a grid like fashion. A table. 
	label1.grid(row = 1, column = 0, padx = 10, pady = 10)
	label2.grid(row = 2, column = 0, padx = 10, pady = 10)
	label3.grid(row = 3, column = 0, padx = 10, pady = 10)
	label4.grid(row = 5, column = 0, padx = 10, pady = 10)
	label5.grid(row=6, column = 0, padx =10, pady = 10)
	label6.grid(row=8, column =1, padx = 15, pady = 15)
	label7.grid(row=10, column = 1, padx = 10, pady = 10)

	# Create an input box
	# for filling or typing the information.
	principle_field = Entry(fw)
	rate_field = Entry(fw)
	time_field = Entry(fw)
	compound_field = Entry(sw)
	afterTax_field = Entry(sw)
	
	

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	
	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	principle_field.grid(row = 1, column = 1, padx = 10, pady = 10)
	rate_field.grid(row = 2, column = 1, padx = 10, pady = 10)
	time_field.grid(row = 3, column = 1, padx = 10, pady = 10)
	compound_field.grid(row = 5, column = 1, padx = 10, pady = 10)
	afterTax_field.grid(row =6, column = 1, padx =10, pady=10)

	

	# Create a Submit Button and attached
	# to calculate_ci function
	button1 = Button(fw, text = "Caclulate", bg = "light grey",
					fg = "black", command = calculate_ci)

	# Create a Clear Button and attached
	# to clear_all function
	button2 = Button(fw, text = "Clear", bg = "light grey",
					fg = "black", command = clear_all)
	button3= Button(sw, text = "Exit", bg = "light gray", fg = "black", command = exit)

	button1.grid(row = 4, column = 1, pady = 10)
	button2.grid(row = 5, column = 1, pady = 10)
	button3.grid(row= 7, column = 1, pady = 10)

# Start the GUI
fw.mainloop() #first window
sw.mainloop() #second window 
	
