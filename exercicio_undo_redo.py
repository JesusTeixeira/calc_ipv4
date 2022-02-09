def show_op(to_do_list):
    print()
    print('Tarefas: ')
    print(to_do_list)
    print()
    
def do_undo(to_do_list, redo_list):
    if not to_do_list:
        print('Nada a desfazer')
        return
    
    last_to_do = to_do_list.pop()
    redo_list.append(last_to_do)

def do_redo(to_do_list, redo_list):
    if not redo_list:
        print('Nada a refazer: ')
        return
    
    last_redo = redo_list.pop()
    to_do_list.append(last_redo)
    
    
def do_add(to_do, to_do_list):
    to_do_list.append(to_do)

if __name__ == '__main__':
    to_do_list = []
    redo_list = []
    
    
    while True:
        to_do = input('Digite uma tarefa ou undo, redo, ls: ')

        if to_do == 'ls':
            show_op(to_do_list)
            continue
        
        elif to_do == 'undo':
            do_undo(to_do_list, redo_list)
            continue
            
        elif to_do == 'redo':
            do_redo(to_do_list, redo_list)
            continue
        
        do_add(to_do, to_do_list)
        
        