import re
def strength_compare(card1,card2):
    checker1=[0]*13
    checker2=[0]*13
 
    for i in card1:
        checker1[int(re.sub(r"\W", "", i))-1] += 1
    for i in card2:
        checker2[int(re.sub(r"\W", "", i))-1] += 1 

    #for i in card1:
    #    checker1[i-1]+=1
    #for i in card2:
    #    checker2[i-1]+=1
    max1=max(checker1)
    max2=max(checker2)
    checker1=checker1[0:1]+list(reversed(checker1[1:]))
    checker2=checker2[0:1]+list(reversed(checker2[1:]))
    #print("checker1:",checker1)
    #print("checker2:",checker2)
    for max_tmp in reversed(range(1,max1+1)):
        for k in range(len(checker1)):
            i=checker1[k]
            j=checker2[k]
            if(i==max_tmp or j==max_tmp):
                if(i>j):
                    return 0
                elif(j>i):
                    return 1
    return -1

print(strength_compare(['♡9', '♧13', '♤3', '♢2', '♡2'],['♧13', '♤3', '♢2', '♧5', '♡2']))
        
    
    



#input 2 cards (they have same score) except for flash
#stronger one