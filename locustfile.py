# coding=utf-8
from locust import HttpLocust, TaskSet
from locust import Locust
from json import loads


def login(l):
    r_content = l.client.post("/register_login", json={'username': u'ddq', 'password': u'ddq'}).content
    cookie = loads(r_content)[0]['cookie']
    return cookie


def get_friends(l):
    r = l.client.post('/friends_list', json={'cookie': l.cookie})

class UserBehavior(TaskSet):

    cookie = None
    tasks = {get_friends: 100}

    def on_start(self):
        self.cookie = login(self)


class WebSiteUser(HttpLocust):
    host = 'http://127.0.0.1:3000'
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

# l = WebSiteUser()
# l.run()