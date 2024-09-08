def wordBreak(n, s, dictionary):
    
    word_set = set(dictionary)
    
    
    dp = [False] * (len(s) + 1)
    
    
    dp[0] = True
    
   
    for i in range(1, len(s) + 1):
        for j in range(i):
            
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  
    
    
    return 1 if dp[len(s)] else 0


n1 = 6
s1 = "ilike"
dictionary1 = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(wordBreak(n1, s1, dictionary1))  # Output: 1

n2 = 6
s2 = "ilikesamsung"
dictionary2 = ["i", "like", "sam", "sung", "samsung", "mobile"]
print(wordBreak(n2, s2, dictionary2))  # Output: 1
