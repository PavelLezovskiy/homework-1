my_dict = {'Victor': 1998, 'Natasha': 1995, 'Oleg': 1972}
print(my_dict)
print(my_dict['Natasha'])
my_dict['Pavel'] = 1980
print(my_dict['Pavel'])
my_dict.update({'Nikita': 1991,
               'Sasha': 1990})
del my_dict['Victor']
print(my_dict.get('Voctor'))
print(my_dict)

my_set = {1, 2, 3, True, 'Apple'}
print(my_set)
print(my_set.add(5))
print(my_set.add('Logo'))
print(my_set.remove(1))
print(my_set)
