#!/usr/bin/env python
# coding: utf-8



# In[18]:


def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))




# In[19]:


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)




# In[20]:


def compareTo(s1, s2):
    if s1[0]< s2[0]:
        return -1
    elif s1[0]> s2[0]:
        return 1
    elif s1 == s2:
        return 0
    else:
        return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    fibonnaci()
    gcd()
    compareTo()

