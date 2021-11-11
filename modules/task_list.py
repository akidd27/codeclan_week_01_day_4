tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []

    for task in list:
        if not task["completed"]:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []

    for task in list:
        if task["completed"]:
            completed_tasks.append(task)
    return completed_tasks

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    tasks_at_least_time = []

    for task in list:
        if task["time_taken"] >= time:
            tasks_at_least_time.append(task)
    return tasks_at_least_time

## Find a task with a given description
def get_task_with_description(list, description):
    
    for task in list:
        if task['description'] == description:
            return task

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    pass

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)



