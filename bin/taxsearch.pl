#!/usr/bin/env perl
#encoding: utf-8

my $help = "taxsearch.pl

Written by:
    David Crabb &
    Austin G. Davis-Richardson
    Eric Tripletts Group
    University of Florida

Usage:
    -t keywords file
    -c cutoff value (percentage)
    -d megablast query (.fasta)
    -m megablast results (.txt)
    -o name of output file
";

use strict;
use Getopt::Std;
use IO::File;

# GET OPTIONS
my %args;
getopts('t:c:d:m:o:',\%args);
if (keys %args == 0) { print $help; exit; }
foreach my $key (keys %args) { unless ($args{$key}) { print $help; exit; } }

# OPEN FILES
open(FASTA, $args{'d'}) or die "Can't open $args{'d'}!";
open(MEGABLAST, $args{'m'}) or die "Can't open $args{'m'}!";
open(KEYWORDS, $args{'t'}) or die "Can't open $args{'t'}!";

# READ KEYWORDS; MAKE OUTPUT HANDLES
my %keywords;
while (my $line = <KEYWORDS>) {
  chomp $line;
  $line =~ s/\///;
  my $handle = IO::File->new;
  $handle->open(">$line.fas") or die "Can't open $line!";
  $keywords{"$line"} = $handle;
}

# MEGABLAST LOOP
my %good_records;
my @keys = keys %keywords;
while (my $line = <MEGABLAST>) {
  my @columns = split(/\t/, $line);
  foreach my $key (@keys) {
    if (("$columns[1]" =~ /\Q$key\E/) and ($columns[2] >= $args{c})) {
      $good_records{"$columns[0]"} = "$columns[1]";
    }
  }
}

# FASTA LOOP; PRINT TABLES
my $match = 0;
my $handle;
while (my $line = <FASTA>) {
  if ($line =~ /^>/) {
    $match = 0;
    chop $line;
    chomp $line;
    $line =~ s/ //;
    $line =~ s/^>//;
    if (exists $good_records{"$line"}) {
      my $name = $good_records{"$line"};
      $handle = $keywords{"$line"};
      print $handle ">$line|$name\n";
      $match = 1;
    }
    elsif ($match) { print $handle $line; }
  }
}

# CLOSE FILES
print "meu trabalho é completo!\n";
foreach my $file (<MEGABLAST>, <FASTA>, <KEYWORDS>) { close $file; }