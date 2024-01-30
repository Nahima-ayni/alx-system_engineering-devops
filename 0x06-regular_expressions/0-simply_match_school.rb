#!/usr/bin/env ruby

word = ARGV[0]

regex = /School/
if word =~ regex
  puts "School"
else
  puts ""
end
