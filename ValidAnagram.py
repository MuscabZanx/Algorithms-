def ValidAnagram(s, t):
    if len(s) != len(t):
        return False
    
    s, t = sorted(s), sorted(t)
    i, j = 0, 0

    while i < len(s):
        if s[i] != t[j]:
            return False
        
        i +=1
        j +=1
    return True 

print(ValidAnagram("anagram", "anagra"))