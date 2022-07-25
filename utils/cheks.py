from data.config import ADMINS
from loader import dp

#Цикл по спику операторів на співпадіння по заданому ID
def is_operator(id):
    return len([operator for operator in ADMINS if id == int(operator)])

#Перевірка State у юзерів
async def curent_user(user):
    user_state = dp.current_state(chat=user, user=user)
    curent_state = await user_state.get_state()
    return curent_state is None