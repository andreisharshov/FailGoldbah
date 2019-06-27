
# coding: utf-8

# In[149]:


mnozh_set = set()
mnozh_set.add(1)
simple_num = set()
simple_num.add(1)
simple_list = []
simple_list.append(1)

def SimpleNum(num):
    i = 2
    ans_list = []
    num_main = num
    while num != 1:
        if num%i == 0:
            num = num/i
            mnozh_set.add(i)
        else:
            i += 1
    
    if len(mnozh_set) > len(ans_list):
        for i in mnozh_set:
            ans_list.append(i)
    ans_list.sort()
    ans_list.reverse()
    if ans_list[0] == num_main:
        
        return True
    else:
        
        return False


def FindSimpleNumLess(num):
    board = simple_list[-1]
    for j in range(board, num+1):
        if SimpleNum(j) == True:
            simple_num.add(j)  
        else:
            continue
            
    if len(simple_num) > len(simple_list):
        for i in simple_num:
            simple_list.append(i)
    simple_list.sort()
    return simple_list
    
def GoldbahTest(y, x):
    stop = 0
    for b in x:
        jack = (((y - b)/2)**0.5)%1
        if jack == 0:
            stop += 1
            break
    if stop == 0:
        return False
    elif stop == 1:
        return True    

FindNumber = 0    
z = 3    
while True:
    
    if SimpleNum(z) == True:
        simple_list.append(z)
        z += 2
    else:
        x = FindSimpleNumLess(z)      
        if GoldbahTest(z, x) == False:
            FindNumber += z
            break
        elif GoldbahTest(z, x) == True:
            z += 2

print(FindNumber, 'не удовлетворяет Гольдбаха')


# In[146]:




