#!/usr/bin/python3

from tkinter import *;
import tkinter;
import glob;
import re;
import os;


#function definition: ***launch()***
def launch():
	if var.get() == '/home/srm/klk/inv_spice':
		os.system("ngspice -b " + var.get());
	elif var.get() == '/home/srm/klk/cmd_ex1.py':
		os.system(str(var.get()) + " " + E1.get());
	else:
		os.system(var.get());
	#selection ="You selected the option " + str(var.get());
	#msg = messagebox.showinfo( "Hello Python", selection);


#function definition: ***entry()***
def entry(*args):
	#entry_list=[];
	sel=var.get();
		
	if sel == '/home/srm/klk/cmd_ex1.py':
		#L1=Label(root,text="Enter values:",font="Verdana 15 bold");
		L1.grid(rowspan=2,row=1,column=0);
		E1.grid(rowspan=2,row=1,column=1);
		E1.config(state=NORMAL);
		#entry_list.append(E1);
	else:
		try:
			L1.grid_forget();
			E1.grid_forget();
		except:
			pass;
	#print(entry_list);
	#return entry_list;


#Main Block:
if __name__ =="__main__":

	path = '/home/srm/klk/*';   
	files=glob.glob(path);

	root = Tk();
	root.title("File Selection and Run");
	root.geometry('600x300');

	var = StringVar(root);
	v=StringVar(root);

	label=Label(root, text="Select a file:",font="Verdana 20 bold",padx = 50,pady = 50);
	label.grid(row=0,column=0);
	var.set("None"); 

	file_list=[];
	for file in files:
		f=re.search(r'(/\w+/\w+.*)',file);
		if f:
			file_list.append(f.group());
	popupMenu=OptionMenu(root,var,'None',*file_list,command=entry());
	popupMenu.grid(row=0,column=1);
	
	L1 = Label(root,text="Enter Values:",font="Verdana 15 bold");
	E1 = Entry(root,textvariable=v,state='disabled');

	if var.get() != 'None':
		L1.config(state=NORMAL);
		L1.grid(rowspan=2,row=1,column=0);
		E1.config(state=NORMAL);
		E1.grid(rowspan=2,row=1,column=1);
	else:
		E1.grid_forget();


	button=Button(root, text = "Run",fg="white",activebackground="green",bg="green",width=10,command = launch());
	button.grid(row=3,column=0,padx=100, pady=60);
	
	button=Button(root, text = "Cancle",width=10,fg="white",activebackground="red",bg="red");
	button.grid(row=3,column=1,padx=100, pady=60);

	root.mainloop();
