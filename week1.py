import random
def create_random_list(n,min_,max_):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers


def create_list_histogram(list_1):
    frequencies=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequencies)):
            if list_1[i] == frequencies[j][0]:
                frequencies[j][1]+=1
                s=True
        if s == False:
            frequencies.append([list_1[i],1])
    return frequencies


def get_mode_with_freq_list(freq_list):
    freq_max=-1
    mode=-1
    for item,freq in freq_list:
        if freq > freq_max:
            freq_max = freq
            mode = item
    return mode, freq_max



def linear_search(list_1, item):
    found = (-1, -1)
    n = len(list_1)
    for i in range(n):
        if list_1[i] == item:
            found = (list_1[i], i)
            # break
    return found


def bubble_sort(list_1):
    n = len(list_1)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if not list_1[j] < list_1[j+1]:
                list_1[j],list_1[j+1] = list_1[j+1], list_1[j]


def get_median(list_1):
    bubble_sort(list_1)
    n = len(list_1)
    if n % 2 == 1:
        middle = n//2 + 1
        median = list_1[middle]
    else:
        middle_1 = list_1[n//2]
        middle_2 = list_1[n//2+1]
        median = (middle_1+middle_2)/2
    return median


def binary_search(list_1, item):
    found = (-100, -100)
    low = 0
    high = len(list_1)-1
    while low <= high:
        mid = (low + high)//2
        if list_1[mid] == item:
            return (item, mid)
        elif list_1[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return found


list_1 = create_random_list(100,-100,100)
print(list_1)

hist_1 = create_list_histogram(list_1)
print(hist_1)

mode_1 = get_mode_with_freq_list(hist)
print(mode_1)

result_1 = linear_search(list_1, -2)
print(result_1)

list_2 = list_1
bubble_sort(list_2) 
print(list_2)

median = get_median(list_2)
print(median)

result = binary_search(list_2, -88)
if(result != (-100,-100)):
	print(result)
else:
	print("did not found")



