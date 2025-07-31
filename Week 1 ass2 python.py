class Solution:
    def largestElement(self, arr):
        # Handle empty list edge case
        if not arr:
            return None
        
        max_element = arr[0]
        for num in arr:
            if num > max_element:
                max_element = num
        return max_element

# Test cases
if __name__ == "__main__":
    sol = Solution()

    arr1 = [1, 8, 7, 56, 90]
    print("Largest:", sol.largestElement(arr1))  # Output: 90

    arr2 = [5, 5, 5, 5]
    print("Largest:", sol.largestElement(arr2))  # Output: 5

    arr3 = [10]
    print("Largest:", sol.largestElement(arr3))  # Output: 10
