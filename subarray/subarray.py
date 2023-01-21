
a=[3,4,4,1]
b=[]
m=2
# generate array b from array a
while m:
    for i in range(len(a)): 
        b.append(a[i])
    m-=1
#print(b)  b=[3,4,4,1,3,4,4,1]  

upper_bound_sum = 6
no_of_subarrays = 0
subarray_list =[]

# generate subarrays of array b
for i in range(len(b)+1):
    for j in range(i+1,len(b)+1):
        subarray = b[i:j]
        if sum(subarray) <= upper_bound_sum:
#         no_of_subarrays+=1
#print(subarray_list) 

# check no of subarrays in b which are <= upper_bound_sum
# for elements in subarray_list:
#     if sum(elements) <= upper_bound_sum:
#         no_of_subarrays+=1
print(no_of_subarrays)
