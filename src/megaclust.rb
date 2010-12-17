#!/usr/bin/env ruby

usage = <<-eos
megaclust.rb -> converts CLC assembly data
  into a megaclust-looking table for use as
  input with David Crabb's megaclusttable.pl
  
usage: ruby megaclust.rb rdp_database clc_outputfile > output.csv
eos

if ARGV.length != 2
  puts usage
  exit -1
end

rdp, clc = ARGV.last 2
f, c = File.new(rdp), 1
rdp = Hash.new{  }

while entry = f.gets("\n>") do
  break if entry.nil?
  res = entry.sub!(/^\s|^>/, "").split("\n").first
  rdp[c] = { :entry => res, :count => 1 }
  c += 1
end

f = File.new(clc)

f.each do |line|
  n = line.split[6].to_i
  if !rdp[n].nil?
    rdp[n][:count] += 1
  end
end

rdp.keys.each do |c|
  puts "#{rdp[c][:entry]},#{rdp[c][:count]}"
end