nums = [1,2,3,4,5,6,7,8,9,10]
-------------------------------
# filter(function,list)

def even(num):
     return (num%2)==0
        
# (lambda_function in filter)
 print(list(filter(lambda num: (num%2)==0,nums))) 
# -------------------------------------------------



 evenNums = list(filter(even,nums))
 print(evenNums)
 _________________________________________________


# comprehension method
nums = [num for num in nums if (num%2)==0]
print(nums)
_____________________________________________


