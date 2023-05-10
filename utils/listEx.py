"""
https://www.tutorialspoint.com/python/python_lists.htm
"""

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]


print("Value available at index 2 : ")
print(list[2])
list[2] = 2001;
print("New value available at index 2 : ");
print(list[2]);

print(list1);
del list1[2];
print(list1)

def compareToList(l1,l2):
    """

    :param l1:
    :param l2:
    :return:
    """
    return cmp(l1,l2);

"""
list1, list2 = [123, 'xyz'], [456, 'abc']
print cmp(list1, list2)
print cmp(list2, list1)
list3 = list2 + [786];
print cmp(list2, list3)
"""

"""
-1
1
-1
"""
