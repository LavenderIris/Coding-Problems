#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    d_list = returnDiffList(sortList(a))
    lnum = 0 
    rnum = 0
    #length of my list - 1 to show how list index is
    listlen = len(d_list)-1
    
    for i in range(0, len(d_list)):
        if i = 1: 
            lnum = diff[i-1] + lnum
        elif i = listlen-1
            rnum = diff[i+1] + rnum
        elif (i>=2) and (i <= listlen-2)
            lnum = 
    
    
    
    answer = 0
    return answer


# Tail starts here

def sortList(a_list):
    a_list = [int(x) for x in a_list]
    a_list.sort()
    return a_list    
        
def returnDiffList(a_list):
    diff_list = []
    for i in range(1, len(a_list)):
        diff_list.append(abs(a_list[i]- a_list[i-1]))
    return (diff_list)        


    
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
        
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    
    print(pairs(b,_k))
    
    
