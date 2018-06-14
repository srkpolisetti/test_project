#!/usr/bin/python3

import sys;
import argparse;
import random;

##This script is for predecting toss between "Lengaburu" and "Enchai" teams

#function definition: ***toss_result()***
def toss_result(): 
	teams=['lengaburu','enchai'];
	for team in teams:
		if (team == "lengaburu") :
			if (weather == "clear") & (match_type == "day"):
				print("#1-Lengaburu wins toss and Bats");
			elif (weather == "cloudy") & (match_type == "night"):
				print("#1-Lengaburu wins toss and Bowls");
			else:
				print("#1-Lengaburu wins toss and Bats");
		else:
			if (weather == "clear") & (match_type == "day"): 
				print("#2-Enchai wins toss and Bowls"); 
			elif (weather == "cloudy") & (match_type == "night"):
				print("#2-Enchai wins toss and Bats");
			else:   
				print("#2-Enchai wins toss and Bats"); 


#Main method
if __name__=="__main__":
	
	#for help message
	parser=argparse.ArgumentParser(description="This script is for predecting toss based on conditions");
	parser.add_argument("weather",help='Enter weather(clear/cloudy) as first argument in command line (lower case)');
	parser.add_argument("match_type",help='Enter match_type(day/night) as second argument in command line (lower case)');
	args = parser.parse_args()

	weather=sys.argv[1];
	match_type=sys.argv[2];
	
	coin_flip=1;

	for coin in range(coin_flip):
		flip=random.randint(1,2);
		if flip == 1:
			#function call
			toss_result();
		else:
			#function call
			toss_result();
