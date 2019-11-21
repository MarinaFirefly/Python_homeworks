import functools

def spam(number):
    return 'bulochka'*number

def my_sum(list_of_numbers):
    # total = 0
    # for i in list_of_numbers:
    #     total+=i
    # return total
    
    # return sum(i for i in list_of_numbers)

    return functools.reduce(lambda x,y: x+y, list_of_numbers)

def shortener(string):
    # old_list = string.split(" ")
    # new_list = []
    # for i in old_list:
    #     if len(i) > 6:
    #         new_list.append(i[0:6]+"*")
    #     else:
    #         new_list.append(i)
    # return (" ").join(new_list)
    return (" ").join([i[:6]+"*" if len(i) > 6 else i for i in string.split(" ")])

def compare_ends(words):
    # cnt = 0
    # for i in list(words):
    #     if len(i) > 1 and i[0]==i[-1]:
    #         cnt+=1
    # return cnt
    return len(['' for i in list(words) if len(i) > 1 and i[0]==i[-1]])