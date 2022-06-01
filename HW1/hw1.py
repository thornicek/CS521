#!/usr/bin/env python
# coding: utf-8
#Tomáš Horníček, no collaborators, no sources, not using the extension option

# In[1]:


def say_greeting(first_name, last_name):
    greeting = f"Hello, your name is {first_name} {last_name}"
    return greeting


# In[2]:


say_greeting("Joe","Biden")


# In[3]:


def calculate_letter(score):
    if score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 50:
        return "D"
    elif score >= 0:
        return "F"


# In[4]:


calculate_letter(81.5)


# In[5]:


def calculate_day(num_hours):
    whole_days = num_hours//24
    days_after = whole_days%7
    if days_after == 0:
        day = "Wednesday"
    elif days_after ==1:
        day = "Thursday"
    elif days_after ==2:
        day = "Friday"
    elif days_after ==3:
        day = "Saturday"
    elif days_after ==4:
        day = "Sunday"
    elif days_after ==5:
        day = "Monday"
    else:
        day = "Tuesday"
    hours = num_hours%24
    if hours >12:
        hours = hours - 12
        suffix = "PM"
    elif hours == 12:
        suffix ="PM"
    else:
        suffix = "AM"
    return f"{day} at {hours} {suffix}"


# In[6]:


calculate_day(1000)


# In[7]:


calculate_day(36)


# In[11]:


def calculate_volume(shape,dimensions):
    radius = dimensions[0]
    if shape == "sphere":
        volume = (4/3)*3.14*radius**3
        volume=round(volume,2)
    elif shape == "cone":
        height = dimensions[1]
        volume = (1/3)*3.14*height*(radius**2)
        volume=round(volume,2)
    else:
        return "Invalid Shape"
    return volume


# In[9]:


calculate_volume("sphere",(5,))


# In[12]:


calculate_volume("cone",(3,7))


# In[13]:


calculate_volume("prism",(2,2,1))


# In[ ]:




