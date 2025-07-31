def is_sorted(arr):
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False  # Found an element smaller than its previous one
    return True

# ---------- Driver Code ----------
if __name__ == "__main__":
    # Input array from user
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    
    if is_sorted(arr):
        print("true")
    else:
        print("false")
