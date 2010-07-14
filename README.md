# BioHacks

[Austin Davis-Richardson](harekrishna@gmail.com)

[Artistic License 2.0](http://www.opensource.org/licenses/artistic-license-2.0.php)

A collection of Python scripts that I've had to write to solve little problems.  I decided to make them available so people can laugh at me.

## Scripts

* `get_taxids.rb`
  Gets Taxonomy IDs from NCBI using Bioruby gem (`sudo gem install bioruby`) and Hpricot gem (`sudo gem install hpricot`).  You might wanna edit the script to parse _your_ fasta file.

* `remdups.py <input.fastas>`
  Removes duplicate FASTA records

* `makeexontable.py <file.gff> <file.ffn>`
  My attempt to create an exon table used to train GlimmerHMM for Eukaryotic for gene prediction.  Gave up because GlimmerHMM doesn't work!

* `randomnames.py <input.fasta>`
  Replaces headers in a fasta file with a long string of random characters.  Useful for when programs like CLC Genomics Workbench replace your headers with `No Name` :\

* `fastqtools.py`
  Working on a script to generate statistics about quality score information, trim reads, pick `n` best quality reads, etc.

* `simgrab.py <fasta 1> <fasta 2>`
  Uses header from `fasta 1`, grabs record from `fasta 2` with same header.
  
* `random_fasta.py <input.fasta> <number>`
  Prints out random records from a given input file.

* `chim_gen.py <input.fasta> <number>`
  Generates chimeras from input fasta file.  Breakpoints are random.

* `truncate.py <input.fasta> <start> <end>`
  Truncates records in input fasta file.  You can use negative numbers to truncate from the right side.

* `stream_truncate.py <start> <end>`
  Same as truncate.py except that it truncates a sequence file from STDIN

* `zip.py`
  Concatenates records from two fasta files (assuming they are congruent).  Also assumes that sequences are on one line.

* `gc.py`
  %GC calculator.

* `quick_filter.py <input.fasta> <keyword>`
  Filters out records with keyword in the header.

* `silva_filter.py <inputfile>`
  Used to remove ambiguous nucleotides from RNA sequences, and then convert them to DNA.  I could have probably just used sed for this.

## Modules

`dna.py` and `fasta.py`
used by other scripts for iterating through fasta/q files:

    with open('reads.fastq') as handle:
        for record in Fasta(handle, 'fastq'):
            print record

Fasta is a fasta record *generator* that makes Dna objects:

    record = Dna('Seqa', 'GATCGATCGATC')
    print record.revcomp
    print record.qual

