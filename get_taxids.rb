#!/usr/bin/env ruby
# encoding: utf-8

require 'rubygems'
require 'Bio'
require 'hpricot'

# always tell NCBI who you are
Bio::NCBI.default_email = "harekrishna@gmail.com"

ncbi = Bio::NCBI::REST.new
file = File.new('how.fa', 'r')
records = []

file.each do |line|
  if line.include? '>'
    id = line.split(' | ')[-3]
    records << id
  end
end

records.each do |record|
  rec = ncbi.efetch(record, {"db"=>"nucleotide", "rettype"=>"gb", "retmode"=>"xml"})
  doc = Hpricot::XML(rec)
  doc.search('GBQualifier_value').each do |h|
    if h.to_s.include? 'taxon:'
      a = h.to_s.split(':')
      a = a[1].split('</')
      id = a[0]
      puts '%s => %s' % [record, id]
    end
  end
end