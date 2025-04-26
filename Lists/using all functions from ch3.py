random_list=['jammy','millennia','life','best','horizontal','fred','ramanand','what','digital','spider_land','emotional','yamuna','brahmaputra']

print(f'accessing first element of list {random_list[0]}')

print(f'full list is {random_list}')

print(f'item number 3,5,8 from list are respectively {random_list[4]},{random_list[6]},{random_list[9]}')

random_list.append("mr.lokesh")

print(f'now lets add new member in the end mr.lokesh.so,now the new list will be \n{random_list} ')

del(random_list[2])
print(f'lets remove element 3 from the list now the list is \n{random_list}')

random_list[-1]= 'life'
print(f'now we have replaced mr.lokesh with life.So the list becames \n{random_list}')

random_list.remove('fred')
print(f'we will remove fred from list.So the list becomes \n{random_list}')