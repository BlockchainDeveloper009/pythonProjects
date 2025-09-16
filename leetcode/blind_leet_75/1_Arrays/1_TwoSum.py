def two_sum(arr: list[int], target:int) -> list[int]:
    num_to_index = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement]]
    return []

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(arr,target)
    print(" ".join(map(str,res)))

