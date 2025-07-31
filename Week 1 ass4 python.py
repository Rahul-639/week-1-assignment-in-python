class Solution:
    def pushZerosToEnd(self, arr, n):
        count = 0
        for i in range(n):
            if arr[i] != 0:
                arr[count], arr[i] = arr[i], arr[count]
                count += 1

if __name__ == "__main__":
    # Read input
    data = input("Enter array elements separated by space:\n").strip().split()
    arr = list(map(int, data))
    n = len(arr)

    sol = Solution()
    sol.pushZerosToEnd(arr, n)
    print("Output array after pushing zeros to end:")
    print(arr)
