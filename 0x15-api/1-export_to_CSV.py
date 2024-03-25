#!/usr/bin/python3
"""
This script is used to access a certain REST API to give data
according to a certain employee ID to retrieve his TODO list
"""
import csv
import json
import requests
import sys


def get_username(user_id) -> str:
    """
    This function returns the username after interacting with the API
    """
    params = {'id': user_id}
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params=params)
    return json.loads(user.text)[0]["username"]


def get_tasks(user_id) -> list:
    """
    This function returns a tuple of tasks completed and the number of all
    tasks in a dictionary format after interacting with an API
    """
    params = {'userId': user_id}
    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params=params)
    tasks = json.loads(todo.text)
    return tasks


if __name__ == "__main__":
    name = get_username(sys.argv[1])
    tasks = get_tasks(sys.argv[1])
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([sys.argv[1], name, task.get("completed"),
                             task.get("title")])
