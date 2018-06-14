#!/usr/bin/python3

import os;
import re;

if __name__ == "__main__":
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
							print("\n");
							with open("inv.spice","r") as iobj:
								for line in iobj:
									line=line.strip();
									if line == '.param TR=':
										line = line + x;
									elif line == '.param TF=':
										line = line + x;
									elif line == '.param CL=':
										line = line + y;
									file_list.append(line);
							#print(file_list);
						
							with open("inv.txt","w") as wobj:
								wobj.truncate();
								for l in file_list:
									#print(l);
									wobj.write(l);
									wobj.write('\n');
							file_list=[];		
							os.system('ngspice -b inv.txt');
