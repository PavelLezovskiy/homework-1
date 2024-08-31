immutable_var = tuple([True, 'coconut', 15,])
print(immutable_var)

#immutable_var.append('apple')
#print(immutable_var) т.к сама по себе структура кортежа не может быть изменена
mutable_list = [(1, 2, 3), 4]
print(mutable_list)
mutable_list[0] = 5
print(mutable_list)
