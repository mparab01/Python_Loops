
# coding: utf-8

# In[57]:

import random as rnd


# In[58]:

a = rnd.random()
print a
if a>0.9:
    print "greater than 0.9"
elif 0.1<a and a<0.5:
    print "greater than 0.1 but less than 0.5"
elif 0.5<a and a<0.9:
    print "greater than 0.5 but less than 0.9"
else:
    print "lower than 0.1"


# In[59]:

d = {'one':1, 'two': 2, 'three': 3}


# In[60]:

for k,v in d.iteritems():
    print k
    print v


# In[61]:

x = 0

while x<10:
    print "X is : " ,x
    x+=1
else:
    print "All done"

