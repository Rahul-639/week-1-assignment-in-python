def reverse_string(s):
    return s[::-1]  # Pythonic way to reverse a string

# --------- Driver Code ---------
if __name__ == "__main__":
    s = input("Enter a string: ")
    reversed_s = reverse_string(s)
    print("Reversed string:", reversed_s)
