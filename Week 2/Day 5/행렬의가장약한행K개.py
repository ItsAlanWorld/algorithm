import collections
import heapq

mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
],
k = 3

soldiers = [row.count(1) for row in mat[0]]
print(heapq.nsmallest(k,soldiers))

