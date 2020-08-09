"""
封装自己的数组
"""

class Arrays:

    def __init__(self,arr=None,capacity=10):

        #判断arr是否是列表类型
        if isinstance(arr,list):
            self.data =arr[:]
            self.size = len(arr)
            return
        self.data = [None]*capacity
        self.size = 0

    #获取数组中元素个数
    def getSize(self):
        return self.size

    #获取数组的容量
    def getCapacity(self):
        return len(self.data)

    #返回数组是否为空
    def is_empty(self):
        return self.size == 0

