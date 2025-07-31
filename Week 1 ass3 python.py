class Solution:
    def getSecondLargest(self, arr):
        first = second = -1
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num != first and num > second:
                second = num
        return second

# Main function for VS Code
if __name__ == "__main__":
    n = int(input("Enter size of array: "))
    arr = list(map(int, input("Enter array elements: ").strip().split()))
    
    sol = Solution()
    result = sol.getSecondLargest(arr)
    print("Second largest element:", result)
