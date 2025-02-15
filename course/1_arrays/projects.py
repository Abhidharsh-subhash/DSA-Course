# Calculate Average Temperature

a = int(input("how many day's temperature?"))
print(a)
temperatures = []
for i in range(a):
    x = int(input(f"Day {i+1}'s high temperature"))
    temperatures.append(x)

average = sum(temperatures) / a
print(f"Average = {average}")
count = 0
for i in temperatures:
    if i > average:
        count += 1
if count > 0:
    print(f"{count} day(s) above average")
