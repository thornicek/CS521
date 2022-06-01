#!/usr/bin/env python
# coding: utf-8

# In[1]:


def f(x):
    if(x==0):
        return 1
    elif(x==1):
        return 1
    elif(x==2):
        return 3
    elif(x>2):
        return f(x-1)+2*f(x-2)+3*f(x-3)


# In[2]:


f(20)


# In[6]:


def valid_DNA(x):
    valid_chars = ("A","C","G","T")
    current_max = 0
    current_length = 0
    for char in x:
        if char in valid_chars:
            current_length += 1
        else:
            if current_length > current_max:
                current_max = current_length
            current_length = 0
            continue
    return current_max


# In[7]:


valid_DNA("ACGDA")


# In[8]:


valid_DNA("GTLGDCACCCALCCTCGXGAXXCTTCTTAXTCTAXTDLXCATGDACCTCCGAGAGGGAGAGTTDACCACACAGTTAALGXDLXCAGLGXDCGXGAAGGDGTCACGATTGAGACGGGCGGAGGDGTTLLCCTXDTGCAXALCGTAGAGGAACDTTAGAAGDGGAAACGTAAGCGGTTDDACCGCTTGGGACCCGCCGATACTLGGXAAGADTLGXAAGTGTALCXCCCTGLCGAAGGDLLTGXGCCATAAAGACGCAGDGCCTTADCDAAGGXLAXCAGCXCCAACAGLCGCAGLAXCAGT")


# In[ ]:




