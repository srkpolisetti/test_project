#!/usr/bin/perl

##coverage report of reference and base file's using functions

##accessing "reference" & "base" files from command line
$reference=@ARGV[0];
$base=@ARGV[1];

##calling coverageReport function with passing "reference" file
$rhash_ref=coverageReport($reference);

##calling coverageReport function with passing "base" file
$bhash_ref=coverageReport($base);


##fetching refhash sum values
$rc1sum=$rhash_ref->{'coverage1'}->{'csum'};
$rc2sum=$rhash_ref->{'coverage2'}->{'csum'};
#print "$rc1sum => $rc2sum\n";

##fetching refhash len values
$rc1len=$rhash_ref->{'coverage1'}->{'clen'};
$rc2len=$rhash_ref->{'coverage2'}->{'clen'};

##fetching basehash sum values
$bc1sum=$bhash_ref->{'coverage1'}->{'csum'};
$bc2sum=$bhash_ref->{'coverage2'}->{'csum'};
#print "$bc1sum => $bc2sum\n";

##fetching basehash len values
$bc1len=$bhash_ref->{'coverage1'}->{'clen'};
$bc2len=$bhash_ref->{'coverage2'}->{'clen'};

##finding Average's of reference
$ravgc1=$rc1sum/$rc1len;
$ravgc2=$rc2sum/$rc2len;

#print "$ravgc1 - $ravgc2\n";
#print "Average of ref cov1: $ravgc1\n";
#print "Average of ref cov2: $ravgc2\n";

##finding Averages's of base
$bavgc1=$bc1sum/$bc1len;
$bavgc2=$bc2sum/$bc2len;

#print "$bavgc1 - $bavgc2\n";
#print "Average of base cov1: $bavgc1\n";
#print "Average of base cov2: $bavgc2\n";

##finding difference between "reference" and "base"
$cov1diff=(($ravgc1-$bavgc1)/$ravgc1)*100;
$cov2diff=(($ravgc2-$bavgc2)/$ravgc2)*100;

#print "coverage1 % diff:$cov1diff\n";
#print "coverage2 % diff:$cov2diff\n\n";

##displaying "Coverage Report"
print "\n";
print "*************Coverage Report************\n";
print "----------------------------------------------------------------------------\n";
print " Design\t\t  Reference_Avg\t  Base_Avg\t  %Difference\n";
print "----------------------------------------------------------------------------\n";
print " Coverage1\t  $ravgc1\t\t  $bavgc1\t\t  $cov1diff\n";
print " Coverage2\t  $ravgc2\t\t  $bavgc2\t\t  $cov2diff\n";
print "---------------------------------------------------------------------------\n";
print "\n";


##function definition
sub coverageReport {
	$file_name=shift;
	
	##opening a file
	open(IN,"$file_name") || die "not able to open '$file_name' file\n";	
	$rbdesign;
	$rbfopen=0;
	@rbwords=();
	$rbhash_ref={};
	while($lines=<IN>){
		if($lines =~ /(\w+)\s+(\{)/) {
			$rbdesign=$1;
			$rbfopen=1;
			next;
		}
		elsif($lines =~ /\}/) {
			$rbfopen=0;
			$rbsum=0;
			$rblen=0;
			foreach $w (@rbwords) {
				$rbsum=$rbsum+$w;
				if($w =~ /\s*\d+.\d+/){
					$rblen=$rblen+1;
				} ##end if
			} ##end foreach
			$rbhash_ref->{$rbdesign}->{'csum'}=$rbsum;
			$rbhash_ref->{$rbdesign}->{'clen'}=$rblen;
			@rbwords=();
			next;
		} ##end if
		if($rbfopen == 1){
			push(@rbwords,split(/\s+/,$lines));
		} ##end if
	} ##end while
  
	##closing a file
	close(IN);
	
	return $rbhash_ref;
} ##end function

