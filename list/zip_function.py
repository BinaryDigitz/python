list1 = [1,2,3,4,]
list2 = [ 10, 20, 30]


# a zip function takes one or more functions list and create a tupple with each item in the list 
zip_list = zip(list1, list2)

for item in zip_list:
    print(item)