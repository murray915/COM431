class TreeNode:
    def __init__(self, data, desc):
        self.data = data
        self.children = []
        self.desc = desc
        self.parent = None

    def add_child(self, child: object):
        """ add child obj to self list"""
        child.parent = self
        self.children.append(child)
        
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

    def get_child_data(self, lvl2=None, lvl3=None) -> list:
        """ return child data & desc as list, input path lvl names """
        output_list = []

        for i in self.children:

            if lvl2 is None:
                print(i.data,i.desc)
                output_list.append([i.data,i.desc])

            # level 2 depth
            if i.data == lvl2:                
                for j in i.children:
                    
                    if lvl3 is None:
                        output_list.append([j.data,j.desc])
                    else:
                        # level 3 depth
                        if j.data == lvl3:
                            for k in j.children:
                                output_list.append([k.data,k.desc])
        
        return output_list

def get_main_menu(treenode: object) -> list:
    """ get the main menu options from treenode input """
    main_menu = []

    # get main menu options
    for i in treenode.children:
        main_menu.append([i.data, i.desc])

    return main_menu


def build_menu_tree():
    root = TreeNode("Main Menu","-")

    # depth 2 menu option
    # task 1
    submenu1 = TreeNode("Add Point of Interest","User input to create new Point of Interest")
    submenu1.add_child(TreeNode("Add Point of Interest","User input for Point of Interest, required fields & data to be followed"))
    submenu1.add_child(TreeNode("Add random Point of Interest data","User input number of random Point of Interest data records to be added"))
    submenu1.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu1)

    # depth 2 menu option
    # task 2 & 4
    submenu2 = TreeNode("Search for Point of Interests","Search for existing Points of Interest (POI) in applicaiton")
    submenu2.add_child(TreeNode("Manual input search - Strict by name","User input (case sensitive optional, fuzzy search off) search for POI"))
    submenu2.add_child(TreeNode("Manual input search - Fuzzy by name","User input (case & space non-sensitve, fuzzy search on) search for POI"))
    submenu2.add_child(TreeNode("Search by Point of Interest ID","User input (number input) search for POI by ID"))
    submenu2.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu2)

     # depth 2 menu option
     # task 3
    submenu3 = TreeNode("Display all Points of Interest","Display all Points of Interest (POIs) - ASC or DESC")
    submenu3.add_child(TreeNode("Display POIs by ascending order (a-z, 0-9)","-"))
    submenu3.add_child(TreeNode("Display POIs by descending order (z-a, 9-0)","-"))
    submenu3.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu3)   

    # depth 2 menu option
    # task 5
    submenu4 = TreeNode("Delete Point of Interest","Search for existing Points of Interest (POI) in applicaiton to delete")
    submenu4.add_child(TreeNode("Manual input search - Strict","User input (case & space sensitive) search for POI - then delete"))
    submenu4.add_child(TreeNode("Manual input search - Fuzzy","User input (case & space non-sensitve) search for POI - then delete"))
    submenu4.add_child(TreeNode("Search by Point of Interest ID","User input (number input) search for POI by ID"))
    submenu4.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu4)

    # depth 2 menu option
    # task 6
    submenu5 = TreeNode("Save and Load Points of Interest from file","Save or load any created Points of Interest files, user defined location or default")
    submenu5.add_child(TreeNode("Save to automatic location","Save file to local directory './data' with user input filename ; path is determined automatically"))
    submenu5.add_child(TreeNode("Save to user input location","Save file to local directory; determined by user folderpath input & filename"))
    submenu5.add_child(TreeNode("Load data from existing file - user selection","Load from user specified file (determined by user filename & folderpath)"))
    submenu5.add_child(TreeNode("Load data from existing file - example dev data","Load from developer example data file(s) (file list determined automatically)"))
    submenu5.add_child(TreeNode("View json file structure","Load from user input path, and print to screen json structure"))
    submenu5.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu5)

    # depth 2 menu option
    # task 7
    submenu6 = TreeNode("Questions and Answers for Points of Interest","Add and answer questions on Points of Interest (POI)")
    submenu6.add_child(TreeNode("Add question to Point of Interest","User input search for POI, then add question to be answered"))
    submenu6.add_child(TreeNode("Add answer to Point of Interest","User input search for POI, then add answer to question(s) in order that they were created for that POI"))
    submenu6.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu6)

    # depth 2 menu option
    # task 8
    submenu7 = TreeNode("Router from Point of Interest to Point of Interest","Input user Point of Interest (POI) for Cariff Data, and input for destination location and all locations required to go to on the way")
    submenu7.add_child(TreeNode("View Full Cardiff Points of Interest List","Display the full points of interests for Cardiff to travel between"))
    submenu7.add_child(TreeNode("Travel between Points of Interest","Input user Point of Interest (POI) for Cariff Data, FROM and TO. Return the distance and locations between"))
    submenu7.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu7)

    # depth 2 menu option
    # additional functionality - show menu descriptions
    submenu8 = TreeNode("View Menu option descriptions","Descriptions of each sub menu within program")
    submenu8.add_child(TreeNode("View Menu Descriptions","Output table of sub menu options and their respective descriptions"))
    submenu8.add_child(TreeNode("View Menu Tree","Print the full menu tree with all sub options"))
    submenu8.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu8)

    # depth 2 menu option
    # additional functionality - demo runs
    submenu9 = TreeNode("Demonstration of Data Structures and Algorithms","Outputs of Data Structures & Algorithms implemented within program. All output data is example non-POI")

    # depth 3 menu option
    # demo runs - Sorting algorithms
    submenu_algs = TreeNode("Sorting algorithms","Run example data through all implemented sorting algorithms")
    submenu_algs.add_child(TreeNode("Bubble Sort","Run example data through Bubble Sort algorithm, printing process steps")) 
    submenu_algs.add_child(TreeNode("Merge sort","Run example data through Merge sort Sort algorithm, printing process steps"))
    submenu_algs.add_child(TreeNode("Quicksort","Run example data through Quicksort Sort algorithm, printing process steps"))   
    submenu_algs.add_child(TreeNode("Algorithm sort tester","Run all algorithms over time with increasing data, to see visually the process speed"))     
    submenu_algs.add_child(TreeNode("Return","Return to Main Menu"))
    submenu9.add_child(submenu_algs)

    # depth 3 menu option
    # demo runs - Sorting algorithms
    submenu_data_stc = TreeNode("Data Structures","Run example data through data all implemented structures")
    submenu_data_stc.add_child(TreeNode("Queue","Run example data through Queue data strucutre, printing process steps")) 
    submenu_data_stc.add_child(TreeNode("Stack","Run example data through Queue data strucutre, printing process steps"))
    submenu_data_stc.add_child(TreeNode("Muti branch Tree","Run example data through Queue data strucutre, printing process steps"))
    submenu_data_stc.add_child(TreeNode("Return","Return to Main Menu"))
    submenu9.add_child(submenu_data_stc)

    submenu9.add_child(TreeNode("Return","Return to Main Menu"))
    root.add_child(submenu9)


    submenu10 = TreeNode("Exit","Exit program")
    root.add_child(submenu10)

    return root