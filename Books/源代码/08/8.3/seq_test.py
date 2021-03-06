# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
def check_key (key):
    '''
    该函数将会负责检查序列的索引，该索引必须是整数值，否则引发TypeError
    且程序要求索引必须为非负整数，否则引发IndexError
    '''
    if not isinstance(key, int): raise TypeError('索引值必须是整数')
    if key < 0: raise IndexError('索引值必须是非负整数')
    if key >= 26 ** 3: raise IndexError('索引值不能超过%d' % 26 ** 3)   
class StringSeq:
    def __init__(self):
        # 用于存储被修改的数据
        self.__changed = {}
        # 用于存储已删除元素的索引
        self.__deleted = []
    def __len__(self):
        return 26 ** 3
    def __getitem__(self, key):
        '''
        根据索引获取序列中元素
        '''
        check_key(key)
        # 如果在self.__changed中找到已经修改后的数据
        if key in self.__changed :
            return self.__changed[key]
        # 如果key在self.__deleted中，说明该元素已被删除
        if key in self.__deleted :
            return None
        # 否则根据计算规则返回序列元素
        three = key // (26 * 26)
        two = ( key - three * 26 * 26) // 26
        one = key % 26
        return chr(65 + three) + chr(65 + two) + chr(65 + one) 
    def __setitem__(self, key, value):
        '''
        根据索引修改序列中元素
        '''
        check_key(key)
        # 将修改的元素以key-value对的形式保存在__changed中
        self.__changed[key] = value
    def __delitem__(self, key):
        '''
        根据索引删除序列中元素
        '''
        check_key(key)
        # 如果__deleted列表中没有包含被删除key，添加被删除的key
        if key not in self.__deleted : self.__deleted.append(key)
        # 如果__changed中包含被删除key，删除它
        if key in self.__changed : del self.__changed[key]
# 创建序列
sq = StringSeq()
# 获取序列的长度，实际上就是返回__len__()方法的返回值
print(len(sq))
print(sq[26*26])
# 打印没修改之后的sq[1]
print(sq[1]) # 'AAB'
# 修改sq[1]元素
sq[1] = 'fkit'
# 打印修改之后的sq[1]
print(sq[1]) # 'fkit'
# 删除sq[1]
del sq[1]
print(sq[1]) # None
# 再次对sq[1]赋值
sq[1] = 'crazyit'
print(sq[1]) # crazyit
