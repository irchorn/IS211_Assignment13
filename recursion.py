#!/usr/bin/env python
# coding: utf-8

#  <b>Fibonnaci Sequence</b>

# In[18]:


def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))


# <b>Euclid’s GCD Algorithm</b>

# In[19]:


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


# <b>Recursive string Comparison</b>

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

