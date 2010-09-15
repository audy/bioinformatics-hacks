#!/usr/bin/env ruby
# encoding: utf-8

require 'rubygems'
require 'Bio'
require 'hpricot'

# always tell NCBI who you are
Bio::NCBI.default_email = "harekrishna@gmail.com"

ncbi = Bio::NCBI::REST.new
file = File.new(ARGV.pop, 'r')
records = []

file.each do |line|
  if line.include? '>'
    id = line.split('|')[3]
    records << id
  end
end

records.uniq!

while records.length > 0
  query = records.pop(30)
  retries = 5
  begin
    rec = ncbi.efetch(query.join(','), {"db"=>"nucleotide", "rettype"=>"gb", "retmode"=>"xml"})
  rescue SocketError
    if (retries -= 1) > 0
      retry
    else
      next
    end
  end
  doc = Hpricot::XML(rec)
  numb = query.pop
  
  doc.search('GBSeq').each do |result|
    gi = result.search('GBSeq_accession-version>')
    result.search('GBQualifier_value').each do |h|
      if h.to_s.include? 'taxon:'
        a = h.to_s.split(':')
        a = a[1].split('</')
        id = a[0]
        puts '%s => %s' % [gi, id]
      end
    end
  end
end