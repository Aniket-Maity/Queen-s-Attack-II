# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:15:33 2020

@author: Aniket Maity
"""

'''
5 3
4 3
5 5
4 2
2 3
'''

n = 5
k = 3
r_q = 4
c_q = 3
obstracles = [[5,5],[4,2],[2,3]]


#left coords
for i in range(1,c_q):
    print(r_q,c_q-i)
#right coords
for i in range(1,(n-c_q)+1):
    print(r_q,c_q+i)
#down coords
for i in range(1,r_q):
    print(r_q-i,c_q)
#up coords
for i in range(1,(n-r_q)+1):
    print(r_q+1,c_q)
#upper Right
for i in range()
#rightCount = 
#upCount = 
#downCount = 