# https://www.kdnuggets.com/2020/01/python-string-processing-primer.html

# Stripping Whitepsace
s = '    This is a sentence with whitespace.    \n'
print('Strip leading whitespace: {}'.format(s.lstrip()))
print('Strip trailing whitespace: {}'.format(s.rstrip()))
print('Srip all whitespace: {}'.format(s.strip()))

s = 'This is a sentence with unwanted characters.AAAAAAAA'
print('Strip unwanted characters: {}'.format(s.rstrip('A')))

# Splitting Strings
s = 'Nobody exists on purpose. Nobody belongs anywhere.'
print(s.split())
# By default, split() splits on whitespace, but other character(s) sequences can be passed in as well.
s = 'Nobody,exists,on,purpose.Nobody,belongs,anywhere.'
print('\',\' separated split -> {}'.format(s.split(',')))
print('\'.\' separated split ->{}'.format(s.split('.')))

# Joining List Elements Into a String
# join list element strings into a single string in Python using the join() method
s = ['Welcome', 'to', 'club', 'pal']
print(' '.join(s))

s = ['GitHub', 'GitPod', 'Git',]
print(' and '.join(s))

# Reversing
s = 'Wubba'
print('The reverse of Wubba is {}'.format(s[::-1]))

# Converting Uppercase and Lowercase
s = 'WuBba'
print('\'WuBba\' as uppercase: {}'.format(s.upper()))
print('\'WuBba\' as lowerrcase: {}'.format(s.lower()))
print('\'WuBba\' as swapped case: {}'.format(s.swapcase()))

# String Membership
s1 = 'Membership'
s2 = 'Member'
s3 = 'ship'
s4 = 'Emper'
print('\'Member\' in \'Membership\' -> {}'.format(s2 in s1))
print('\'ship\' in \'Membership\' -> {}'.format(s3 in s1))
print('\'Emper\' in \'Membership\' -> {}'.format(s4 in s1))

# finding the location of a substring 
s = 'Does this string contain a substring?'
print('\'string\' location -> {}'.format(s.find('string')))
print('\'spring\' location -> {}'.format(s.find('sub')))
print('\'spring\' location -> {}'.format(s.find('spring')))

# Replacing Substrings
s1 = 'Lemme check my list of powers and weaknesses: ability to do anything, but only whenever I want'
s2 = 'strength'
print('The new sentence: {}'.format(s1.replace('weaknesses', s2)))

# Combining the Output of Multiple Lists
songs = ['shape of you', 'closer', 'circles']
artists = ['ed sheeran', 'the chainsmokers', 'postmalone']

for song, artist in zip(songs, artists):
  print('{} by {}'.format(song, artist))

# Checking for Anagrams

from collections import Counter
def is_anagram(s1, s2):
  return Counter(s1) == Counter(s2)

# Stripping Whitepsace

s = '    This is a sentence with whitespace.    \n'
print('Strip leading whitespace: {}'.format(s.lstrip()))
print('Strip trailing whitespace: {}'.format(s.rstrip()))
print('Srip all whitespace: {}'.format(s.strip()))

s = 'This is a sentence with unwanted characters.AAAAAAAA'
print('Strip unwanted characters: {}'.format(s.rstrip('A')))

# Splitting Strings
s = 'Nobody exists on purpose. Nobody belongs anywhere.'
print(s.split())
# By default, split() splits on whitespace, but other character(s) sequences can be passed in as well.
s = 'Nobody,exists,on,purpose.Nobody,belongs,anywhere.'
print('\',\' separated split -> {}'.format(s.split(',')))
print('\'.\' separated split ->{}'.format(s.split('.')))

# Joining List Elements Into a String
# join list element strings into a single string in Python using the join() method
s = ['Welcome', 'to', 'club', 'pal']
print(' '.join(s))

s = ['GitHub', 'GitPod', 'Git',]
print(' and '.join(s))

# Reversing
s = 'Wubba'
print('The reverse of Wubba is {}'.format(s[::-1]))

# Converting Uppercase and Lowercase
s = 'WuBba'
print('\'WuBba\' as uppercase: {}'.format(s.upper()))
print('\'WuBba\' as lowerrcase: {}'.format(s.lower()))
print('\'WuBba\' as swapped case: {}'.format(s.swapcase()))

# String Membership
s1 = 'Membership'
s2 = 'Member'
s3 = 'ship'
s4 = 'Emper'
print('\'Member\' in \'Membership\' -> {}'.format(s2 in s1))
print('\'ship\' in \'Membership\' -> {}'.format(s3 in s1))
print('\'Emper\' in \'Membership\' -> {}'.format(s4 in s1))

# finding the location of a substring 
s = 'Does this string contain a substring?'
print('\'string\' location -> {}'.format(s.find('string')))
print('\'spring\' location -> {}'.format(s.find('sub')))
print('\'spring\' location -> {}'.format(s.find('spring')))

# Replacing Substrings
s1 = 'Lemme check my list of powers and weaknesses: ability to do anything, but only whenever I want'
s2 = 'strength'
print('The new sentence: {}'.format(s1.replace('weaknesses', s2)))

# Combining the Output of Multiple Lists
songs = ['shape of you', 'closer', 'circles']
artists = ['ed sheeran', 'the chainsmokers', 'postmalone']

for song, artist in zip(songs, artists):
  print('{} by {}'.format(song, artist))

# Checking for Anagrams

from collections import Counter
def is_anagram(s1, s2s2):
  return Counter(s1) == Counter(s2)
  
s1 = 'listen'
s2 = 'silent'
s3 = 'runner'
s4 = 'neuron'

print('\'listen\' is an anagram of \'silent\' -> {}'.format(is_anagram(s1, s2)))
print('\'runner\' is an anagram of \'neuron\' -> {}'.format(is_anagram(s3, s4)))

# Checking for Palindromes

def is_palindrome(s):
  reverse = s[::-1]
  if (s == reverse):
    return True
  return False

s1 = 'racecar'
s2 = 'malayalam'
s3 = 'madmax'
print('\'racecar\' a palindrome -> {}'.format(is_palindrome(s1)))
print('\'malayalam\' a palindrome -> {}'.format(is_palindrome(s2)))
print('\'madmax\' a palindrome -> {}'.format(is_palindrome(s3)))
