#!/usr/bin/env ruby
# encoding: utf-8

require 'rubygems'
require 'Bio'
require 'hpricot'

# always tell NCBI who they're messing with
Bio::NCBI.default_email = "harekrishna@gmail.com"

if ARGV.length == 0
  $stdout.puts "usage #{__FILE__} fasta_file_with_accessions > output"
  exit
end

# Get accession numbers
records = []
File.open(ARGV.pop) do |handle|
  handle.each do |line|
    if line[0] == ">"
      id = line.split('|')[3]
      records << id
    end
  end
end
records.uniq!
puts records
# Query NCBI
ncbi = Bio::NCBI::REST.new

while records.length > 0
  query = records.pop 100
  retries = 5
  begin # get record
    rec = ncbi.efetch(query.join(','),
      {"db" => "nucleotide", "rettype" => "gb", "retmode" => "xml"})
  rescue SocketError # NCBI sometimes messes up
    if (retries -= 1) > 0
      retry
    else
      next
    end
  end
  
  # Parse XML reply
  doc = Hpricot::XML(rec)
  numb = query.pop
  
  # Do some weird obfuscated hpricot shit to get the taxid
  doc.search('GBSeq').each do |result|
    gi = result.search('GBSeq_accession-version>')
    result.search('GBQualifier_value').each do |h|
      if h.to_s.include? 'taxon:'
        a = h.to_s.split(':')
        a = a[1].split('</')
        id = a[0]
        
        # print to STDOUT
        puts '%s => %s' % [gi, id]
      end
    end
  end
end
