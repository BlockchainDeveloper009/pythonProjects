#https://www.edureka.co/blog/data-structures-in-python/
#
# #List



#Set
my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}

@count
def handleSets():
    try:
        print(my_set.union(my_set_2), '----------', my_set | my_set_2)
        print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
        print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
        print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
        my_set.clear()
        print(my_set)
    except IndexError as er:
        print(er)
    except (NameError, TypeError, RuntimeError) as e:
        print(e)

#Dictionary

#Stack
#Double-ended queue
#Hash table

"""
Arrays vs. List
Stack
Queue
Trees
Linked Lists
Graphs
HashMaps

"""