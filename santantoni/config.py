import decouple


class Config:

    @property
    def DEBUG(self):
        return decouple.config('DEBUG', default=False, cast=bool)

    @property
    def TELEGRAM_TOKEN(self):
        return decouple.config('TELEGRAM_TOKEN')


config = Config()
