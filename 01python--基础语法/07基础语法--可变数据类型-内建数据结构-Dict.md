# Dict-字典
- 字典是一种没有顺序的组合数据，数据以键值对的形式出现
## Dict的创建
## Dict的特征
- 字典是序列类型，但是是无序序列，所以没有分片和索引
- 字典中的数据每个都有键值对组成，即k，v对
    - key：必须是可哈希的值，比如int，str，float，tuple，但是，list，set，dict不行
    - value：任何值
    - 可哈希:- [https://www.jianshu.com/p/bc5195c8c9cb]
             - 简单来说,不可变数据类型是可哈希的,可变数据类型是不可哈希的
## Dict的常见操作
- 1.访问数据 
    - d[key]
- 2.删除数据
    - del d[key]
- 3.成员检测
    - 注: 检测key, 不检测value
- 4.Dict遍历
- 5.Dict生成式
## Dict相关函数
- 1.通用函数
    - len(d)
    - 最值
        - max(dict,key=dict.get)
        - min(dict,key=dict.get) 
  2.str(d): 返回Dict的字符串格式
  3.d.clear(): 清空
  4.d.items(): 返回Dict的键值对组成的元组格式
  5.d.keys(): 返回Dict的key组成一个可迭代的结构
  6.d.values(): 同d.keys()
  7.d.get(key): 根据指定键返回相应的值，
        - 好处: 可以用来设置默认值
  8.fromkeys(l, value):使用指定的序列(例:l)作为key，使用一个value作为Dict的所有键的值
  