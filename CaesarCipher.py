def caesarCipher(s, k):
    # Write your code here
    lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    out_str=[]
    for char in s:
        wasCap=False
        if char in lst or char in cap:
            if char.isUpper():
                wasCap =True
                char = char.lower()
                
            pos = lst.index(char)
            
            if pos+k >= len(lst):
                n=(k-(25 - pos)-1) %26
            else:
                n=(pos+k) %26      
            a = lst[n].upper() if wasCap else lst[n]
            out_str.append(a)
            print(out_str)
        else:
            out_str.append(char)
    return "".join(out_str)



# test="abcdefghijklmnopqrstuvwxyz"
# test="middle-Outz"
# test="1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M"
test="www.abc.xy"
print(caesarCipher(test,87))