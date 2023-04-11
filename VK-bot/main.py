
def load_pass ():
    auth_key = ''
    with open('config.ini', mode='r', encoding='utf8') as configs:
        for line in configs:
            auth_key = line
            break
    return auth_key

def call ():
    pass


if __name__ == '__main__':
     pass