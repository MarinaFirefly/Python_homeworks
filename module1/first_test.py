def spam(number):
    return 'bulochka'*number

def my_sum(list_of_numbers):
    sum = 0
    for i in list_of_numbers:
        sum+=i
    return sum

def shortener(string):
    # old_list = string.split(" ")
    # new_list = []
    # for i in old_list:
    #     if len(i) > 6:
    #         new_list.append(i[0:6]+"*")
    #     else:
    #         new_list.append(i)
    # return (" ").join(new_list)
    return (" ").join([i[0:6]+"*" if len(i) > 6 else i for i in string.split(" ")])

def compare_ends(words):
    cnt = 0
    for i in list(words):
        if len(i) > 1 and i[0]==i[-1]:
            cnt+=1
    return cnt