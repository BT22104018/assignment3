var1 = 1
var2 = 1
var3 = 2
i = 0
print(var1)
print(var2)
while i < 10:
   var1 = var1+var2
   print(var1)
   var2 = var1+var2
   print(var2)
   var3 = var3+var2
   i+=1
print((var3)/(i))