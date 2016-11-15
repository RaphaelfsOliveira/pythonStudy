def median(l_list):
    l_list.sort()
    result = 0
    #return l_list
    
    if len(l_list) <= 1:
        #print "if 1"
        #result = l_list[len(l_list)]
        result = 1
        #print result

    elif len(l_list) % 2 == 0:
        #print "elif 2"
        l = len(l_list) / 2
        #print l
        result = (l_list[l-1] + l_list[l]) / 2.0
        #print l_list[l-1], l_list[l]
        #print "Result: ", result
        #result = result / 2
    
    else:
        #print "else 3"
        #print l_list
        #print len(l_list) / 2
        l = len(l_list) / 2
        result = l_list[l]
    
    
    return result


#print median([4,5,5,4])
print median([6, 8, 12, 2, 23])
#print median([1])
#median([1])
