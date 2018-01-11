class Node(object):
    """单链表节点"""
    def __init__(self, item):
        # 保存元素
        self.item = item
        # 保存下一个节点引用
        self.next = None
        

class SinCycLinkList(object):
    """单项循环列表"""
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
        if self.is_empty():
            return 0
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        # 从头节点开始遍历
        # 定义游标(索引),指向头节点
        cur = self.__head
        print(cur.item)
        while cur.next != self.__head:
            # 指向下一个节点
            cur = cur.next
            # 输出当前节点
            print(cur.item)

    def add(self, item):
        """链表头部添加元素"""
        # 创建新节点
        node = Node(item)
        if self.is_empty():
            # 空链表,创建一个自己指向自己的节点
            self.__head = node
            node.next = node
        else:
            # 添加节点指向__head
            node.next = self.__head
            # 循环遍历,将最后节点next指向head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            # __head指向该节点
            self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        # 创建节点,保存元素
        node = Node(item)
        # 如果是空链表,直接把元素添加到
        if self.is_empty():
            self.add(item)
        # 遍历,找到尾节点
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 当循环结束,cur指向尾节点
            cur.next = node
            # 将node指向头节点_head
            node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素"""
        assert pos >= 0, 'Index out of range, 请你丫的再输小一点'
        assert pos <= (self.length()-1), 'Index out of range, 请你丫的输小一点'
        cur = self.__head
        # 定义下标
        index = 0
        while index < (pos-1):
            index += 1
            cur = cur.next
        # 循环结束,cur指向pos的上一个节点
        node = Node(item)
        node.next = cur.next
        cur.next = node

    def remove(self, item):
        """删除节点,成功返回True,失败返回False"""
        if self.is_empty():
            return False
        # 定义遍历的节点
        cur = self.__head
        # 定以前一个节点,用来修改next指向
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                # 如果第一个就是要删除的元素
                if not pre:
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 将头指针指向后一个节点
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间结点
                    pre.next = cur.next
                return True
            else:
                # 前一个节点
                pre = cur
                # 当前节点
                cur = cur.next
        return False

    def search(self, item):
        """查找节点是否存在, 如果有返回索引, 否则返回False"""
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return 0
        index = 0
        while cur.next != self.__head:
            # print(cur.item, item)
            if cur.item == item:
                return index
            index += 1
            cur = cur.next
        # 最后一个原色会跳过,再判断一次
        if cur.item == item:
            return index
        return False


if __name__ == '__main__':
    link_list = SinCycLinkList()
    print('-'*10, '是否为空')
    print('-'*10, link_list.is_empty())
    print('-'*10, '添加')
    link_list.add(1)
    link_list.add(2)
    link_list.add(3)
    print('-'*10, link_list.is_empty())
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
    link_list.remove(2)
    link_list.travel()
    print('-' * 10, '删除节点')
    link_list.remove(2)
    link_list.travel()
    print('-' * 10, '搜索元素')
    print(link_list.search('哈哈'))
