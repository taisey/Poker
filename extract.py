def extract(list_,num):
    ans_list=[]

    if(list_==[] or num==0):
        return [[]]
    if(len(list_)<num):
        return [[]]

    for i in extract(list_[1:],num-1):
        ans_list.append(list_[0:1]+i)
    for i in extract(list_[1:],num):
        ans_list.append(i)
    if len(ans_list)>1 and [] in ans_list:
        ans_list.remove([])
    return ans_list
