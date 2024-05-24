#!/usr/bin/python3
"""Returns employees TO DO list"""

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

    with open("{}.csv".format(worker_id), 'w') as f:
        for task in to_do_list:
            f.write('"{}","{}","{}","{}"\n'
                    .format(worker_id, u_n,
                            task.get("completed"), task.get('title')))
