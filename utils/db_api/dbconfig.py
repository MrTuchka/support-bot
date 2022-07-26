import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from data.config import dp_api

cred = credentials.Certificate(dp_api)
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_statistics():
    statistics = db.collection(u'users').document(u"statistic")
    launches = statistics.get().to_dict()['number of launches']
    launches += 1;
    statistics.set({
        u'number of launches': launches,
    })


def chek(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        name = user_name.to_dict()['name']
    except:
        name = 'No name'
    return name != "No name"


def get_name(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        name = user_name.to_dict()['name']
    except:
        name = 'No name'
    return name

def get_phone(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        phone = user_name.to_dict()['phone']
    except:
        phone = 'No phone'
    return phone

def create_user(id, full_name, username):
    doc_ref = db.collection(u'users').document(str(id))
    doc_ref.set({
        u'name': str(full_name),
        u'username': str(username),
    })