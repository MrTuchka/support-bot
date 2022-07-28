import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from data.config import dp_api

cred = credentials.Certificate(dp_api)
firebase_admin.initialize_app(cred)

db = firestore.client()


async def add_statistics():
    statistics = db.collection(u'statistic').document(u"SidisTestsBot")
    launches = statistics.get().to_dict()['number_of_launches']
    launches += 1;
    statistics.set({
        u'number_of_launches': launches,
    })


async def chek(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        name = user_name.to_dict()['name']
    except:
        name = 'No name'
    return name != "No name"


async def get_name(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        name = user_name.to_dict()['name']
    except:
        name = 'No name'
    return name


async def get(bot_name, collection, field):
    bot_ref = db.collection(str(collection)).document(str(bot_name))
    data = bot_ref.get()
    try:
        current_field = data.to_dict()[str(field)]
    except:
        current_field = 'No data'
    return current_field


async def get_phone(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        phone = user_name.to_dict()['phone']
    except:
        phone = 'No phone'
    return phone


async def create_user(id, full_name, username):
    doc_ref = db.collection(u'users').document(str(id))
    doc_ref.set({
        u'name': str(full_name),
        u'username': str(username),
    })


async def get_all_users():
    all_users = db.collection(u'users')
