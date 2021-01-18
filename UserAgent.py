import random

headers = [

]


def get_User_Agent():
    sjs = random.randint(0, len(headers) - 1)
    user_agent = headers[sjs]
    return user_agent
