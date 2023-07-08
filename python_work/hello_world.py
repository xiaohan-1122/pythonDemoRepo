print('hello python world!')

current_users = ['admin', 'Cangguan', 'BaJie']
new_users = ['WUJING', 'Admin', 'Cangguan']

users = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in users:
        print('这个名字重复了')
    else:
        print('OK 不重复')

        
