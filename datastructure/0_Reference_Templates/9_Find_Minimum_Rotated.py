def find_min_rotated(arr: list[int]) -> int:
    left = 0
    right = len(arr) -1
    boundary_index =-1

    while left <=right:
        mid = (left + right) // 2
        # if <= last element, then belogs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = midright = mid - 1
        else:
            left = mid + 1

    return boundary_index


print(find_min_rotated([30,40,50,10,20]))
