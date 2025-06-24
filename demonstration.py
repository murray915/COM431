import random as rd
import time
import sorting_algs as algs
import queue_class as qc
import stack_class as sc
import menu_tree as mt

def get_data_arr(top_range = 15) -> list:
    """ return large random array ; input top random size """
    ori_list = []
    for _ in range(0, rd.randrange(10,top_range)):
        ori_list.append(rd.randrange(0,10000))

    return ori_list


def demo_sorting_algr(ori_list, print_cons, runset):
    """ demo sorting algr ; input sorting algr name """
    start_time = time.time()

    if print_cons:
        print("-----------------------------------------------------------------")
        print(f'Length of list: {len(ori_list)}, action on runset {runset}:\nOriginal list: \n {ori_list}')
        print(f"-----------------------------------------------------------------\n\n")

    try:
        # set runset as varible function
        func = getattr(algs, runset)

        # Call runset
        if "quicksort" in runset:
            func(ori_list, 0, len(ori_list) -1, print_cons)
        else:
            func(ori_list, print_cons)
            
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")

    if print_cons:
        print(f'----------------------------------------------------------------- \nFinal Output value list: \n {ori_list}')
        print("  --- Run completed in %s seconds ---" % (time.time() - start_time))
        print("-----------------------------------------------------------------")

def demo_stack_data_type():
    """ demo sorting algr ; input sorting algr name """
    demo_stack = sc.Stack()

    print(f'Demo for Stack, random add / remove actions and results')

    for _ in range(1, rd.randrange(2,8)):
        num = rd.randrange(1,8)        
        print(f'\tadd to stack {num}')
        demo_stack.stack_add(num)

    for _ in range(1, rd.randrange(2,5)):      
        print(f'\tremove from stack')
        demo_stack.stack_remove()

    demo_stack.print_queue()
    

def demo_queue_data_type():
    """ demo sorting algr ; input sorting algr name """
    demo_que = qc.Queue(8)

    print(f'Demo for queue, random enqueue / dequeue actions and results')

    for _ in range(1, rd.randrange(2,8)):
        num = rd.randrange(1,8)        
        print(f'\tadd to queue {num}')
        demo_que.enqueue(num)

    for _ in range(1, rd.randrange(2,5)):      
        print(f'\tdequeue')
        demo_que.dequeue()

    demo_que.print_queue()

def build_product_tree_demo_001():
    root = mt.TreeNode("Electronics","All items within electronics")

    # depth 2 menu option
    laptop = mt.TreeNode("Laptop","Laptop Brands selection")
    laptop.add_child(mt.TreeNode("Mac","Apple laptop"))
    laptop.add_child(mt.TreeNode("Surface","Surface laptop"))
    laptop.add_child(mt.TreeNode("Thinkpad","Thinkpad, notepad"))
    root.add_child(laptop)

    # depth 3 menu option
    # Sub menu
    keyboard = mt.TreeNode("keyboard","Keyboard Brands selection")
    keyboard.add_child(mt.TreeNode("razor","Razor brand keyboards"))
    keyboard.add_child(mt.TreeNode("steelseries","Steelseries brand keyboards"))
    laptop.add_child(keyboard)   

    # depth 2 menu option
    cellphone = mt.TreeNode("Cell Phone","Phone Brands selection")
    cellphone.add_child(mt.TreeNode("iPhone","iPhone (mac) phone"))
    cellphone.add_child(mt.TreeNode("Google Pixel","Google (android) phone"))
    cellphone.add_child(mt.TreeNode("Vivo","Vivo (android) phone"))
    root.add_child(cellphone)

    # depth 2 menu option
    tv = mt.TreeNode("TV","TV Brands selection")
    tv.add_child(mt.TreeNode("Samsung","Samsung TVs import"))
    tv.add_child(mt.TreeNode("LG","LG TVs import"))
    root.add_child(tv)

    return root

def build_product_tree_demo_002():
    root = mt.TreeNode("Menu Option","n/a")

    # depth 2 menu option
    laptop = mt.TreeNode("Sub Menu 1","n/a")
    laptop.add_child(mt.TreeNode("Option 1","Descript - 1"))
    laptop.add_child(mt.TreeNode("Option 2","Descript - 2"))
    laptop.add_child(mt.TreeNode("Option 3","Descript - 3"))
    root.add_child(laptop)

    # depth 3 menu option
    # Sub menu
    keyboard = mt.TreeNode("Sub sub-menu ","n/a")
    keyboard.add_child(mt.TreeNode("Option 1","Descript - 1"))
    keyboard.add_child(mt.TreeNode("Option 2","Descript - 2"))
    laptop.add_child(keyboard)   

    # depth 2 menu option
    cellphone = mt.TreeNode("Sub Menu 2","n/a")
    cellphone.add_child(mt.TreeNode("Option 1","Descript - 2"))
    cellphone.add_child(mt.TreeNode("Option 2","Descript - 2"))
    cellphone.add_child(mt.TreeNode("Option 3","Descript - 2"))
    root.add_child(cellphone)

    return root

    
def demo_menu_tree():
    """ demo tree menu """
    rootnode002 = build_product_tree_demo_002()
    rootnode001 = build_product_tree_demo_001()

    print('')
    rootnode001.print_tree()
    print('')
    rootnode002.print_tree()
    print('')

    output = rootnode001.get_child_data("Laptop")

    print(f'"Laptop" sub-menu option & description print ; returned data as list -> \n\n{output}\n\nReturned menu option & Desc for menu printouts to users :')
    for i in output:
        print(f'\tMenu Option : {i[0]} \t\tmenu description : {i[1]}')
    
    print('')





#runset = 'quicksort'
#runset = 'merge_sort'
#runset = 'bubble_sort'
#print_cons = True
#ori_list = get_data_arr()

#demo_sorting_algr(ori_list, print_cons, runset)
#demo_queue_data_type()
#demo_stack_data_type()
#demo_menu_tree()