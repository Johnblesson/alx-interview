# Three Steps
# Input no. of rows
# Nested list of numbers

n = int(input("enter the row number: "))
triangle = []
for i in range (n) :
  temp_list=[]
  for j in range(i+1) :
    if j==0 or j==i :
      temp_list.append (1)
    else:
      temp_list.append(triangle[i-1] [j-1] + triangle[i-1] [j])
  triangle.append(temp_list)

# print(triangle)

# require shape
for i in range(n) :
  for j in range(n-i-1) :
    print(format(" ", "<2") ,end="")
  for j in range(i+1) :
      print(format(triangle[i] [j], "<3"), end=" ")
  print()
