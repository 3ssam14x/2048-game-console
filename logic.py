import random

def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    print("commands are as follows: ")
    print("'W' or 'w' : moves up\n'S' or 's' : movies down\n'A' or 'a' : moves left\n'D' or 'd' : moves right")

    add_new_2(mat)
    print_matrix(mat)
    return mat

def add_new_2(mat):
    
    def check_adding_new_2(mat):
        for row in range(4):
            for col in range(4):
                if mat[row][col] == 0: return True
        return False
    
    if not check_adding_new_2(mat): return
    
    row = random.randint(0,3)
    col = random.randint(0,3)
    
    while mat[row][col] != 0:
       row = random.randint(0,3)
       col = random.randint(0,3)
    
    mat[row][col] = 2
    
def get_current_state(mat):
    
    for row in range(4):
        for col in range(4):
            if mat[row][col] == 2048: return "won"
            
    for row in range(4):
        for col in range(4):
            if mat[row][col] == 0:
                return "game not over"
    
    for row in range(4):
        for col in range(4):
            if mat[row][col] == mat[row][col+1] or mat[row][col] == mat[row+1][col]:
                return "game not over"

    for col in range(3):
        if mat[3][col] == mat[3][col+1]:
            return "game not over"
    for row in range(3):
        if mat[row][3] == mat[row+1][3]:
            return "game not over"
        
    return 'lost'

def compress(mat):
    changed = False
    new_mat = []
    
    for row in range(4):
        new_mat.append([0] * 4)
    
    for row in range(4):
        pos = 0
        
        for col in range(4):
            if mat[row][col] != 0:
                new_mat[row][pos] = mat[row][col]
                if col != pos: changed = True
                pos += 1
    return new_mat, changed


def merge(mat):
    changed = False
    
    for row in range(4):
        for col in range(3):
            if mat[row][col] == mat[row][col + 1]:
                mat[row][col] *= 2
                mat[row][col+1] = 0
                changed = True
    return mat, changed


def reverse(mat):
    for row in range(4):
        for col in range(2):
            mat[row][col], mat[row][3-col] = mat[row][3-col], mat[row][col]
    return mat


def transpose(mat):
    for row in range(4):
        for col in range(row+1,4):
            mat[row][col], mat[col][row] = mat[col][row], mat[row][col]
    return mat

def move_left(mat):
    new_mat, changed1 = compress(mat)
    new_mat, changed2 = merge(new_mat)
    changed = changed2 or changed1
    new_mat, _ = compress(new_mat)
    
    return new_mat, changed

def move_right(mat):
    new_mat = reverse(mat)
    new_mat, changed = move_left(new_mat)
    new_mat = reverse(new_mat)
    return new_mat, changed

def move_up(mat):
    new_mat = transpose(mat)
    new_mat, changed = move_left(new_mat)
    new_mat = transpose(new_mat)
    return new_mat, changed

def move_down(mat):
    new_mat = transpose(mat)
    new_mat, changed = move_right(new_mat)
    new_mat = transpose(new_mat)
    return new_mat, changed


def print_matrix(mat):
    for row in range(4):
        print(mat[row])


    
   
            
        

if __name__ == '__main__':
    
    test_mat = []
    for i in range(4):
        test_mat.append([0] * 4)
    
    test_mat[2][1] = 14
    test_mat[0][3] = 11
    test_mat[3][2] = 55
    test_mat[3][3] = 10
    
    print_matrix(test_mat)
    test_mat, _ = compress(test_mat)
    
    print_matrix(test_mat)
    
    #start_game()
    