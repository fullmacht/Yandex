n = [9,2,3,4,5]
value_list = []
index = list(range(len(n)))
abs_list = []
index_list = []
j = 0
for i in index:
    value_list = []
    j = 0
    j+=2+i
    if n[i] != None:
        for m in n[i:]:
            value_list.append(m)
# я убрал одиночные значения так как в задании была сумма непустого подотрезка
            if len(value_list)!=1:
                abs_value= abs(sum(value_list))
                index_slice = [i,j]
                j += 1
# для записи значений словарь не подходил так как заменял одинаковые значения поэтому
# пришлось использовать список
                abs_list.append(abs_value)
                index_list.append(index_slice)
slice = index_list[abs_list.index(min(abs_list))]
print(n[slice[0]:slice[1]])


