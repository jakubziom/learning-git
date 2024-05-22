numbers_divided_by5=[]
numbers_divided_by5_power_of_3=[]

for i in range(0,100):
    if i%5 ==0:
        numbers_divided_by5.append(i)
        numbers_divided_by5_power_of_3.append(i**3)

print(numbers_divided_by5)
print(numbers_divided_by5_power_of_3)