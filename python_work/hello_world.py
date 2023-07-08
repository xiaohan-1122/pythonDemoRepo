print('hello python world!')


# 列表推导式 格式: [xxx for xxx in range() 条件]
squares = [value ** 2 for value in range(1,11)]
print(squares)

nums = []
for n in range(21):
    if n % 2 == 1:
        nums.append(n)
print(nums)

nums2 = [n for n in range(21) if n % 2 == 1]
print(nums2)

names = ['a', 'b', 'c', 'd', 'e']
print(names[1:3])   # 下标1开始取到下标3之前的元素 ['b', 'c']
print(names[:3])    # 默认从0开始 ['a', 'b', 'c']
print(names[2:])    # 默认取到最后一位 ['c', 'd', 'e']
print(names[-3:])   # 取列表最后3个元素 ['c', 'd', 'e']
# 遍历列表中部分元素时，可以使用切片
# 遍历列表最后三个元素
for name in names[-3:]:
    print(name)
