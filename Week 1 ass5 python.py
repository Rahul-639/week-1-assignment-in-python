def rotate(arr):
    n = len(arr)
    
    # Store the last element
    last = arr[-1]

    # Shift elements to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Set the first element
    arr[0] = last

    return arr

# ---------- Driver Code ----------
if __name__ == "__main__":
    # Input array from user
    arr = list(map(int, input("Enter elements separated by space: ").split()))
    
    rotated_arr = rotate(arr)
    
    print("Rotated array:", rotated_arr)
