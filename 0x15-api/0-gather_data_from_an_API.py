#!/usr/bin/python3
"""Returns employees TO DO list"""

import requests
import sys

if __name__ == "__main__":
    worker_id = sys.argv[1]
    url_api = "https://jsonplaceholder.typicode.com/users"
    url = url_api + "/" + worker_id

    response = requests.get(url)

    worker_name = response.json().get('name')

    url_todo = url + "/todos"
    response = requests.get(url_todo)
    to_do_list = response.json()

    i = 0
    complete_t = []

    for task in to_do_list:
        if task.get('completed'):
            complete_t.append(task)
            i = i + 1

    print(f"Employee {worker_name} is done with tasks ({i}/{len(to_do_list)}):")

    for task in complete_t:
        print("\t {}".format(task.get('title')))
