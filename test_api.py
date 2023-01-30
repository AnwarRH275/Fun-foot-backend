import unittest
from main import create_app
from config import TestConfig
from models.exts import db


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():
            db.init_app(self.app)
            db.create_all()

    def test_hello_word(self):
        hello_response = self.client.get('/product/Hello')

        json = hello_response.json
       # print(json)
        self.assertEqual(json, {"message": "hello word!!"})

    def test_signUp(self):
        signup_reponse = self.client.post('/auth/signup', json={
            "username": "anwarleroc21",
            "email": "mail@mail.com",
            "password": "thegamecc"
        })
        # json = signup_reponse.json
        # print(json)
        # self.assertEqual(json, json)
        status = signup_reponse.status_code
        print(status)
        self.assertEqual(status, 201)

    def test_login(self):
        signup_reponse = self.client.post('/auth/signup', json={
            "username": "anwarleroc21",
            "email": "mail@mail.com",
            "password": "thegamecc"
        })

        login_response = self.client.post('auth/login', json={
            "username": "anwarleroc21",
            "password": "thegamecc"
        })
        status = login_response.status_code
        self.assertEqual(status, 200)

    def test_create_recipie(self):
        signup_reponse = self.client.post('/auth/signup', json={
            "username": "anwarleroc21",
            "email": "mail@mail.com",
            "password": "thegamecc"
        })

        login_response = self.client.post('auth/login', json={
            "username": "anwarleroc21",
            "password": "thegamecc"
        })
        acces_token = login_response.json['acces_token']
        create_recipie_response = self.client.post('product/recipies',
                                                   json={
                                                       "title": "item1",
                                                       "description": "desciption of item1"
                                                   }, headers={'authorization': f'Bearer {acces_token}'}
                                                   )
        status = create_recipie_response.status_code
        self.assertEqual(status, 201)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':

    unittest.main()
