class Node(object):
    """双向链表节点"""
    def __init__(self, item):
        # 保存元素
        self.item = item
        # 保存下一个节点引用
        self.next = None
        # 保存上一个节点引用
        self.pre = None
        

class DoubleLinkList(object):
    """双向循环列表"""
    def __init__(self):
        """初始化节点"""
        # 头节点指向
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        # 从头节点开始遍历
        # 定义游标(索引),指向头节点
        cur = self.__head
        while cur is not None:
            # 输出当前节点
            print(cur.item)
            # 指向下一个节点
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        # 创建新节点
        node = Node(item)
        if self.is_empty():
            # 如果是空链表,将head指向node
            pass
        else:
            # 将node的next指向head头节点
            node.next = self.__head
            # 将head头节点pre指向node
            self.__head.pre = node
        # __head指向该节点
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        # 创建节点,保存元素
        node = Node(item)
        # 如果是空链表,直接把元素添加到头部
        if self.is_empty():
            self.add(item)
        # 遍历,找到尾节点
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 当循环结束,cur指向尾节点
            node.pre = cur
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        assert pos >= 0, 'Index out of range, maybe you can use add()'
        assert pos <= (self.length() - 1), 'Index out of range, maybe you can use append()'
        cur = self.__head
        node = Node(item)
        index = 0
        # 移动到指定位置的前一个位置
        while index < (pos - 1):
            index += 1
            cur = cur.next
        # 建立node的前后连接
        node.prev = cur
        node.next = cur.next
        # 修改前后两个节点的指向
        cur.next.pre = node
        cur.next = node

    def remove(self, item):
        """删除节点,成功返回True,失败返回False"""
        # 定义遍历的节点
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                # 如果第一个就是要删除的元素
                if cur == self.__head:
                    # 将头指针指向后一个节点
                    self.__head = cur.next
                else:
                    # 删除cur节点
                    cur.pre.next = cur.next
                    # 如果存在下一个节点
                    if cur.next:
                        cur.next.pre = cur.pre
                return True
            else:
                # 当前节点
                cur = cur.next
        return False

    def search(self, item):
        """查找节点是否存在, 如果有返回索引, 否则返回False"""
        cur = self.__head
        index = 0
        while cur is not None:
            if cur.item == item:
                return index
            index += 1
            cur = cur.next
        return False


if __name__ == '__main__':
    link_list = DoubleLinkList()
    print('-'*10, '是否为空')
    print(link_list.is_empty())
    print('-'*10, '添加')
    link_list.add(1)
    link_list.add(2)
    print('-' * 10, '是否为空')
    print(link_list.is_empty())
    print('-'*10, '遍历')
    link_list.travel()
    print('-'*10, '链表长度')
    print(link_list.length())
    print('-'*10, '尾部添加')
    link_list.append('哈哈')
    link_list.travel()
    print('-'*10, '指定位置添加元素')
    link_list.insert(2, '第三个元素')
    link_list.travel()
    print('-' * 10, '删除节点')
    print(link_list.remove(2))
    link_list.travel()
    print('-' * 10, '删除节点')
    print(link_list.remove(2))
    link_list.travel()
    print('-' * 10, '搜索元素')
    print(link_list.search(2))
