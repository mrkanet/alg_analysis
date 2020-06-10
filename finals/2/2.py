import random

def cr_vector(n):
    vec = []
    for i in range(n):
        vec.append(random.randint(0,10))
##    print(vec)
    return vec

def sc_mul_vectors(v1,v2):
    _len = len(v1)
    if(_len > len(v2)):
        _len = len(v2)
    mul = 0
    for i in range(_len):
        mul += v1[i]*v2[i]
    return mul

def print_matrix(m):
    print("*****")
    for i in m:
        print(i)

def cr_matrix(m,n):
    mat = []
    for i in range(m):
        mat.append(cr_vector(n))
    print_matrix(mat)
    return mat

def mul_matrix(m1,m2):
    if(len(m1[0]) == len(m2)):
        rev_m2 = rev_matrix(m2)
        mul_mat = []
        for i in range(len(m1)):
            mul_mat.append([])
            for j in range(len(rev_m2)):
##                print("carpimlar")
##                print_matrix([m1[i],rev_m2[j]])
                mul_mat[i].append(sc_mul_vectors(m1[i],rev_m2[j]))
        return mul_mat
    else:
        return None
    
def rev_matrix(m):
    rev = []
    for i in range(len(m[0])):
        rev.append([])
        for j in range(len(m)):
            rev[i].append(m[j][i])
    return rev

def mul_matrix_list(m_list):
    res = m_list[0]
    for i in range(1,len(m_list)):
        res = mul_matrix(res,m_list[i])
        if(res == None):
            return None
    return res

def tester():
##    print_matrix(mul_matrix(cr_matrix(2,3),cr_matrix(3,2)))
##  test case 1 -> fail
    m_list = []
    for i in range(5):
        m_list.append(cr_matrix(3,6))
    res = mul_matrix_list(m_list)
    if(res != None):
        print_matrix(res)
    else:
        print("*****")
        print("carpilamaz")
##  test case 2 -> succeed
    print("-----")
    m_list = []
    for i in range(5):
        m_list.append(cr_matrix(3,3))
    res = mul_matrix_list(m_list)
    if(res != None):
        print_matrix(res)
    else:
        print("*****")
        print("carpilamaz")


if(__name__ == "__main__"):
    
    tester()
    
