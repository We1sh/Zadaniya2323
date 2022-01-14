def is_lucky(num):
  count1 = 0
  count2 = 0
  for i in str(num):
    if int(i) %2 == 0:
      count1 += 1
      print("Yes")
    
    else:
      count2 += 1
      print("No")
      
  return count1 == count2
a=int(input())
b=int(input())
for j in range(a,b):
  is_luc
