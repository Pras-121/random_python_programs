def is_palindrome(s):
   rs =  s[::-1]
   if rs == s:
       return True
   else:
       return False
        
def palindromeIndex(s):
    lst=[]
  
    start=0
    end=len(s) -1
    # Write your code here
    if is_palindrome(s):
        return -1
    else:
        
        for i in range(len(s)//2):
            if s[start] == s[end]:
                start += 1
                end   -= 1
            else:
                from_left = is_palindrome(s[start+1:end+1])
                from_right =  is_palindrome(s[end-1:start-1:-1])
                
                if from_left:
                    return start
                if from_right:
                    return end
        # for item in s:
        #     lst.append(item)
        #     ns = "".join(lst)
        #     rs = ns[::-1] 
        #     if not is_palindrome(ns,rs):
        #             index = ns.index(item)
        #             return index
                
            
print(palindromeIndex("aaab")) # 3
print(palindromeIndex("baaab")) # -1
print(palindromeIndex("baa"))# 0
print(palindromeIndex("aba")) # -1
print(palindromeIndex("aabcdcba")) # 1