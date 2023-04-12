from vk_api import VkApi, bot_longpoll
from auth_data import auth_key, group_id
from random import randint


class EchoBot:

    def __init__(self, key, id):
        self.vk_src = VkApi(token=key)
        self.bot = bot_longpoll.VkBotLongPoll(self.vk_src, id)
        self.sender = self.vk_src.get_api()

    def run(self, timeout=25):
        for event in self.bot.listen():

            if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
                #     print(f'Новое сообщение от {event.object}, текст сообщения: \n')
                print(event.message.from_id, ' ', event.message.text)
                self.sender.messages.send(user_id=event.message.from_id, random_id=randint(0, 999),
                                          message=event.message.text + ' ' + event.message.text)


if __name__ == '__main__':
    bot = EchoBot(auth_key, group_id)
    bot.run()
