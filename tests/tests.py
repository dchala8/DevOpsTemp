import json
from unittest import TestCase
from faker import Faker
from application import application

class TestUsers(TestCase):
    
    def setUp(self):
        self.data_factory = Faker()
        self.client = application.test_client()
        
    #TESTS FOR HEALTH CHECK
    def test_success_health_check(self):
        healthBlacklists_request = self.client.get("/", headers={'Content-Type': 'application/json'})
        self.assertEqual(healthBlacklists_request.status_code, 200)
        
        
    #TESTS FOR THE POST METHOD
    def test_success_post_email(self):
        email = self.data_factory.email()
        app_uuid = self.data_factory.name()
        blocked_reason = self.data_factory.name()
        
        new_blacklist ={
                "email" : email,
                "app_uuid" : app_uuid,
                "blocked_reason" : blocked_reason
        }

        postBlackslit_request = self.client.post("/blacklists",data=json.dumps(new_blacklist) ,headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})
        getBlackslit_request = self.client.get("/blacklists/"+email, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})
        request_response = json.loads(getBlackslit_request.data)
        
        self.assertEqual('is_in_black_list' in request_response, True)
        self.assertEqual('reason' in request_response, True)
        self.assertEqual(request_response['reason'], blocked_reason)
        self.assertEqual(postBlackslit_request.status_code, 200)
        self.assertEqual(getBlackslit_request.status_code, 200)
        
        
    def test_failed_incomplete_body_post_email(self):
        email = self.data_factory.email()
        app_uuid = self.data_factory.name()
        
        new_blacklist ={
                "email" : email,
                "app_uuid" : app_uuid
        }

        postBlackslit_request = self.client.post("/blacklists",data=json.dumps(new_blacklist) ,headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})

        self.assertEqual(postBlackslit_request.status_code, 400)
        
        
    def test_failed_no_body_post_email(self):
        new_blacklist ={
        }

        postBlackslit_request = self.client.post("/blacklists",data=json.dumps(new_blacklist) ,headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})

        self.assertEqual(postBlackslit_request.status_code, 400)
        
    
    def test_failed_no_token_post_email(self):
        email = self.data_factory.email()
        app_uuid = self.data_factory.name()
        blocked_reason = self.data_factory.name()
        
        new_blacklist ={
                "email" : email,
                "app_uuid" : app_uuid,
                "blocked_reason" : blocked_reason
        }

        postBlackslit_request = self.client.post("/blacklists",data=json.dumps(new_blacklist) ,headers={'Content-Type': 'application/json'})

        self.assertEqual(postBlackslit_request.status_code, 400)
        
        
    def test_failed_bad_token_post_email(self):
        email = self.data_factory.email()
        app_uuid = self.data_factory.name()
        blocked_reason = self.data_factory.name()
        
        new_blacklist ={
                "email" : email,
                "app_uuid" : app_uuid,
                "blocked_reason" : blocked_reason
        }

        postBlackslit_request = self.client.post("/blacklists",data=json.dumps(new_blacklist) ,headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqeasdasdasdas1sdfs5sdqe56'})

        self.assertEqual(postBlackslit_request.status_code, 403)
        
        
        
    #TESTS FOR THE GET METHOD        
    def test_success_get_existing_email(self):
        email = self.data_factory.email()
        app_uuid = self.data_factory.name()
        blocked_reason = self.data_factory.name()
        
        new_blacklist ={
                "email" : email,
                "app_uuid" : app_uuid,
                "blocked_reason" : blocked_reason
        }

        postBlackslit_request = self.client.post("/blacklists",data=json.dumps(new_blacklist) ,headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})
        getBlackslit_request = self.client.get("/blacklists/"+email, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})
        request_response = json.loads(getBlackslit_request.data)
        
        self.assertEqual('is_in_black_list' in request_response, True)
        self.assertEqual('reason' in request_response, True)
        self.assertEqual(request_response['reason'], blocked_reason)
        self.assertEqual(getBlackslit_request.status_code, 200)
        
        
    def test_success_get_non_existing_email(self):
        email = self.data_factory.email()
       
        getBlackslit_request = self.client.get("/blacklists/"+email, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe56'})
        request_response = json.loads(getBlackslit_request.data)
        
        self.assertEqual('is_in_black_list' in request_response, True)
        self.assertEqual(request_response['is_in_black_list'], False)
        self.assertEqual('reason' in request_response, False)
        self.assertEqual(getBlackslit_request.status_code, 200)
        
        
    def test_failed_bad_token(self):
        email = self.data_factory.email()
        
        getBlackslit_request = self.client.get("/blacklists/"+email, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer kfsdmxcvnms82439wwqeqe1sdfs5sdqe5sas'})
        self.assertEqual(getBlackslit_request.status_code, 403)
        
        
    def test_failed_no_token(self):
        email = self.data_factory.email()
        
        getBlackslit_request = self.client.get("/blacklists/"+email, headers={'Content-Type': 'application/json'})
        self.assertEqual(getBlackslit_request.status_code, 400)