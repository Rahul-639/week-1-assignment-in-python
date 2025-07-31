class Solution:
    def insertAtEnd(self, arr, val):
        arr.append(val)
        return arr

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    result1 = sol.insertAtEnd([1, 2, 3, 4, 5], 90)
    print("Output 1:", result1)  # Expected: [1, 2, 3, 4, 5, 90]

    # Example 2
    result2 = sol.insertAtEnd([1, 2, 3], 50)
    print("Output 2:", result2)  # Expected: [1, 2, 3, 50]
