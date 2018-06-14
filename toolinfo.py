#!/usr/bin/python3
import argparse;
import re;

##This script is for finding Tool infomation

##function definition
def toolInfo(filename):
	#print(filename);
	tool_dict={};
	user_dict={};
	user_dict['user']={};
	names_list=[];
	tuser=0;
	toolname=' ';
	with open(filename,"r") as fobj:
		for line in fobj:
			line=line.strip();
			ttool=re.search(r'Users\s+of\s+(\w+):',line);
			tinfo=re.search(r'Users\s+of\s+(\w+):\s+\(Total\s+of\s+(\d+)\s+licenses\s+issued;\s+Total\s+of\s+(\d+)\s+\w+\s+in\s+use\)',line);
			lineflag=re.search(r'floating\s+license',line);
			uinfo=re.search(r'(\w+)\s+.*\s+start',line);
		
			if ttool is not None:
				if tinfo is not None:
					if int(tinfo.group(3)) > 0:
						tuser=1;
					else:
						tuser=0;
					
					toolname=tinfo.group(1);
					tool_dict[toolname]={'li issued': tinfo.group(2), 'li use': tinfo.group(3)};
					continue;
			elif uinfo is not None:
				names_list.append(uinfo.group(1));
				continue;	
			
			if tuser == 1:
				usernames={};
				for un in names_list:
					#print(names_list);
					if un in usernames.keys():
						usernames[un] = usernames[un] + 1;
					else:
						usernames[un] = 1;
					#for k,v in usernames.items():
						#print(k,v);
					user_dict['user'][toolname]=usernames;
					#print(user_dict);
			names_list=[];
	
	user_dict['tool']=tool_dict;
	
	return user_dict;	
##end function


if __name__=="__main__":
	parser=argparse.ArgumentParser(description='Passing file name and finding tool & user infomation');
	parser.add_argument('-filename', '-file', dest='file', help='Enter filename');
	parser.add_argument('-username', '-user', dest='user', help='Enter username');
	args=parser.parse_args();
	#print(args);	

	tool_dict={};
	
	if args.user is not None:
		tool_dict=toolInfo(args.file);   ##function call
		#print(tool_dict);		

		print("\n");
		print("******User details******");
		print("User Name:", args.user);
		print("------------------------------------------");
		print("Tool name\t\t No.of licenses");
		print("------------------------------------------");
		for key,value in tool_dict.items():
			#print(key);
			for k,v in tool_dict[key].items():
				#print(k,v);
				for uk,uv in tool_dict[key][k].items():
					if uk == args.user:
						print("{} \t\t {}".format(k,uv));
		print("------------------------------------------");	
	elif args.file is not None:
		tool_dict=toolInfo(args.file);    ##function call
		#print(tool_dict);
	
		print("\n");
		print("******Tool Details******");
		for dk,dv in tool_dict.items():
			if dk == 'tool':
				for key,value in tool_dict[dk].items():
					#print(key);
					print("Tool Name:", key);
					print("No.of licenses issued:", tool_dict['tool'][key]['li issued']);
					print("No.of licenses in use:", tool_dict['tool'][key]['li use']);
					print("---------------------------------");
					print("User Name\t No.of Licenses");
					print("---------------------------------");
					for uk,uv in tool_dict.items():
						#print(uk,uv);
						if uk == 'user':
							for tuk,tuv in tool_dict[uk].items():
								if tuk == key:
									for k,v in tool_dict[uk][tuk].items():
										print("{}     \t {}".format(k,v));
					print("----------------------------------");	
