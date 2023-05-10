dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
"""
dict['Name']:  Zara
dict['Age']:  7

"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Alice']: ", dict['Alice']

"""
dict['Alice']:
Traceback (most recent call last):
   File "test.py", line 4, in <module>
      print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'
"""


dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])


dict['Age']:  8
dict['School']:  DPS School
"""