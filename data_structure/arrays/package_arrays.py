"""
��װ�Լ�������
"""

class Arrays:

    def __init__(self,arr=None,capacity=10):

        #�ж�arr�Ƿ����б�����
        if isinstance(arr,list):
            self.data =arr[:]
            self.size = len(arr)
            return
        self.data = [None]*capacity
        self.size = 0

    #��ȡ������Ԫ�ظ���
    def getSize(self):
        return self.size

    #��ȡ���������
    def getCapacity(self):
        return len(self.data)

    #���������Ƿ�Ϊ��
    def is_empty(self):
        return self.size == 0

