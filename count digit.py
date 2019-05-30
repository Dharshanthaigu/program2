def number_digit(a):
  c=0
  for i in a:
    if(i.isdigit()):
      c+=1
  print(c)
b=input()
n=number_digit(b)
