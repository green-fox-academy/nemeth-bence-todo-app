import sys

class Main:

    def arg_reader():
    	if len(sys.argv) == 1:
            print_help()
        else:
    		if sys.argv[1] == '-l':
                my_todo()

    def print_help():
        help_text = open('help.txt' , 'r')
        help_text = help_text.read
        print (help_text)

    def open_my_todo():
        my_todo = open('tasks.txt' , 'r')
        my_todo = my_todo.read
        print (my_todo)

    arguments = arg_reader()

'''    if len(arguments) == 0:
    	print('help text')
    else:
    	if( arguments[0] == '-l' ):
    		print('Addolunk ilyet', arguments[1])'''
