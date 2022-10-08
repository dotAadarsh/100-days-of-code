# 14. Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

def longest_common_prefix(strs):
  r = []
  first_word = strs[0]
  for i,e in enumerate(first_word):
    try: 
      if all(e == word[i] for word in strs):
        r.append(e)
      else:
        break
    except:
      pass
        
  if r:
    return ''.join(r)
  else:
    return ''

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
print(longest_common_prefix(strs1))
print(longest_common_prefix(strs2))
