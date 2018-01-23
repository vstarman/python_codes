class Node(object):
    """节点类"""
    def __init__(self, elem=-1, left_child=None, right_child=None):
        self.elem = elem
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree(object):
    """二叉树"""
    def __init__(self, root=None):
        """构造根节点"""
        self.root = root

    def add(self, elem):
        """添加子节点"""
        node = Node(elem)
        # 如果根节点为空,则对根节点赋值
        if self.root == Node:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            # 对已有节点层次遍历
            while queue:
                # 弹出队列第一个元素
                cur = queue.pop(0)
                if cur.left_child == None:
                    cur.left_child = node
                    return
                elif cur.right_child == None:
                    cur.right_child = node
                    return
                else:
                    # 如果左右子树都不为空,加入队列继续判断
                    queue.append(cur.right_child)
                    queue.append(cur.left_child)


if __name__ == '__main__':
    b_tree = BinaryTree(root='祖先')
    b_tree.add('祖父')
    b_tree.add('祖母')
    b_tree.add('外祖母')
    b_tree.add('外祖母')
