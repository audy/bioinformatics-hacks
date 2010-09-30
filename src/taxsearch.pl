#!/usr/bin/env perl
#encoding: utf-8

my $help = "taxsearch.pl

Written by:
    David Crabb &
    Austin G. Davis-Richardson
    Eric Tripletts Group
    University of Florida

Usage:
    -t taxa keyword
    -c cutoff value (decimal)
    -d megablast query (.fasta)
    -m megablast results (.txt)
    -o name of output file
";

use strict;
use Getopt::Std;

my %args;
my %heads = ();
my $match = 0;

getopts('t:c:d:m:o:', \%args);

foreach my $key (keys %args) {unless ($args{$key}) { print $help; exit; } }

open(RESULTS, $args{'d'}) or die "can't open $args{'d'}";
open(QUERY, $args{'m'}) or die "can't open $args{'m'}";

open OUT, ">$args{o}" or die $!;

while (my $line = <QUERY>) {
	if (eval($line =~ /$args{t}/)) {
		my @columns = split(/\t/, $line);
		if ($columns[2] >= $args{c}) {
		    $heads{"$columns[0]"} =  "$columns[1]";

		}
	}
}

while (my $line = <RESULTS>) {
	if ($line =~ /^>/) {
		$match = 0;		
		chomp $line;
		chop $line;
		$line =~ s/^>//;
        if (exists $heads{$line}) {
            my $name = $heads{"$line"};
            print OUT ">$line|$name\n";
            $match = 1;
        }
    } 
    elsif ($match) { print OUT $line; }
}

print "meu trabalho é completa!\n";

foreach my $file (<OUT>, <RESULTS>, <QUERY>) { close $file; }