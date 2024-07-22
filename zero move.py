nums = [0,1,0,3,2]
l=len(nums)-1
i=0
j=0
while j<l:
    j+=1
    if nums[i]!=0:
        i+=1
    nums[j],nums[i]=nums[i],nums[j]

print(nums)