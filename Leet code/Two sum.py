nums=[1,2,3]
target = 4
for i in range(len(nums)) :
    for j in range(len(nums)) :
        [i ,j] = [j , i]
        if nums[i] + nums[j] == target :
            print([i , j])