# Set the size of the butterfly (number of rows in each half)
n = 5

# Loop for the upper half of the butterfly
for i in range(1, n + 1):
    # Left wing stars
    for j in range(1, i + 1):
        print("*", end="")
        
    # Spaces between the wings
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
        
    # Right wing stars
    for j in range(1, i + 1):
        print("*", end="")
        
    # Move to the next line
    print()

# Loop for the lower half of the butterfly
for i in range(n, 0, -1):
    # Left wing stars
    for j in range(1, i + 1):
        print("*", end="")
        
    # Spaces between the wings
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end="")
        
    # Right wing stars
    for j in range(1, i + 1):
        print("*", end="")
        
    # Move to the next line
    print()

