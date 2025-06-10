class TreeNode:
    def __init__(self, data, desc):
        self.data = data
        self.children = []
        self.desc = desc
        self.parent = None

    def get_level(self):
        """ get level of child list """
        level = 0
        p = self.parent

        # print out level
        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree_level(self, level: int):
        """ print tree at input level """
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        # recursion of tree to print all
        if self.children:
            for child in self.children:
                child.print_tree_level(level)    


    def print_tree(self):
        """ print whole tree """
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        # recursion of tree to print all
        if self.children:
            for child in self.children:
                child.print_tree()


    def add_child(self, child: object):
        """ add child obj to self list"""
        child.parent = self
        self.children.append(child)


    def get_child_data(self, lvl2: str, lvl3=None):
        """ return child data & desc, input path lvl names """
        output_list = []

        for i in self.children:
            # level 2 depth
            if i.data == lvl2:
                for j in i.children:
                    
                    if lvl3 is None:
                        output_list.append(j.data + "," + j.desc)
                    else:
                        # level 3 depth
                        if j.data == lvl3:
                            for k in j.children:
                                output_list.append(k.data + "," + k.desc)
        
        return output_list


def build_product_tree():
    root = TreeNode("Electronics","n/a")

    laptop = TreeNode("Laptop","n/a")
    laptop.add_child(TreeNode("Mac","n/a"))
    laptop.add_child(TreeNode("Surface","n/a"))
    laptop.add_child(TreeNode("Thinkpad","n/a"))
    root.add_child(laptop)

    cellphone = TreeNode("Cell Phone","n/a")
    cellphone.add_child(TreeNode("iPhone","n/a"))
    cellphone.add_child(TreeNode("Google Pixel","n/a"))
    cellphone.add_child(TreeNode("Vivo","n/a"))
    root.add_child(cellphone)

    tv = TreeNode("TV","n/a")
    tv.add_child(TreeNode("Samsung","n/a"))
    tv.add_child(TreeNode("LG","n/a"))
    root.add_child(tv)

    keyboard = TreeNode("keyboard","n/a")
    keyboard.add_child(TreeNode("razor","n/a"))
    keyboard.add_child(TreeNode("steelseries","n/a"))
    laptop.add_child(keyboard)   

    return root


if __name__ == '__main__':
    rootnode = build_product_tree()
    
    print(rootnode.get_child_data("Laptop","keyboard"))
    print(rootnode.get_child_data("Laptop"))

