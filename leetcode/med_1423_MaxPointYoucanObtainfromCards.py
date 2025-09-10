def maxScore (cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints[:k])
    max_points = total

    for i in range(1, k+1):
        total = total - cardPoints[k-i]+ cardPoints[-i]
        max_points = max(max_points, total)

    return max_points


# Example usage:
cardPoints = [1,2,3,4,5,6,1]
k=3
print(maxScore(cardPoints,k)) # Output: 12


cardPoints = [2,2,2]
k=2
print(maxScore(cardPoints,k)) # Output: 4


cardPoints = [9, 7,7,9,7,7,9]
k=7
print(maxScore(cardPoints,k)) # Output: 12