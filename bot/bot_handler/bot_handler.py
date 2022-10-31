import loguru

from bot.bot import bot
from bot.manipulation.support import get_status_web, get_status_ping

logger = loguru.logger


class BotHandler(object):
    def run(self):
        bot.polling()

    @staticmethod
    @bot.message_handler(commands=["help", "start"])
    def host(message):
        msg = bot.send_message(
            message.chat.id,
            "This bot is created for checking connection to some host\n"
            + "You can use two methods:\n"
            + "/ping for checking host via ping command\n"
            + "/web for checking host via get request",
        )

    @staticmethod
    @bot.message_handler(commands=["ping"])
    def host(message):
        msg = bot.send_message(
            message.chat.id, "Please provide the host DNS name (f.e roslyakov.net)"
        )
        bot.register_next_step_handler(msg, BotHandler.ping)

    @staticmethod
    @bot.message_handler(commands=["web"])
    def host(message):
        msg = bot.send_message(
            message.chat.id, "Please provide the host DNS name (f.e roslyakov.net)"
        )
        bot.register_next_step_handler(msg, BotHandler.web)

    @staticmethod
    @bot.message_handler(content_types=["text"])
    def ping(message):

        status = get_status_ping(message.text)

        if status == 0:
            logger.info(f"Network Active for host: {message.text}")
            bot.send_message(
                message.chat.id, f"Network Active for host: {message.text}"
            )
        else:
            logger.error(f"Network Error for host: {message.text}")
            bot.send_message(message.chat.id, f"Network Error for host: {message.text}")

    @staticmethod
    @bot.message_handler(content_types=["text"])
    def web(message):

        print(message.text)
        status = get_status_web(message.text)
        print(status)

        if status == 0:
            logger.info(f"Network Active for host: {message.text}")
            bot.send_message(
                message.chat.id, f"Network Active for host: {message.text}"
            )
        else:
            logger.error(f"Network Error for host: {message.text}")
            bot.send_message(message.chat.id, f"Network Error for host: {message.text}")
