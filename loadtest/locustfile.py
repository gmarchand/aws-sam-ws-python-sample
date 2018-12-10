from locust import HttpLocust, TaskSet, task
import json
import uuid
 
class UserBehavior(TaskSet):
 
        
    def create_name(self):
        self.name = str(uuid.uuid1())
    
    @task(1)    
    def create_post(self):
        
        name = str(uuid.uuid1())
        headers = {'content-type': 'application/json','Accept-Encoding':'gzip'}
        self.client.post('/' + name,data= json.dumps({
		  "title": "load testing",
		  "name": name,
		  "description": "checking if a software can handle the expected load"
    }), 
    headers=headers, 
    name = "Create a new post")
 
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior