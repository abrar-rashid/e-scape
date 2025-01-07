import environment  # NOQA isort:skip
import pytest
from bson.objectid import ObjectId
from database import (add_room, add_user, delete_room_with_id, find_room,
                      get_all_rooms_for_id, get_user, replace_room)
from mongomock import MongoClient
from src.pages.pageTypes import Difficulty, PuzzleType, Theme
from src.room_new import Room


@pytest.fixture
def mock_db():
    # Create a mongomock client for testing
    client = MongoClient()
    db = client.escape_room_db
    yield db


def test_add_room(mock_db):
    a = [x.value for x in PuzzleType]
    room = Room(Theme.PIRATE, ["finding buried treasure",
                "exploring the seas"], Difficulty.HARD,
                len(a), a, [], include_storyline=False)
    room.storyline.introduction = ""
    room.storyline.phases = []
    room.storyline.conclusion = ""
    room.storyline.failure = ""
    room_id = add_room(room, "1", "Test Room", database=mock_db)
    # Verify that room was inserted into mock database
    assert room_id is not None
    assert mock_db.escape_rooms.count_documents({}) == 1


def test_replace_room(mock_db):
    a = [x.value for x in PuzzleType]
    room = Room(Theme.PIRATE, ["finding buried treasure",
                "exploring the seas"], Difficulty.HARD,
                len(a), a, [], include_storyline=False)
    room.storyline.introduction = ""
    room.storyline.phases = []
    room.storyline.conclusion = ""
    room.storyline.failure = ""
    room_id = add_room(room, "1", "Test Room", database=mock_db)
    # Call the replace_room function with mock database
    room.storyline.introduction = "intro"
    replace_room(room_id, room, "1", database=mock_db)
    # Verify that room was replaced in mock database
    updated_room = mock_db.escape_rooms.find_one({'_id': room_id})
    assert updated_room is not None
    assert updated_room['conclusion'] == ""
    assert updated_room['introduction'] != ""
    assert mock_db.escape_rooms.count_documents({}) == 1


def test_get_user(mock_db):
    # Add a user to the mock database
    mock_db.users.insert_one({'email': 'test@example.com',
                              'password': 'password', 'creator_id': '123'})

    # Test getting an existing user
    user_id = get_user('test@example.com', 'password', database=mock_db)
    assert user_id == '123'

    # Test getting a non-existing user
    user_id = get_user('nonexisting@example.com', 'password', database=mock_db)
    assert user_id is None


def test_add_user(mock_db):
    # Test adding a new user
    user_id = add_user('test@example.com', 'password', database=mock_db)
    assert user_id == 0  # Assuming creator_id starts from 0

    # Test adding an existing user (should raise ValueError)
    with pytest.raises(ValueError):
        add_user('test@example.com', 'password', database=mock_db)


def test_get_all_rooms_for_id(mock_db):
    # Add some rooms to the mock database
    mock_db.escape_rooms.insert_many([
        {'creator_id': '123', 'name': 'Room 1'},
        {'creator_id': '123', 'name': 'Room 2'}
    ])

    # Test getting all rooms for a user
    rooms = get_all_rooms_for_id('123', database=mock_db)
    assert len(rooms) == 2
    assert rooms[0]['name'] == 'Room 1'
    assert rooms[1]['name'] == 'Room 2'


def test_delete_room_with_id(mock_db):
    # Add a room to the mock database
    room_id = mock_db.escape_rooms.insert_one({'creator_id': '123',
                                               'name': 'Room'}).inserted_id
    # Test deleting a room
    deleted_count = delete_room_with_id(str(room_id), database=mock_db)
    assert deleted_count == 1

    # Test deleting the deleted room
    deleted_count = delete_room_with_id(str(room_id), database=mock_db)
    assert deleted_count == 0

    # Test deleting a non-existing room with random room id
    deleted_count = delete_room_with_id(ObjectId("aa5f472e029530cbaac0fd5a"),
                                        database=mock_db)
    assert deleted_count == 0


def test_find_room(mock_db):
    # Add a room to the mock database
    room_id = mock_db.escape_rooms.insert_one({'creator_id': '123', 'name':
                                               'Room'}).inserted_id

    # Test finding an existing room
    room = find_room(str(room_id), database=mock_db)
    assert room['name'] == 'Room'

    # Test finding a non-existing room with random room id
    room = find_room(ObjectId("aa5f472e029530cbaac0fd5a"), database=mock_db)
    assert room is None
