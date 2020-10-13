#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Software: PythonDemo1
# @File: py_05_list.py
# @Author: xiaohanzhang
# @Data: 2020/8/11

# list里面的元素的数据类型也可以不同
list = ["hahah", 1, ['a', 'd'], True]

# 遍历
name_list = ["小红", "小蓝", "小绿"]
print(name_list)
for name in name_list:
    print(name)
print('*' * 50)

for i in range(len(name_list)):
    print(name_list[i])
print('*' * 50)

n = 0
while n < len(name_list):
    print(name_list[n])
    n += 1
print('*' * 50)

for i in enumerate(name_list):
    print(i)
    """
    (0, '小红')
    (1, '小蓝')
    (2, '小绿')
    """
for index, item in enumerate(name_list):
    print(f'小标是{index}的元素是{item}')

# 判断某个元素是否在列表中
if '小红' in name_list:
    print('小红在列表中')

if '小白' not in name_list:
    print('小白不在列表中')

list1 = ['a', 'b', 'c', 'a']

# list长度
len(list1)

# list中某个元素有几个
list1.count('a')

# 往list中追加元素到末尾
list1.append("d")

# 元素插入到指定的位置
list1.insert(1, "e")

# 将一个列表中元素增加到另一个列表中
list2 = ["ff", "gg"]
list1.extend(list2)
print(list1)

# 把某个元素替换成别的元素
list1[1] = 'bb'

# 获取元素下标,如果元素不在列表中，会报错
list1.index('c')

# 删除list末尾的元素
list1.pop()

# 删除指定位置的元素
list1.pop(1)

# 删除指定元素，数据不存在会报错
list1.remove('d')

# 清空列表中的元素
list1.clear()

# 扩展：删除列表中指定下标元素 可以用del
list3 = ["aaa", "bbb", "ccc"]
del list3[0]

# del也可以将变量从内存中删除
# a = "aaa"
# del a

# 排序
list4 = ["zhangsan", "lisi", "wangwu"]
list4.sort()                # 升序排列
print(list4)
list4.sort(reverse=True)    # 降序排列
print(list4)

# 逆序（反转）
list3.reverse()

# 列表相加 +=相当于调用extend()方法
list1 = [1, 2, 3]
list2 = [4, 5]
list3 = list1 + list2
print(list3)    # [1, 2, 3, 4, 5]

print(list3 * 2)

# 复制列表
list4 = list1.copy()

# 列表嵌套
list5 = [['a', 'b'], ['小白', '小黑'], [1, 9]]
# 获取'小白'
name = list5[1][0]
print(name)