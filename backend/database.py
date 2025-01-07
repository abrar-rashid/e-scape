from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)


db = client.escape_room_db
escape_rooms = db.escape_rooms
users = db.users

'''Uncomment below to CLEAR database (irreversible) or show all documents'''
# escape_rooms.delete_many({})

# documents = escape_rooms.find()
# for document in documents:
#     print(document)

# user1 = {
#     'email': 'a@a.com',
#     'password': 'a',
#     'creator_id': 0
# }
# users.insert_one(user1)


def add_room(room, creator_id, name, database=db):
    room_doc = {
        'creator_id': creator_id,
        'name': name,
        'theme': room.theme.value,
        'keywords': room.keywords,
        'difficulty': room.difficulty,
        'length': room.length,
        'whitelist': room.whitelist,
        'blacklist': room.blacklist,
        'puzzles': room.get_puzzles(),
        'solutions': room.get_solutions(),
        'introduction': room.get_intro(),
        'story_phases': room.get_story_phases(),
        'conclusion': room.get_conclusion(),
        'failure': room.get_failure(),
        'is_public': room.is_public
    }
    rooms = database.escape_rooms
    room_id = rooms.insert_one(room_doc).inserted_id
    return room_id


def replace_room(room_id, room, creator_id, database=db):
    room_doc = {
        'creator_id': creator_id,
        'theme': room.theme.value,
        'keywords': room.keywords,
        'difficulty': room.difficulty,
        'length': room.length,
        'whitelist': room.whitelist,
        'blacklist': room.blacklist,
        'puzzles': room.get_puzzles(),
        'solutions': room.get_solutions(),
        'introduction': room.get_intro(),
        'story_phases': room.get_story_phases(),
        'conclusion': room.get_conclusion(),
        'failure': room.get_failure(),
        'is_public': room.is_public
    }
    rooms = database.escape_rooms
    rooms.update_one(
        {'_id': ObjectId(room_id)},
        {'$set': room_doc},
        upsert=True
    )


def replace_room_field(room_id, field_to_replace, new_val, database=db):
    rooms = database.escape_rooms
    rooms.update_one(
        {'_id': ObjectId(room_id)},
        {'$set': {field_to_replace: new_val}},
        upsert=True
    )


def get_user(email, password, database=db):
    accounts = database.users
    user = accounts.find_one({'email': str(email)})
    if user and (password == user['password']):
        return user['creator_id']
    else:
        return None


def add_user(email, password, database=db):
    accounts = database.users
    existing_user = accounts.find_one({'email': str(email)})
    if existing_user:
        # If user already exists, must fail to sign up
        raise ValueError("User with this email already exists")
    else:
        # If user doesn't exist, insert the new user data into the collection.
        creator_id = accounts.count_documents({})
        user_data = {
            'email': str(email),
            'password': password,
            'creator_id': creator_id
        }
        accounts.insert_one(user_data)
        return creator_id


def get_all_rooms_for_id(creator_id, database=db):
    rooms = database.escape_rooms
    rooms = list(rooms.find({'creator_id': creator_id}))
    new_rooms = []

    for room in rooms:
        room['_id'] = str(room['_id'])
        new_rooms.append(room)
    return new_rooms


def get_public_rooms(database=db):
    rooms = database.escape_rooms
    rooms = list(rooms.find({'is_public': True}))
    new_rooms = []

    for room in rooms:
        room['_id'] = str(room['_id'])
        new_rooms.append(room)
    return new_rooms


def delete_room_with_id(room_id, database=db):
    rooms = database.escape_rooms
    return rooms.delete_one({'_id': ObjectId(room_id)}).deleted_count


def find_room(room_id, database=db):
    rooms = database.escape_rooms
    return rooms.find_one({'_id': ObjectId(room_id)})


def is_valid_id(room_id):
    return ObjectId.is_valid(room_id)
