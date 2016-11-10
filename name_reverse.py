def reverse(text):
    t = ""
    for c in range(len(text)-1,-1,-1):
        t += text[c]
    
    return t


print reverse("Raphael!")
print
print reverse("Python!")


