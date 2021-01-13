#!/usr/bin/env python
# coding: utf-8

# In[2]:


def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


# In[3]:


def printer(*args):
    print('there are ', len(args), ' arguements')

printer('Horsefeather','Adonis','Bone')


# In[36]:


def printDictionary(**args):
    print(args)
    for k in args:
        print(k )

        
printDictionary(Country='Canada',Province='Ontario',City='Toronto')


# Come up with a function that divides the first input by the second input:
# 

# In[26]:


def divider(a,b):
    print(int(a/b))
    
divider(10,2)    


# In[27]:


# Use the con function for the following question

def con(a, b):
    return(a + b)


# In[28]:


con(2,2)


# In[30]:


con('a','b')


# In[34]:


con(('1'),('2'))


# You have been tasked with creating a lab that demonstrates the basics of probability by simulating a bag filled with colored balls. The bag is represented using a dictionary called "bag", where the key represents the color of the ball and the value represents the no of balls. The skeleton code has been made for you, do not add or remove any functions. Complete the following functions -
# 
# fillBag - A function that packs it's arguments into a global dictionary "bag".
# totalBalls - returns the total no of balls in the bucket
# probOf - takes a color (string) as argument and returns probability of drawing the selected ball. Assume total balls are not zero and the color given is a valid key.
# probAll - returns a dictionary of all colors and their corresponding probability

# In[46]:


def fillBag(**specs):
    global bag 
    bag = specs


def totalBalls():
    return sum(bag.values())

def probOf(color):
    return (bag[color]/totalBalls())

def probAll():
    for i in bag:
        print(i, " : ", prob(i))
    
        

    


# In[49]:



testBag = dict(red = 12, blue = 20, green = 14, grey = 10)

dictCasting = dict(a = 1, b =2, c=3)
print(dictCasting)

total =  sum(testBag.values())
prob={}
for color in testBag:
    prob[color] = testBag[color]/total;

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("fillBag : ")
try:
    fillBag(**testBag)
    print(testMsg(bag == testBag))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")



print("totalBalls : ")
try:
    print(testMsg(total == totalBalls()))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probOf")
try:
    passed = True
    for color in testBag:
           if probOf(color) != prob[color]:
                passed = False
        
    print(testMsg(passed) )
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    
print("probAll")
try:
    print(testMsg(probAll() == prob))
except NameError as e: 
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
    


# In[ ]:




