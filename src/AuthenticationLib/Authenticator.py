from .IAuthenticator import IAuthenticator


class Authenticator(IAuthenticator):

    def __init__(self, session):
        self.session = session

    def authenticate(self, username, password):
        csrftoken = Authenticator.__getCsrfToken(self.session)
        url = "https://www.instagram.com/accounts/login/ajax/"
        headers = {
            "x-instagram-ajax": "dd83f9c3c3c1",
            "content-type": "application/x-www-form-urlencoded",
            "accept": "*/*",
            "x-requested-with": "XMLHttpRequest",
            "x-ig-app-id": "936619743392459",
            "x-csrftoken": csrftoken
        }
        payload = {
            "username": username,
            "password": password,
            "queryParams": '''{"source":"auth_switcher"}''',
            "optIntoOneTap": "false"
        }

        response = self.session.post(url = url, headers = headers, data = payload)

        if response.status_code != 200:
            raise RuntimeError("Login failed!")

    @staticmethod
    def __getCsrfToken(session):
        """Just makes get request to login page"""

        url = "https://www.instagram.com"
        headers = {
            "upgrade-insecure-requests": "1",
            "accept": "text/html",
        }

        response = session.get(url = url, headers = headers)

        if response.status_code == 200:
            return session.cookies.get_dict()["csrftoken"]

        raise RuntimeError("Can't achieve main page.")

