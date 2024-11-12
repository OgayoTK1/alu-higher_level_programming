
>>> my_list = _import_('1-my_list').MyList

>>> my_list_obj = my_list()

>>> my_list_obj.append(5)
>>> my_list_obj.append(900)
>>> my_list_obj.append(59)
>>> my_list_obj.append(500)
>>> my_list_obj.append(51)
>>> my_list_obj.append(-59)
>>> my_list_obj.append(500)
>>> my_list_obj.append(-51)

[5, 900, 59, 500, 51, -59, 500, -51]

# Ensure no return value from print_sorted
>>> result = my_list_obj.print_sorted()
[-59, -51, 5, 51, 59, 500, 500, 900]

# Check with an empty list
>>> my_list_obj = my_list()
>>> my_list_obj.print_sorted()
[]
