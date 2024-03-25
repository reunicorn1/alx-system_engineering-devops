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
    user = requests.get("https://jsonplaceholder.typicode.com/users",
                        params=params)
    return json.loads(user.text)[0]["username"]


def get_tasks(user_id) -> list:
    """
    This function returns a tuple of tasks completed and the number of all
    tasks in a dictionary format after interacting with an API
    """
    params = {"userId": user_id}
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        params=params)
    tasks = json.loads(todo.text)
    return tasks


def get_list_tasks(user_id) -> list:
    """
    This function uses the other function get_username and get_tasks
    to create a list of all tasks in a certain format for a specific user
    """
    name = get_username(user_id)
    tasks = get_tasks(user_id)
    new_list = []
    for task in tasks:
        new_list.append({"username": name, "task": task.get("title"),
                         "completed": task.get("completed")})
    return new_list


if __name__ == "__main__":
    dictionary = {}
    for i in range(1, 11):
        userlist = get_list_tasks(str(i))
        dictionary[str(i)] = userlist
    with open("todo_all_employees.json", "w") as f:
        json.dump(dictionary, f)
