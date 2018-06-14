#!/usr/bin/python3

import sys;
import argparse;

#function definition: ***lengaburu()***
def lengaburu(weather,match,toss_result):
	if (toss_result == "head") | (toss_result == "tail"):
		if ((weather == "clear") & (match == "day") & (toss_result == "head") | (weather == "clear") & (match == "day") & (toss_result == "tail")):
			print("Lengaburu wins toss and Bats");
		elif ((weather == "cloudy") & (match == "night") & (toss_result == "head") | (weather == "cloudy") & (match == "night") & (toss_result == "tail")):
			print("Lengaburu wins toss and Bowls");
		else:
			print("Lengaburu wins toss and Bats");


#functon definition: ***enchai()***
def enchai(weather,match,toss_result):
	if (toss_result == "head") | (toss_result == "tail"):
		if ((weather == "clear") & (match == "day") & (toss_result == "head") | (weather == "clear") & (match == "day") & (toss_result == "tail")):
			print("Enchai wins toss and Bowls");
		elif ((weather == "cloudy") & (match == "night") & (toss_result == "head") | (weather == "cloudy") & (match == "night") & (toss_result == "tail")):
			print("Enchai wins toss and Bats");
		else:
			print("Enchai wins toss and Bats");


#Main method
if __name__=="__main__":
	
	#for help message
	parser=argparse.ArgumentParser(description="This script is for predecting toss based on conditions");
	parser.add_argument("Toss",help='Enter weather(clear/cloudy) and match_type(day/night) as arguments in command line(lower case)');
	parser.add_argument("Example",help='(./the_toss clear day); [Enter toss chooser team: enchai]; [Enter toss choice: head]; [Enter toss result: head]');
	args = parser.parse_args()


	weather=sys.argv[1];
	match=sys.argv[2];
	#print(weather,match);
	toss_sel_team=input("Enter toss chooser team(lengaburu/enchai): ");
	toss_choose_by=input("Enter toss choice(head/tail): ");
	toss_result=input("Enter toss result(head/tail): ");
	
	if ((toss_sel_team == "lengaburu") & (toss_choose_by == "head") & (toss_result == "head")) | ((toss_sel_team == "lengaburu") & (toss_choose_by == "tail") & (toss_result == "tail")):
		lengaburu(weather,match,toss_result);
	elif ((toss_sel_team == "lengaburu") & (toss_choose_by == "head") & (toss_result == "tail")) | ((toss_sel_team == "lengaburu") & (toss_choose_by == "tail") & (toss_result == "head")):
		enchai(weather,match,toss_result);
	elif ((toss_sel_team == "enchai") & (toss_choose_by == "head") & (toss_result == "head")) | ((toss_sel_team == "enchai") & (toss_choose_by == "tail") & (toss_result == "tail")):
		enchai(weather,match,toss_result);
	elif ((toss_sel_team == "enchai") & (toss_choose_by == "head") & (toss_result == "tail")) | ((toss_sel_team == "enchai") & (toss_choose_by == "tail") & (toss_result == "head")):
		lengaburu(weather,match,toss_result);
