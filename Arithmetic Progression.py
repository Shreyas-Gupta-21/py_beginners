#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to generate_AP
def generate_AP(a, d, n):
    AP_series = []
    for i in range(1,n+1,1):
        AP_series.append(int(a+(i-1)*d))
    return AP_series


print('enter test_cases')	
T = int(input())

if T<=25 and 1<=T:
    for i in range(1,T+1):
        print("enter values for case",i)
        print("enter 1st element, differnce, number of terms: ")
        a, d,n = map(int, input().split())
        
        if ((int(a)<=20) and (-20<=int(a))) and  ((int(d)<=20) and (-20<=int(d))) and  ((int(n)<=20) and (-20<=int(n))):
            AP_series = generate_AP(a, d, n)
            print("AP is -")
            print(AP_series)

            sum_AP_series =((n)*(2*a + (n-1)*d))/2
            print("Sum of AP terms is -")
            print (sum_AP_series) 
            
            sqr_AP_series = list(map(lambda x: x*x , AP_series)) 
            print("Square of AP is -")
            print(sqr_AP_series)
             
        else:
            print("values out of range")
else:
    print("test case out of range")


# In[ ]:




