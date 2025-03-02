def mergeArrays(nums1: list, nums2: list) -> list:
    l1, l2 = len(nums1), len(nums2)
    i,j = 0, 0
    result = []

    while i < l1 and j < l2:
        if nums1[i][0] == nums2[j][0]:
            result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
            i += 1 
            j += 1 
        elif nums1[i][0] < nums2[j][0]:
            result.append(nums1[i])
            i += 1 
        else:
            result.append(nums2[j])
            j += 1 


    while i < l1:
        result.append(nums1[i])
        i += 1 

    while j < l2:
        result.append(nums2[j])
        j += 1 

    return result 


print(mergeArrays([[1,2], [2,3], [4,5]], [[1,4], [3,2], [4,1]]))
print(mergeArrays([[2,4], [3,6], [5,5]], [[1,3], [4,3]]))
