def findrepeats(s):
    i=1
    r=0
    found = False
    while i < len(s) and r < len(s):
        if s[r] == s[i]:
            if r == i:
                i=i+1
            else:
                i=0
                r=r+1
                
        else: i=i+1
    if r < len(s):
        print("the index of first not repeating string is : " , r)
    else:
        print(-1)
            
wordd=input("enter a word bro ")
findrepeats(wordd)