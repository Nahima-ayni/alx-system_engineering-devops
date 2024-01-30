#!/usr/bin/env ruby

require 'oniguruma'

word = ARGV[0]
regex = /School/
if word =~ regex
  puts "School"
else
  puts ""
end
