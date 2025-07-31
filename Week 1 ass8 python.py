def frequency_count(arr):
    n = len(arr)
    freq = [0] * n  # Initialize frequency array with zeros

    for num in arr:
        if 1 <= num <= n:
            freq[num - 1] += 1  # Decrease index by 1 for 0-based indexing

    return freq

# ---------- Driver Code ----------
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements separated by space: ").split()))
    result = frequency_count(arr)
    print("Frequency array:", result)
