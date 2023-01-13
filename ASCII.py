# Inputs by the user
l = int(input())  # can be hard coded to 4
h = int(input())  # can be hardcoded to 5
t = str(input())

# Creating a list with the ASCII art rows. Each row will be an item in the list.
rows = []
for i in range(h):
    row = str(input())
    rows.append(row)

# Looping through the range of H for each row
for i in range(h):
    # looping through each character in the input text
    for ch in t:
        if ch >= 'a' and ch <= 'z':
            x = ord(ch) - ord('a')
        elif ch >= 'A' and ch <= 'Z':
            x = ord(ch) - ord('A')
        else:
            x = ord('z') - ord('a') + 1

        # Looping through the length l, from the beginning of each character to the end
        for j in range(l):
            print(rows[i][x * l + j], end='')

    print('')
