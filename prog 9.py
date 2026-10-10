english = int(input("total marks in english: "))
physics = int(input("total marks in physics: "))
chemistry = int(input("total marks in chemistry: "))
math = int(input("total marks in math: "))
comp_sc = int(input("total marks in computer science: "))

total = english+physics+chemistry+math+comp_sc
percentage = ((english+physics+chemistry+math+comp_sc)/500) * 100

print ("total marks= ", total)
print ("percentage is= ", percentage,"%")
