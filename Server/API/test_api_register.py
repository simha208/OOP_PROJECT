import pytest
import requests


class TestRegister():
    @pytest.mark.sanity
    def test_success_register(self):
        url= "https://ivolunteer-app.herokuapp.com/users/register"
        myobj ={"FirstName":"kcij","LastName":"okjcpio","Email":"cffbjrpo0@gmail.com","Password":"202020","Age":"24","ProfilePic":"jbuhjnm"}
        y = requests.post(url, json=myobj)
        value =y.json()
        assert y.status_code == 200
        assert y.elapsed.total_seconds() < 10
        assert value["Message"] == "User Added Successfully"


    @pytest.mark.regration
    def test_incorrect_email_register(self):
        url= "https://ivolunteer-app.herokuapp.com/users/register"
        myobj ={"Email":"jhbgphfjgh1j","Password":"45612","Age":"17","ProfilePic":"dgrhthtyh","FirstName":"bbbb","LastName":"zaro"}
        y = requests.post(url, json=myobj)
        value =y.json()
        assert y.status_code == 200
        assert y.elapsed.total_seconds() < 10
        assert value["Message"] == "User Added Successfully"

    @pytest.mark.regration
    def test_FirstNameNull_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        myobj = {"LastName": "fzfs", "Email": "fs4ad@gmail.com", "Age": "25", "ProfilePic": "טאו","Password": "54684"}
        y = requests.post(url, json=myobj)
        assert y.status_code == 500
        assert y.elapsed.total_seconds() < 10

    @pytest.mark.regration
    def test_LastNameNull_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        myobj = {"FirstName":"bbbbyyy","Email":"fgsad@gmail.com","Age":"25","ProfilePic":"טאו","Password":"54684"}
        y = requests.post(url, json=myobj)
        assert y.status_code == 500
        assert y.elapsed.total_seconds() < 10

    @pytest.mark.regration
    def test_emailNull_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        mysql = {"FirstName":"bbbbyyy","LastName":"fzfs","Age":"25","ProfilePic":"טאו","Password":"54684"}
        y = requests.post(url, json=mysql)
        assert y.status_code == 500
        assert y.elapsed.total_seconds() < 10

    @pytest.mark.regration
    def test_ageNull_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        mysql = {"FirstName":"bbbbyyy","LastName":"fzfs","Email":"fsad@gmail.com","ProfilePic":"טאו","Password":"54684"}
        y = requests.post(url, json=mysql)
        assert y.status_code == 400
        assert y.elapsed.total_seconds() < 10

    @pytest.mark.regration
    def test_ProfilePicNull_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        mysql = {"FirstName":"bbbbyyy","LastName":"fzfs","Email":"fsad@gmail.com","Password":"54684"}
        y = requests.post(url, json=mysql)
        assert y.status_code == 400
        assert y.elapsed.total_seconds() < 10

    @pytest.mark.regration
    def test_PasswordNull_register(self):
        url = "https://ivolunteer-app.herokuapp.com/users/register"
        mysql = {"FirstName":"bbbbyyy","LastName":"fzfs","Email":"fsad@gmail.com","Age":"25","ProfilePic":"טאו"}
        y = requests.post(url, json=mysql)
        assert y.status_code == 400
        assert y.elapsed.total_seconds() < 10