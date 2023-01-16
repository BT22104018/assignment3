print("\nQuestion 5")

string = "ABCDEFGHIJK"
count = 0
while len(string)-count*2 >= 1:
    print(" "*count, string[0 : len(string) - count*2])
    count += 1