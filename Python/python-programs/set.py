# set 集合

set_1 = {'apple', 'orange', 1, 'pear', 'organze', 'banana'}
set_2 = {'apple', 'orange', 2, 'pear', 'watermelon'}


Intersection = set_1 & set_2  # 交集
Union = set_1 | set_2  # 并集

Substract_1 = set_1 - set_2
Substract_2 = set_2 - set_1

only = set_1 ^ set_2

print(Intersection, Union, Substract_1, Substract_2, only)
