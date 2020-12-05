#!/usr/bin/env python3

#adding four fruits and their quantities
quantity_list = []
x = 0
while x < 4:
  a = int(input("please enter quantities of the good: "))
  quantity_list.append(a)
  x += 1

storage_dic = {"apples": quantity_list[0], "oranges": quantity_list[1], "watermelons": quantity_list[2], "bananas": quantity_list[3]}
print(storage_dic)
print("----------------------------------------------")

print("Adding existing items and also adding new items to storage")
while True:
  b = input("please enter fruit name and number quantities to add seperated by space: ")
  if b == "q":
    break
  else:
    c = b.split()
    fruit, quantity = c[0], c[1]
    for keys, values in storage_dic.items():
      if keys == fruit:
        storage_dic[keys] = int(quantity) + values
    if fruit not in storage_dic:
        storage_dic[fruit] = int(quantity)
print(storage_dic)
print("----------------------------------------------")


print("Subtracting existing items from the storage and also adding new items ")
while True:
  b = input("please enter fruit name and number quantities to add seperated by space: ")
  if b == "q":
    break
  else:
    c = b.split()
    fruit, quantity = c[0], c[1]
    for keys, values in storage_dic.items():
      if keys == fruit:
        if values - int(quantity) < 0:
          print("you are trying to remove more than what is in the storage")
        else:
          storage_dic[keys] = values - int(quantity)
    if fruit not in storage_dic:
        storage_dic[fruit] = int(quantity)
print(storage_dic)
print("----------------------------------------------")



f = input("please type total to get the total quantities of all goods in the storage: ")
if f == "total":
  sum = 0
  for keys, values in storage_dic.items():
    sum += values
  print(sum)
print("----------------------------------------------")




g = input("Please type finished to see finished goods: " )
if g == "finished":
  for keys, values in storage_dic.items():
    if values == 0:
      print(keys)






