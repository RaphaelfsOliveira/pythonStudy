def remove_duplicates(l_list):
    l_new = []

    for l in l_list:
        if l not in l_new:
            l_new.append(l)
    return l_new

print remove_duplicates([4,5,5,4])
