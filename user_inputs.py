def display_options_retur(all_options: list, title:str, type: str, posit: str) -> str | bool:
    """
    query_rows: must consist of two values - id and description i.e. the category_id and category_description.
    title: is some text to put above the list of options to act as a title.
    type: is used to customise the prompt to make it appropriate for what you want the user to select.
    posit; this is the sql column poss. (index 1 - pos 0 is line sequce)

    return. posit of the input data option
    """
    try:
        option_num = 1
        option_list = []

        print("\n",title,"\n")

        for option in all_options:
            code = option[0]
            desc = option[1]

            print("{0}.\t{1}".format(option_num, desc))
            
            option_num = option_num + 1
            option_list.append(code)

        selected_option = 0

        while selected_option > len(option_list) or selected_option == 0:
            
            prompt = input("\nEnter the number against the "+type+" you want to choose: ")
            
            if not prompt.isnumeric():
                print(f'\n* ERROR * : Please enter only numbers (int) ')

            elif int(prompt) > len(option_list):
                print(f'\n* ERROR * : Please enter a number within the list')

            else:
                selected_option = int(prompt)

        # return tuple position from input data
        for i in range(0, len(all_options)+1):
            men_op = all_options[i][0]
            if men_op == selected_option:
                selected_option_tar_pos = all_options[i][int(posit)]
                break

        return selected_option_tar_pos
    
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} ** \n\n")
        return False
    

def welcome_screen() -> None:
    """Input data, first name / surname printout"""
    print(
            '\n'
            '-------------------------------------'
            '\n'
            '        Welcome to Paraná            '
            '\n'
            '-------------------------------------'
            )

def exit_screen() -> None:
    """"exit screen, printout"""
    print(
        '\n'
        '-------------------------------------'
        '\n'
        '----- Thank you for shopping at -----'
        '\n'
        '-------------------------------------'
        '\n'
        '-------------- Paraná ---------------'
        '\n'
        '-------------------------------------'
        '\n'
        )