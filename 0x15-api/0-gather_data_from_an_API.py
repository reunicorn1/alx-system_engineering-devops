#!/usr/bin/python3
"""
This script is used to access a certain REST API to give data
according to a certain employee ID to retrieve his TODO list
"""
import json
import requests
import sys


def get_name(user_id) -> str:
    """
    This function returns the name of the user after interacting with the API
    """
    params = {'id': user_id}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=params)
    return json.loads(user.text)[0]["name"]


def get_tasks(user_id) -> (list, int):
    """
    This function returns a tuple of tasks completed and the number of all
    tasks in a dictionary format after interacting with an API
    """
    params = {'userId': user_id}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=params)
    tasks = json.loads(todo.text)
    completed = [task for task in tasks if task.get('completed') is True]
    return completed, len(tasks)


if __name__ == "__main__":
    name = get_name(sys.argv[1])
    completed, tasks = get_tasks(sys.argv[1])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), tasks))
    for task in completed:
        print("\t {}".format(task["title"]))
