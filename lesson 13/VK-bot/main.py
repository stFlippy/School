from vk_api import VkApi, bot_longpoll
from auth_data import auth_key, group_id
from random import randint
import logging

class Fatality(Exception):

    def __str__(self):
        return "Screw u guys, Im gona home"


logger = logging.getLogger('Inf')
logger.setLevel('DEBUG')

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.INFO)

f_handler = logging.FileHandler(filename='errors.txt', mode='a')
f_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(levelname)s - %(asctime)s — %(message)s")
s_handler.setFormatter(formatter)
f_handler.setFormatter(formatter)

logger.addHandler(s_handler)
logger.addHandler(f_handler)

class EchoBot:

    def __init__(self, key, id):
        self.vk_src = VkApi(token=key)
        logger.info('Получен ключ')
        logger.warning('в жопу кайла')
        self.bot = bot_longpoll.VkBotLongPoll(self.vk_src, id)
        self.sender = self.vk_src.get_api()

    def run(self, timeout=25):
        try:
            for event in self.bot.listen():

                if event.type == bot_longpoll.VkBotEventType.MESSAGE_NEW:
                    if event.message.text == 'Fatality':
                        raise Fatality
                    #     print(f'Новое сообщение от {event.object}, текст сообщения: \n')
                    print(event.message.from_id, ' ', event.message.text)
                    self.sender.messages.send(user_id=event.message.from_id, random_id=randint(0, 999),
                                              message=event.message.text + ' ' + event.message.text)

        except Exception as err:
            logger.error(err)


if __name__ == '__main__':
    logger.debug('STart')
    bot = EchoBot(auth_key, group_id)
    bot.run()
