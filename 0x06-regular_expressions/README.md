# Regular Expressions in Ruby

Regular expressions (regex or regexp) in Ruby are powerful tools for pattern matching and manipulation of strings. Ruby's built-in support for regular expressions makes it easy to perform complex string operations efficiently.

## Syntax

Regular expressions in Ruby are represented by literals between forward slashes (`/.../`) or using the `Regexp.new` constructor. Here are some common components of regular expressions:

- **Literal Characters**: Match exact characters.
- **Character Classes**: Match sets of characters.
- **Anchors**: Specify positions in the string (start, end, word boundaries).
- **Quantifiers**: Indicate how many times a character or group should repeat.
- **Alternation**: Match one pattern or another.
- **Grouping and Capturing**: Group parts of a pattern and capture matched substrings.
- **Modifiers**: Affect matching behavior (case sensitivity, multiline mode, etc.).
- **Escaping**: Use backslash (`\`) to escape special characters.

## Basic Examples

### Matching

- `/pattern/` - Matches the pattern.
- `=~` - Matches a string against a regular expression.
  
```ruby
"hello" =~ /hello/   # Returns 0 (match at index 0)
```

### Anchors

- `^` - Matches the start of a line.
- `$` - Matches the end of a line.

```ruby
/^hello/ =~ "hello world"   # Returns 0 (matches at the start)
/world$/ =~ "hello world"   # Returns 6 (matches at the end)
```

### Character Classes

- `[...]` - Matches any single character within the brackets.
- `[^...]` - Matches any single character not within the brackets.

```ruby
/[aeiou]/ =~ "hello"    # Matches any vowel
/[^0-9]/ =~ "abc123"    # Matches any non-digit character
```

### Quantifiers

- `*` - Matches zero or more occurrences.
- `+` - Matches one or more occurrences.
- `?` - Matches zero or one occurrence.
- `{n}` - Matches exactly `n` occurrences.
- `{n,}` - Matches `n` or more occurrences.
- `{n,m}` - Matches between `n` and `m` occurrences.

```ruby
/\d+/ =~ "12345"   # Matches one or more digits
/\d{2,4}/ =~ "12345"   # Matches between 2 and 4 digits
```

### Grouping and Capturing

- `()` - Groups patterns together.
- `$1`, `$2`, etc. - Capture group contents.

```ruby
/(abc)+/ =~ "abcabcabc"    # Matches "abc" one or more times
puts $1    # Prints "abc"
```

### Modifiers

- `i` - Case insensitive matching.
- `m` - Treat string as multiple lines.
- `x` - Ignore whitespace and comments.

```ruby
/hello/i =~ "HELLO"   # Matches case insensitive
```

## Methods

Ruby provides several methods for working with regular expressions:

- `=~`: Matches a string against a regular expression.
- `match`: Returns a MatchData object for the first match.
- `scan`: Returns an array of all matches.
- `sub`: Replaces the first occurrence.
- `gsub`: Replaces all occurrences.

## Resources

- [Ruby Regular Expressions Documentation](https://ruby-doc.org/core-3.0.2/doc/regexp_rdoc.html)
- [Rubular](https://rubular.com/): Interactive Ruby regular expression editor and tester.

Regular expressions are a vast topic, and mastering them takes practice. Experimenting with different patterns and exploring Ruby's regex capabilities will help you become proficient in using them effectively.
