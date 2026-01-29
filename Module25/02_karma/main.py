import random


class KillError(Exception):
    def __str__(self):
        return 'вы кого-то убили'


class DrunkError(Exception):
    def __str__(self):
        return 'вы выпили алкоголь'


class CarCrashError(Exception):
    def __str__(self):
        return 'вы разбили машину'


class GluttonyError(Exception):
    def __str__(self):
        return 'вы слишком много съели'


class DepressionError(Exception):
    def __str__(self):
        return 'вы в депрессии'


def one_day():
    error_dict = {1: KillError, 2: DrunkError, 3: CarCrashError, 4: GluttonyError, 5: DepressionError}
    if random.randint(0, 10) == 10:
        raise error_dict[random.randint(1, 5)]
    return random.randint(1, 7)


karma = 0
with open('karma.log', 'w', encoding='UTF-8') as log:
    while karma < 500:
        try:
            karma += one_day()
        except KillError:
            log.write('KillError: вы кого-то убили\n')
        except DrunkError:
            log.write('DrunkError: вы выпили алкоголь\n')
        except CarCrashError:
            log.write('CarCrashError: вы разбили машину\n')
        except GluttonyError:
            log.write('GluttonyError: вы слишком много съели\n')
        except DepressionError:
            log.write('DepressionError: вы в депрессии\n')

print('Вы достигли просветления!')







