===========================
 Bioinformatics Quickhacks
===========================

Austin Davis-Richardson
harekrishna@gmail.com

 LICENSE
=========

GPL v3
Go to http://www.gnu.org/licenses/gpl-3.0-standalone.html

Oh, and these scripts are distributed with *ABSOLUTELY NO WARRANTY!*

 DESCRIPTION
=============

A collection of Python scripts that I've had to write to solve little problems.
I decided to make them available so people can laugh at me.

	*random_fasta.py <input.fasta> <number>*
	
	prints out random records from a given input file.


	*chim_gen.py <input.fasta> <number>*

	Generates chimeras from input fasta file.  Breakpoints are random.

	
	*truncate.py <input.fasta> <start> <end>*

	Truncates records in input fasta file.  You can use negative numbers
	to truncate from the right side.

	
	*quick_filter.py <input.fasta> <keyword>*

	Filters out records with keyword in the header.

	
	*dnaobj.py & fastitr.py*

	I was using these for FASTA iteration but not so much anymore.

	
	*silva_filter.py <inputfile>*

	Used to remove ambiguous nucleotides from RNA sequences, and then convert
	them to DNA.  I could have probably just used sed for this.