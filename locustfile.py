# This locust test script example will simulate a user cloned from https://github.com/locustio/locust/tree/master/examples
# browsing the Locust documentation on https://docs.locust.io/

import random
from locust import HttpLocust, TaskSet, task
from pyquery import PyQuery


class BrowseDocumentation(TaskSet):
    @task
    def index_page(self):
        r = self.client.get("/")
        pq = PyQuery(r.content)
        link_elements = pq(".toctree-wrapper a.internal")
        self.toc_urls = [
            l.attrib["href"] for l in link_elements
        ]
        # insert more code to check for urls and follow them here




class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation

    # we assume someone who is browsing the Locust docs, 
    # generally has a quite long waiting time (between 
    # 20 and 600 seconds), since there's a bunch of text 
    # on each page
    min_wait = 20  * 1000
    max_wait = 600 * 1000