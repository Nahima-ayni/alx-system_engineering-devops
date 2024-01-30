#!/usr/bin/env ruby

word = ARGV[0]

regex = /School/
if regex.match(word)
  puts "School"
else
  puts ""
end
