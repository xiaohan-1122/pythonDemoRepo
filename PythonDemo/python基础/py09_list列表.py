#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo
# @File: py09_list列表.py
# @Author: xiaohanzhang
# @Data: 2020/8/11

# list里面的元素的数据类型也可以不同，开发过程中尽量存储相同类型数据
list = ["hahah", 1, ['a', 'd'], True]

# 下标
name_list = ["小红", "小蓝", "小绿"]
print(name_list)
print(name_list[1])
# 把某个元素替换成别的元素
name_list[1] = '小白'
print(name_list)

list1 = ['a', 'b', 'c', 'a']
# 1.index(数据) 获取元素下标,如果元素不在列表中，会抛异常
list1.index('c')    # 2

# 2.count(数据) 统计指定数据在当前列表中出现的次数
list1.count('a')    # 2

# 3.len(列表) 列表的长度,即列表中数据的个数
len(list1)  # 4

# 4. in 判断指定数据在列表中是否存在，存在True，不存在False
print('b' in list1)    # True

# 5. not in 判断指定数据不在列表中是否存在，不在True，在False
print('aa' not in list1)    # True

# 6. append(数据) 列表结尾添加指定数据
list1.append("d")
print(list1)    # ['a', 'b', 'c', 'a', 'd']

# 7.extend() 列表结尾追加数据，如果追加数据是一个序列，则将这个序列的数据逐一添加到列表
list1.extend('a')
print(list1)    # ['a', 'b', 'c', 'a', 'd', 'a']
list1.extend('ee')
print(list1)    # ['a', 'b', 'c', 'a', 'd', 'a', 'e', 'e']
list2 = ["fff", "ggg"]
list1.extend(list2)
print(list1)    # ['a', 'b', 'c', 'a', 'd', 'a', 'e', 'e', 'fff', 'ggg']

# 8. insert(index, 数据) 指定位置添加数据
list1.insert(1, "e")
print(list1)    # ['a', 'e', 'b', 'c', 'a', 'd', 'a', 'e', 'e', 'fff', 'ggg']

print('*' * 50)

# 9. del 将变量从内存中删除
del list1[9]
print(list1)    # ['a', 'e', 'b', 'c', 'a', 'd', 'a', 'e', 'e', 'ggg']
del name_list
# print(name_list)    # NameError: name 'name_list' is not defined

# 10. pop() 删除指定下标的数据，不写下标默认删除末尾的元素，会返回被删除的数据
a = list1.pop()     # ggg
print(list1)    # ['a', 'e', 'b', 'c', 'a', 'd', 'a', 'e', 'e']
b = list1.pop(1)    # e
print(list1)    # ['a', 'b', 'c', 'a', 'd', 'a', 'e', 'e']

# 11.remove(数据) 删除指定数据，数据不存在会报错
list1.remove('d')
print(list1)    # ['a', 'b', 'c', 'a', 'a', 'e', 'e']

# 12. clear() 清空列表
list1.clear()
print(list1)    # []
print('*' * 50)

list1 = [2, 1, 3]
# 13. 反转数组
list1.reverse()
print(list1)    # [3, 1, 2]

# 14. 排序
list1.sort()  # 升序排列
print(list1)    # [1, 2, 3]
list1.sort(reverse=True)    # 降序排列
print(list1)    # [3, 2, 1]

# 15. copy() 复制列表
list2 = list1.copy()
print(list2)    # [3, 2, 1]
print('')

# 列表的遍历 while
names = ['大王', '八戒', '白骨精']
i = 0
while i < len(names):
    print(names[i])
    i += 1
print('*' * 50)

# 列表的遍历 for
for name in names:
    print(name)
print('*' * 50)

for i in range(len(names)):
    print(names[i])
print('*' * 50)

for i in enumerate(names):
    print(i)
    """
    (0, '大王')
    (1, '八戒')
    (2, '白骨精')
    """
for index, item in enumerate(names):
    print(f'下标是{index}的元素是{item}')
    '''
    下标是0的元素是大王
    下标是1的元素是八戒
    下标是2的元素是白骨精
    '''

# 列表相加 +=相当于调用extend()方法
list1 = [1, 2, 3]
list2 = [4, 5]
list3 = list1 + list2
print(list3)    # [1, 2, 3, 4, 5]

print(list3 * 2)


# 列表嵌套
list5 = [['a', 'b'], ['小白', '小黑'], [1, 9]]
# 获取'小白'
name = list5[1][0]
print(name)     # 小白