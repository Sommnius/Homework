# Create a program that asks the user for a number and then prints out a list
# of all the [divisors]



number = int(input("Enter a number:\n"))
sqrt = int(number ** 0.5)  # square root
result = []  # creating list
for divisor in range(1, sqrt + 1):  # 1...sqrt(number), so, it should be two times faster
    if number % divisor == 0:
        result.extend([divisor, number // divisor])  # append two divisors at the same time
if sqrt in result: result.remove(sqrt)  # remove duplicate.
result.sort()  # sort
print(result)
