#!/usr/bin/perl

##coverage report for reference and base file

##opening "reference" file
open(IN,"reference") || die "no such a file\n";
$refdesign;
$rfopen=0;
@refwords=();
%refhash=();
%rlenhash=();
while($line =<IN>){
	if($line =~ /(\w+)\s+(\{+)/) {
		#print "coverage:$1\n";
		$refdesign=$1;
		$rfopen=1;
		next;
	}
	elsif($line =~ /\}/){
		$rfopen=0;
		#print "@refwords\n";
		$sum=0;
		$len=0;
		foreach $v (@refwords){
			$sum=$sum+$v;
			if($v =~ /\s*\d+.\d+/){
				$len=$len+1;
			} ##end if
		} ##end foreach
		$refhash{$refdesign}=$sum;
		$rlenhash{$refdesign}=$len;
		@refwords=();
		next;	
	} ##end if
	if($rfopen == 1){
		push(@refwords,split(/\s+/,$line));
	}
} ##end while

##closing "reference" file
close(IN);

##fetching refhash values
$refc1sum=$refhash{'coverage1'};
$refc2sum=$refhash{'coverage2'};

##fetching rlenhash values
$refc1len=$rlenhash{'coverage1'};
$refc2len=$rlenhash{'coverage2'};

#print "len of cov1: $refc1len\n";
#print "len of cov2: $refc2len\n";

#print "ref file coverage1 sum: $refc1sum\n";
#print "ref file coverage2 sum: $refc2sum\n";

##opening "base" file
open(IN,"base") || die "no such a file\n";
$bdesign;
$bfopen=0;
@basewords=();
%basehash=();
%blenhash=();
while($line=<IN>){
	if($line =~ /(\w+)\s+(\{+)/) {
		#print "coverage:$1\n";
		$bdesign=$1;
		$bfopen=1;
		next;
	}
	elsif($line =~ /\}/) {
		$bfopen=0;
		#print "@basewords\n";
		$sum=0;
		$len=0;
		foreach $v (@basewords){
			$sum=$sum+$v;
			if($v =~ /\s*\d+.\d+/){
				$len=$len+1;
			}
		} ##end foreach
		$basehash{$bdesign}=$sum;
		$blenhash{$bdesign}=$len;
		@basewords=();
		next;
	} ##end if
	if($bfopen == 1){
		push(@basewords,split(/\s+/,$line));	
	}
} ##end while

##closing "base" file
close(IN);

##fetching basehash values
$bc1sum=$basehash{'coverage1'};
$bc2sum=$basehash{'coverage2'};

##fetching blenhash values
$basec1len=$blenhash{'coverage1'};
$basec2len=$blenhash{'coverage2'};
#print "base cov1 len: $basec1len\n";
#print "base cov2 len: $basec2len\n";


#print "base file coverage1 sum: $bc1sum\n";
#print "base file coverage2 sum: $bc2sum\n"; 

##finding ref file Average's
$refc1avg=$refc1sum/$refc1len;
$refc2avg=$refc2sum/$refc2len;

##finding base file Average's
$bc1avg=$bc1sum/$basec1len;
$bc2avg=$bc2sum/$basec2len;

#print "Average of ref and base cov1: $rbavgc1\n";
#print "Average of ref and base cov2: $rbavgc2\n";

##finding difference between "reference" and "base"
$cov1diff=(($refc1avg-$bc1avg)/$refc1avg)*100;
$cov2diff=(($refc2avg-$bc2avg)/$refc2avg)*100;

#print "coverage1 % diff:$cov1diff\n"; 
#print "coverage2 % diff:$cov2diff\n\n";


##displaying "Coverage Report" 
print "\n";
print "*************Coverage Report************\n";
print "---------------------------------------------------------------------------\n";
print "Design\t\t Reference\t Base\t\t  %Difference\n";
print "---------------------------------------------------------------------------\n";
print "Coverage1\t $refc1avg\t\t $bc1avg\t\t  $cov1diff\n";
print "Coverage2\t $refc2avg\t\t $bc2avg\t\t  $cov2diff\n";
print "\n";

