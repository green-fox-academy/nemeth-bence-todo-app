import sys

def arg_reader():
	if len(sys.argv) == 1:
        print_help()
    else:
        if sys.argv[1] == '-l':
            open_todo()
        if sys.argv[1] == '-a':
            open_add()
        if sys.argv[1] == '-r':
            open_remove()
        if sys.argv[1] == '-c':
            open_complete()

def print_help():
    help_text = open('help.txt' , 'r')
    help_text = help_text.read
    print (help_text)

def open_todo():
    my_todo = open('tasks.txt' , 'r')
    my_todo = my_todo.read
    print (my_todo)

def open_add()
    add = open('tasks.txt' , 'a')
    add = add.readlines
    add.write("\n0;" + sys.argv[2].rstrip())



arg_reader()
