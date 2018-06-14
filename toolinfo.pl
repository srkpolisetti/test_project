#!/usr/bin/perl

use strict;
use warnings;
use Getopt::Long;

##This script is for finding Tool information and User information based on passed file in comm line


my $file_name;
my $user_name;
my $help;
GetOptions("filename|file=s" => \$file_name, "username|user=s" => \$user_name, "help|h" => \$help) or die("Error in comm line args\n");

my $tool_user={};

if(defined($help)) {
 ##function call
 &help();
} ##end if

if(defined($file_name) & defined($user_name)) {
	##function call
	$tool_user=&toolInfo($file_name); 
		
	print "\n";
	print "*****User details*****\n";
	print "User Name: $user_name\n";
	print "------------------------------------------\n";
	print "Tool name\t\t No.of licenses\n";
	print "------------------------------------------\n";

	while((my $key, my $value) = each(%{$tool_user})) {
		#print "$key,$value\n";
		#print "$tool_user->{'user'}\n";
		while((my $k, my $v) = each(%{$tool_user->{$key}})) {
		#	print "$k => $v\n";
			while((my $uk,my $uv) =each(%{$tool_user->{$key}->{$k}})) {
				#	print "$uk,$uv\n";
				if($uk eq $user_name) {
					print "$k \t\t $uv\n";
				} ##end if
			} ##end while
		} ##end while
	} ##end while
	print "------------------------------------------\n";
}
elsif(defined($file_name)) {	
	##function call
	$tool_user=&toolInfo($file_name);
	while((my $k, my $v) = each(%{$tool_user->{'user'}})) {
		while((my $a,my $b) = each(%{$tool_user->{'user'}->{$k}})) {
			#print "hash: $a => $b\n";
		}
	}

	print "\n";
	print "*****Tool Details*****\n";
	while((my $hk,my $hv) = each(%{$tool_user})) {
		if($hk eq 'tool') {
			while((my $key,my $value) = each(%{$tool_user->{$hk}})) {
				print "Tool Name: $key\n";
				print "No.of licenses issued: $tool_user->{'tool'}->{$key}->{'li issued'}\n"; 		
				print "No.of licenses in use: $tool_user->{'tool'}->{$key}->{'li use'}\n";
				print "--------------------------------\n";
				print "User Name\t No.of Licenses\n";
				print "--------------------------------\n";
				while((my $uk,my $uv) = each(%{$tool_user->{'user'}})) {
					#print "$uk => $uv\n";
					if($uk eq $key) {
						#print "$uk => $uv\n";	
						#print "$tool_user->{'user'}->{'XT_XCC_TIE'}->{'sdandu'}\n";
						while((my $k,my $v) =each(%{$tool_user->{'user'}->{$uk}})) {
							print "$k     \t $v\n";					
						} ##end while
					} ##end if
				} ##end while
				print "-------------------------------------\n";
			} ##end while
		} ##end if
	} ##end while
}	##end if



##function definition:-toolInfo-
sub toolInfo {
	$file_name=shift;
	
	##opening a file
	my $tool_info={};
	my @usernames=();
	my $tuser=0;
	my $toolname=' ';
	my $tool_user->{'user'}={};
	open(IN,"$file_name") || die "file not found\n";

	while(my $lines=<IN>) {
		if($lines =~ /Users\s+of\s+(\w+):/) {
			if($lines =~ /Users\s+of\s+(\w+):\s+\(Total\s+of\s+(\d+)\s+licenses\s+issued;\s+Total\s+of\s+(\d+)\s+\w+\s+in\s+use\)/) {
     		if($3 > 0) {
					$tuser=1;
				}

				$toolname=$1;
				$tool_info->{$toolname}={'li issued' => $2, 'li use' => $3};
				next;
			} ##end if 
		} ##end if
		elsif($lines =~ /(\w+)\s+.*\s+start/) {
			#print "user_name: $1\n";
			push(@usernames,$1);
			next;
		} ##end if

		if($tuser == 1){
				my %username=();
				foreach my $k (@usernames) {
					if($k eq (keys %username)) {
			 			$username{$k} += 1;
					}
					else{
						$username{$k} = 1;
					}
				} ##end foreach
				foreach my $uk (keys %username) {
				#	print "check hash: $uk => $username{$uk}\n";
				} ##end foreach
			
				$tool_user->{'user'}->{$toolname}=\%username;
		} ##end if
		@usernames=();
 	} ##end while	

  ##closing file
	close(IN);
	
	$tool_user->{'tool'}=$tool_info;
 	
	return $tool_user;
} ##end function


##function definition: -help-
sub help {
	print "$0 => This scriptis used to find infomation of tools,licenses used & finding user info\n";
	print "filename|file <Enter file name> username|user <Enter user name>  <mandatory>
				help|h <print script usage options>
				Ex: $0 -file file1.txt -user user1\n";
} ##end function
