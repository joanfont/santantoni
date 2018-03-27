from datetime import date


class Message:

    @classmethod
    def filter(cls, message):
        raise NotImplementedError()

    @classmethod
    def handler(cls, bot, update):
        raise NotImplementedError()


class SantAntoniRemainingDays(Message):

    TEXT = '!santantoni'

    SANT_ANTONI_DATE = {
        'day': 17,
        'month': 1,
    }

    DEFAULT_TEMPLATE = 'Queden {remaining_days} dies per Sant Antoni 👹'
    TEMPLATE_ONE_DAY = 'Demà és Sant Antoni 👹'
    TEMPLATE_TODAY = 'Avui és Sant Antoni 👹'

    @classmethod
    def filter(cls, message):
        return message.text and message.text.lower() == cls.TEXT

    @classmethod
    def handler(cls, bot, update):
        chat_id = update.message.chat_id

        message = cls._compose_message()
        if message:
            bot.send_message(chat_id, message)

    @classmethod
    def _compose_message(cls):
        remaining_days = cls._get_remaining_days()
        if remaining_days > 1:
            message = cls.DEFAULT_TEMPLATE.format(remaining_days=remaining_days)
        elif remaining_days == 1:
            message = cls.TEMPLATE_ONE_DAY
        elif remaining_days == 0:
            message = cls.TEMPLATE_TODAY
        else:
            message = None

        return message

    @classmethod
    def _get_remaining_days(cls):
        today = date.today()
        next_sant_antoni = date(
            year=today.year + 1,
            **cls.SANT_ANTONI_DATE
        )

        delta = next_sant_antoni - today
        return delta.days
