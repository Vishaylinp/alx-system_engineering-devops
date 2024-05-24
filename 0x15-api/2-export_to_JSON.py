#!/usr/bin/python3
"""Returns employees TO DO list"""

import json
import requests
import sys

if __name__ == "__main__":
    worker_id = sys.argv[1]
    url_api = "https://jsonplaceholder.typicode.com/users"
    url = url_api + "/" + worker_id

    response = requests.get(url)

    u_n = response.json().get('username')

    url_todo = url + "/todos"
    response = requests.get(url_todo)
    to_do_list = response.json()
    count = 0
    complete_t = []

    json_dict = {worker_id: []}
    for task in to_do_list:
        json_dict[worker_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": u_n
            })

    with open('{}.json'.format(worker_id), 'w') as j_file:
        json.dump(json_dict, j_file)
