import pytest
import requests


class TestLogin():
    @pytest.mark.sanity
    def test_success_login(self):
        url= "https://wetechsocial.herokuapp.com/auth/login"
        myobj = {"email": "hsjllhi@gmail.com", "password": "202020888"}
        x =requests.post(url, data=myobj)
        print(x.text)

    @pytest.mark.sanity
    def test_login_correct(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myobj = {"email": "simhaamara2020@gmail.com", "password": "202020888"}
        x = requests.post(url, data=myobj)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 5

    @pytest.mark.regration
    def test_login_incorrect(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myodj= {"email": "simhaamara2020@gmail.com", "password": "202020888"}
        x = requests.post(url, data=myodj)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 5

    @pytest.mark.sanity
    def test_search_friends(self):
        url = "https://wetechsocial.herokuapp.com/users/getByUserName?username=betty"
        body = "username: betty"
        x = requests.get(url, data=body)
        assert x.status_code == 200
        assert x.elapsed.total_seconds() <5

    @pytest.mark.sanity
    def test__incorrect(self):
        url = "https://wetechsocial.herokuapp.com/auth/login"
        myodj= {"email": "simhaamara2020@gmail.com", "password": "202020888"}
        x = requests.post(url, data=myodj)
        assert x.status_code == 500
        assert x.elapsed.total_seconds() < 5


