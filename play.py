import logic

if __name__ == '__main__':
    mat = logic.start_game()
    
    while True:
        inpt = input("Press the command: ")
        if inpt == 'W' or inpt == 'w':
            mat, flag = logic.move_up(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'game not over':
                 logic.add_new_2(mat)
            else: break
        elif inpt == 's' or inpt == 's':
            mat, flag = logic.move_down(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'game not over':
                 logic.add_new_2(mat)
            else: break
        elif inpt == 'A' or inpt == 'a':
            mat, flag = logic.move_left(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'game not over':
                 logic.add_new_2(mat)
            else: break
        elif inpt == 'D' or inpt == 'd':
            mat, flag = logic.move_right(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'game not over':
                 logic.add_new_2(mat)
            else: break
        else:
            print("Invalid Key Pressed")
        logic.print_matrix(mat)
        