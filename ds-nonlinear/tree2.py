
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.root = None

    def add_child(self, child):
        self.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        if self.children:
            for child in self.children:
                self.print_tree(child)


    def build_tree(self, level, data):
        if level == 0 and data != "":
            if self.get_level() != 0:
                self.root = TreeNode(data)
            else:
                print("Level 0 parent already exists")
        if level == 1 and data != "":
            child = self.root(TreeNode(data))
        elif level == 2 and data != "":
            child = self.root(TreeNode(data))
