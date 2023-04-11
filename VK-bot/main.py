import vk_api.bot_longpoll
from vk_api import VkApi
from auth_data import auth_key, group_id


class EchoBot:

    def __init__(self, key, id):
        self.vk_src = VkApi(token=key)
        self.bot = vk_api.bot_longpoll.VkBotLongPoll(self.vk_src, id)

    def run(self, timeout=25):
        for event in self.bot.listen():
            print(event)


if __name__ == '__main__':
    bot = EchoBot(auth_key, group_id)
    bot.run()
