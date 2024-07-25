to_do_list = []

def add_task(task):
    to_do_list.append(task)

def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)

def show_tasks():
    for task in to_do_list:
        print(task)

add_task("Learn Python")
add_task("Read a book")
show_tasks()
remove_task("Learn Python")
show_tasks()
