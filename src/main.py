from AuthenticationLib.Authenticator import Authenticator
import requests


def main():
    session = requests.Session()
    session.verify = False
    session.headers.update({
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.119 Safari/537.36",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    session.proxies.update({
        "http": "http://127.0.0.1:8888",
        "https": "https://127.0.0.1:8888"
    })
    authenticator = Authenticator(session = session)
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    authenticator.authenticate(username = username, password = password)


if __name__ == '__main__':
    main()
