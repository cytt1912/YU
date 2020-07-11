
"""

可变数据类型：当该数据类型对应变量的值发生变化时，对应内存地址并没有开辟新的内存，而是在原来的内存值上进行修改。
列表、集合、字典都是属于可变数据类型

不可变数据类型：当该数据类型对应变量的值发生变化时，原来内存中的值不变，而是会开辟一块新的内存，变量指向新的内存地址。
元祖、字符串、整型、浮点型、布尔型都是不可变数据类型

"""

dict1 = {"k1":"v1"}
dict2 = {"k2":"v2"}

dict3 = dict1  #赋值仅对值进行引用，实际指向的还是dict1的内存地址，所以dict3更新，dict1也进行了更新
dict3.update(dict2)
print(dict1,dict3)
print(id(dict1),id(dict3))

import copy
#深浅copy
dict4 = {"k4":"v4"}
dict5 = {"k5":"v5"}

dict6 = copy.deepcopy(dict4)  #深copy后，dict6重新开辟了一个内存地址用来存储与dict4相同的值，下面dict6更新不影响dict4
dict6.update(dict5)
print(dict4,dict6)
print(id(dict4),id(dict6))
