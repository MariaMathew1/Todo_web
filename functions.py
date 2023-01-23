FILEPATH = 'C:/Users/wetsp/PycharmProjects/pythonProject/Web_todo/tasks.txt'


def get_task(filepath=FILEPATH):
    """
    Reads a text file and returns the list of tasks
    :return: list of tasks
    """
    with open(filepath, 'r') as file:
        todo_list_local = file.readlines()

    return todo_list_local


def write_task(task_list, filepath=FILEPATH):
    """
    Writes a new task into the text file
    :param task_list:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(task_list)
