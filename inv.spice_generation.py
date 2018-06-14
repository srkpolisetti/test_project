#!/usr/bin/python3
import argparse;
import os;
import re;
import glob;

#This script is for generating net list(inverter) by reading 'i/p transition' and 'o/p capacitance' from "input_values" file.
#Generating and saving combination of files by simulating ngspice based on the net list(inverter).
#Storing measurements from net list(inverter) into a dictonary.


##function definition: ***net_list_generation()***
def net_list_generation(x,y):
	"This is function is for generating netlist file for accessing arguments passed from function call"
	net_list="*inverter net list\n\n \
*** Model Statements ***\n \
.model MOSN NMOS level=8 version=3.3.0\n \
.model MOSP PMOS level=8 version=3.3.0 \n\n \
*** DECLARE POWER HV VOLTAGES *** \n \
.param HV=5V \n \
.param LV=0V \n \
.param TR=" + x + "\n \
.param TF=" + x + " \n \
.param CL=" + y + "\n\n \
M1 1 2 3 3 MOSP L=0.18u W=0.72u\n \
M2 1 2 0 0 MOSN L=0.18u W=0.36u\n\n \
*** input sources ***\n \
VDD 3 0 DC 'HV'\n \
VG 2 0 pulse('LV' 'HV' 0ns 'TR' 'TF' 20ns 40ns)\n\n \
*** analysis type ***\n \
.tran 1ns 100ns 5ns\n \
*** DEFINE CAPACITANCE ***\n \
COUT 1 0 'CL'\n\n \
.measure tran tpdr TRIG v(2) VAL='HV/2' FALL=1 TARG v(1) VAL = 'HV/2' RISE=1\n \
.measure tran tpdf TRIG v(2) VAL='HV/2' RISE=1 TARG v(1) VAL = 'HV/2' FALL=1\n \
*.measure tran tpd  param='(tpdr+tpdf)/2'\n \
*trise\n \
.measure tran trise TRIG  v(1) VAL='0.2*HV' RISE=1 TARG v(1) VAL = '0.8*HV' RISE=1\n \
*tfall\n \
.measure tran tfall TRIG  v(1) VAL='0.8*HV' FALL=1 TARG v(1) VAL = '0.2*HV' FALL=1\n\n \
*** POWER CALCULATION ***\n \
.measure tran iavg AVG i(VDD) FROM=0ns TO=40ns\n \
.measure tran power PARAM='iavg*5'\n \
*.control \n \
*run\n \
*plot v(2)\n \
*plot v(1)\n \
*.endc\n \
.end";
	return net_list;


#function definition: ***cell_char_values()***
def cell_char_values():
	cell_char={};
	cell_char['inv']={};
	cell={};
	cell_list=[];
	file_key=' ';
	decimal_text=' ';
	decimal_value=0.0;
	file_name=glob.glob('/home/srm/inv_values/*');
	for file in file_name:
		file=re.search(r'/home/srm/inv_values/(\w+\d+\.\d+\w+\d+\.\d+\w+)',file);
		#print(file.group(1));
		file_key=file.group(1);
		with open(file.group(),"r") as fobj:
			cell_list=[];
			for line in fobj:
				cval_pos=re.search(r'(\w+)\s+\=\s+(\d+\.\d+\w+-\d+)\s+targ',line);
				cval_neg=re.search(r'(\w+)\s+\=\s+(-\d+\.\d+\w+-\d+)\s+targ',line);
				if cval_pos is not None:
					#print(cval_pos.group(1),cval_pos.group(2));
					decimal_text=cval_pos.group(1);
					decimal_value=("%.16f" % float(cval_pos.group(2)));
					cell_list.append({decimal_text : decimal_value});
					cell[file_key]=cell_list;
					cell_char['inv']=cell;
				elif cval_neg is not None:
					#print(neg_pos.group(1),neg_pos.group(2));
					decimal_text=cval_neg.group(1);
					decimal_value=("%.16f" % float(cval_neg.group(2)));
					cell_list.append({decimal_text : decimal_value});
					cell[file_key]=cell_list;
					cell_char['inv']=cell;      
	print(cell_char);



if __name__=="__main__":
	parser=argparse.ArgumentParser(description='This file is for reading "input_values" file and generating net list files');
	args=parser.parse_args();
	
  #Reading "input_values" file
	ip_list=[];
	com_list=[];
	ic_dict={};
	index_name='';
	x=' ';y=' ';
	with open("input_values","r") as fobj:
		for line in fobj:
			ip_list.extend(line.split());
			for ele in ip_list:
				index_ele1=re.search(r'i/p_transistion:',ele);
				index_ele2=re.search(r'o/p_capacitance:',ele);
				search_ele=re.search(r'(\d+.\d+\w+)',ele);
				if index_ele1:
					index_name=index_ele1.group();
				elif index_ele2:
					index_name=index_ele2.group();
				elif search_ele:
					com_list.append(search_ele.group());
			#print(com_list);
			ic_dict[index_name]=com_list;
			com_list=[];
			ip_list=[];
  #print(ic_dict);
  
	a=0;
	file_list=[]; 
	#dictonary elements
	for k,v in ic_dict.items():
		#print(k,v);
		if k == 'i/p_transistion:':
			for v1 in ic_dict[k]:
				x=v1;
				#print('x:',x);
				for k1,v1 in ic_dict.items():
					if k1 == 'o/p_capacitance:':
						for v2 in ic_dict[k1]:
							y=v2;
							a+=1;
							print("***Combination:" + str(a));
							print('x:',x);
							print('y:',y);
							print("###############################");
							file_name="values_"+ x +"_"+ y;
							
							#function call: ****net_list_generation****
							net_list=net_list_generation(x,y);	
							#print(net_list);

							with open("inv.txt","w") as wobj:
								wobj.truncate();
								wobj.write(net_list);
								#wobj.write('\n');
							#print(file_name);
							#os.system("ngspice -b inv.txt");
	
	print("#########################################");
	print("\n***Cell Characterization Measurements*** \n");
	print("#########################################");
	#function call: ***cell_char_values()***
	cell_char_values();

