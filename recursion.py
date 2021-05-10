#!/usr/bin/env python
# coding: utf-8

# <b>Fibonnaci Sequence</b>

# In[11]:


def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))


# In[13]:


fibonnaci(3)


# <b>Euclid’s GCD Algorithm</b>

# In[14]:


def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


# In[15]:


gcd(60,48)


# <b>Recursive string Comparison</b>

# In[6]:


def compareTo(s1, s2):
    if str1[index] != str2[index]:
        return 1
    else:
        if the index exceeds the length of either string
            return 0
        else:
            return recursive_string_comparison(str1, str2, index + 1)


# In[ ]:




