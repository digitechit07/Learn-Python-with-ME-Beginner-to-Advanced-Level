def num_23():
    user_input = input('enter the name of a nursery rhyme: ')
    print(len(user_input))         # To get the length of the title or name of the nursery rhyme
    #
    start_num = int(input("Enter a starting number: "))
    end_num = int(input("Enter an ending number: "))
    print(user_input[start_num:end_num])  # To slice from the rhyme name based on the user's input


num_23()






