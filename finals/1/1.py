import random
#0: soldan saga, 1: sagdan sola, 2: asagidan yukariya, 3: yukaridan asagiya
words = ['q','w','e','r','t','y','u','o','p','a','s','d','f','g','h','j','k','l','i','z','x','c','v','b','n','m']
g_matrix = []
koruma = []
def new_matrix(m,n):
    n_matrix = []
    for i in range(m):
        n_matrix.append([])
        for j in range(n):
            loc = random.randint(0,len(words)-1)
            n_matrix[i].append(words[loc])
    global g_matrix
    g_matrix = n_matrix
    koruma = g_matrix
    print_matrix(g_matrix)

def add_word(i,j,orient,word):
    global g_matrix
    if(len(g_matrix) > i and len(g_matrix[0]) > j):    
            #kodlar burada
            if(orient == 0):
                #soldan saga
                while(word != ""):
                    c = word[0]
                    word = word[1:]
                    if (j == len(g_matrix[0])):
                        j = 0
                        i += 1
                    if (i == len(g_matrix)):
                        i = 0
                    g_matrix[i][j] = c
                    j += 1 
            elif(orient == 1):
                #sagdan sola
                while(word != ""):
                    c = word[0]
                    word = word[1:]
                    if (j == -1):
                        j = len(g_matrix[0])-1
                        i -= 1
                    if (i == -1):
                        i = len(g_matrix)-1
                    g_matrix[i][j] = c
                    j -= 1    
            elif(orient == 2):
                #asagidan yukariya
                while(word != ""):
                    c = word[0]
                    word = word[1:]
                    if(i == -1):
                        i = len(g_matrix)-1
                        j -= 1
                    if(j == -1):
                        j = len(g_matrix[0])-1
                    print(i,j)
                    g_matrix[i][j] = c
                    i -= 1
            elif(orient == 3):
                #yukaridan asagiya
                while(word != ""):
                    c = word[0]
                    word = word[1:]
                    if(i == len(g_matrix)):
                        i = 0
                        j += 1
                    if(j == len(g_matrix[0])):
                        j = 0
                    g_matrix[i][j] = c
                    i += 1
            else:
                print("orientation out of range")
    else:
        print("out of range")
        g_matrix = koruma
        return
    print_matrix(g_matrix)
    return

def myReverse(v):
    v2=[]
    for i in v[::-1]:
        v2.append(i)
    return v2

def palindrom_list():
    global g_matrix
    if(len(g_matrix[0]) < 10):
        return []
    elif(len(g_matrix[0]) == 10):
        pol_list = []
        for i in range(len(g_matrix)):          
            if(g_matrix[i] == myReverse(g_matrix[i])):
                if(g_matrix[i] not in pol_list):
                    pol_list.append(g_matrix[i])
        return pol_list
    else:
        pol_list = []
        for i in range(len(g_matrix)):
            a = g_matrix[i]
            count = len(a)-9
            count = count*(count+1)/2
            l,k = 10,0
            for j in range(int(count)):
                v = g_matrix[i][k:l]

                if(v == myReverse(v)):
                    if(v not in pol_list):
                        pol_list.append(v)
                    l+=1
                else:
                    l+=1
                
                if(k+l == len(g_matrix[0])+1):
                    l = 10
                    k+=1
        return pol_list
                        
def print_matrix(m):
    for i in m:
        print(i)
def tester():
    
    #palindrom test
    print(new_matrix(15,15))
    print(add_word(0,0,0,"tenettenettenet"))
    print_matrix(palindrom_list())


if(__name__ == "__main__"):
    tester()
    
