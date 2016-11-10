def anti_vowel(text):
    t = ""

    for c in text:
        boolean = False

        #print text[c]
        for v in "aeiouAEIOU":
            
            if c == v:
                boolean = True
                print "True: ",c, v
            else:
                print "False: ",c, v
                
        #print "Check final: ",boolean 
        if not boolean:
            t += c
        
    return t

print anti_vowel("Hello World!!")
