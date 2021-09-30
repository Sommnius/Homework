# Write a program which makes a pretty print of a part of the multiplication
# table.



left_start = int(input("a = "))
left_end = int(input("b = "))
top_start = int(input("c = "))
top_end = int(input("d = "))
result = " " * 4
for col in range(top_start, top_end + 1):
    result += f"{col:4}"  # first line
for row in range(left_start, left_end + 1):
    result += f"\n{row:4}"  # first element in a line
    for col in range(top_start, top_end + 1):
        result += f"{row*col:4}"   # element in line
print(result)
# bad for a,b,c,d > 100
