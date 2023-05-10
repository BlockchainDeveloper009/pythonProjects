import time;  # This is required to include time module.

print('refer: https://www.tutorialspoint.com/python/python_date_time.htm')

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)


var1 = 'Hello World!'
var2 = "Python Programming"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])


print("Updated String :- ", var1[:6] + 'Python')


var = 100
if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
   elif var == 50:
      print "Which is 50"
   elif var < 50:
      print "Expression value is less than 50"
else:
   print "Could not find true expression"

print "Good bye!"