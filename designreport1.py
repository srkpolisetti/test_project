#!/usr/bin/python3

import sys;
import re;

##coverage report of "reference" and "base" file using functions


##defining function
def coverageReport(file_name):
	"This function reads the passed file and returns the dictionary"
	with open(file_name,"r") as fobj:
		design=' ';
		rbfopen=0;
		rbwords=[];
		dict={};
		for line in fobj:
			line=line.strip();
			rbopen=re.search(r'(\w+)\s+(\{)',line);
			rbclose=re.search(r'\}',line);	
			if rbopen is not None:	
				design=rbopen.group(1);
				rbfopen=1;
				continue;
			elif rbclose is not None:	
				rbfopen=0;
				sum=0;
				len=0;
				for w in rbwords:
					sum=sum+float(w);
					len=len+1;
				dict[design]={'sum':sum,'len':len};
				rbwords=[];
				continue;
			if rbfopen == 1:
				rbwords.extend(line.split(" "));
	return dict;
##end function

##fetching comm line arguments
reference_file=sys.argv[1];
base_file=sys.argv[2];

##function call by passing "reference" file
dict_ref=coverageReport(reference_file);
#print("reference file:",dict_ref);

##function call by passing "base" file
dict_base=coverageReport(base_file);
#print("base file:",dict_base);

##finding Average's of "reference"
refc1avg=dict_ref['coverage1']['sum']/dict_ref['coverage1']['len'];
refc2avg=dict_ref['coverage2']['sum']/dict_ref['coverage2']['len'];

##finding Average's of "base"
basec1avg=dict_base['coverage1']['sum']/dict_base['coverage1']['len'];
basec2avg=dict_base['coverage2']['sum']/dict_base['coverage2']['len'];


##finding %difference between "reference" and "base"
cov1diff=((refc1avg-basec1avg)/refc1avg)*100;
cov2diff=((refc2avg-basec2avg)/refc2avg)*100;


##displaying "Coverage Report"
print("\n"); 
print("*************Coverage Report************");
print("----------------------------------------------------------------------------");
print(" Design\t\t Reference_Avg\t Base_Avg\t%Difference");
print("----------------------------------------------------------------------------");
print(" Coverage1\t {}\t\t {}\t\t{}".format(refc1avg,basec1avg,cov1diff)); 
print(" Coverage2\t {}\t\t {}\t\t{}".format(refc2avg,basec2avg,cov2diff));
print("----------------------------------------------------------------------------");
#print("\n");
