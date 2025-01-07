# Load environment
import os
from pathlib import Path
import environment  # NOQA isort:skip

import sys
from random import randint
# from bson import ObjectId
from flask import Flask, request, jsonify, session, send_file
from flask_cors import CORS
from database import (add_room, add_user, delete_room_with_id,
                      find_room, get_all_rooms_for_id, get_public_rooms,
                      get_user, is_valid_id, replace_room, replace_room_field)
from src.pages.pageTypes import Difficulty, PuzzleType, Theme
from src.room_new import Room


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SESSION_COOKIE_PATH'] = '/'
CORS(app, supports_credentials=True)


# class User():
#     def __init__(self):
#         self.logged_in = False

#     def set_details(self, email, creator_id):
#         self.email = email
#         self.creator_id = creator_id
#         self.logged_in = True


# user = User()

def set_session_details(email, creator_id):
    session["email"] = email
    session['creator_id'] = creator_id
    session['logged_in'] = True
    session['room'] = None


@app.route('/api/generate-room', methods=['POST'])
def generate_room():
    data = request.get_json()
    name = data['roomName']
    theme = Theme(int(data['theme']))
    keywords = data['keywords']
    difficulty = Difficulty(int(data['difficulty']))
    length = data['length']
    whitelist = data['whitelist']
    blacklist = data['blacklist']
    is_public = data['isPublic']
    try:
        room = Room(theme, keywords, difficulty, length,
                    whitelist, blacklist, include_storyline=True,
                    is_public=is_public)
        room_id = add_room(room, session['creator_id'], name)
        session['curr_room_id'] = str(room_id)
        return jsonify({
            'id': session['curr_room_id']
        })
    except Exception:
        return "Invalid parameters for escape room", 404


@app.route('/api/update-room', methods=['GET'])
def save_room():
    try:
        if 'curr_room_id' in session:
            room_id = session['curr_room_id']
            room = set_room(room_id)
            url = room.regen_room()
            replace_room(room_id, room,
                         session['creator_id'])
            return send_file(url, mimetype='application/pdf')
        else:
            return 'cannot update room', 404
    except Exception:
        return "Invalid parameters for escape room"


@app.route('/api/toggle-public/<value>', methods=['POST'])
def toggle_public(value):
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
    replace_room_field(room_id, 'is_public', value)
    return jsonify({'done': 1})


@app.route('/api/themes')
def get_themes():
    return jsonify({'names': list(Theme.get_names())})


@app.route("/api/background-image/<theme>", methods=["GET"])
def get_background_image(theme):
    theme_name = Theme(int(theme)).name.lower()
    files_no = len(os.listdir(
        f'{Path(__file__).parent}/src/pages/themes/{theme_name}/papers'
    ))
    imageNo = randint(1, files_no)
    image = Theme.get_images(
        Theme(int(theme))
    ) + f'{theme_name}{imageNo}.png'
    return jsonify({'url': image})


@app.route('/api/puzzle-count')
def get_puzzle_count_json():
    return jsonify({'count': len(get_puzzle_names())})


@app.route('/api/puzzle-types')
def get_puzzle_types_json():
    return jsonify({'names': get_puzzle_names()})


def get_puzzle_names():
    return list(PuzzleType.get_names())


# @app.route('/api/introduction')
# def get_introduction():
#     return jsonify({'introduction': find_room(room_id)['Intro']})


@app.route('/api/regenerate-introduction', methods=["POST"])
def regenerate_introduction():
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.regen_intro()
        replace_room_field(room_id, 'introduction', room.get_intro())
        return jsonify({'introduction': room.storyline.introduction})
    else:
        return 'cannot regen introduction', 404


@app.route('/api/edit-introduction/<new_intro>', methods=["POST"])
def edit_introduction(new_intro):
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.set_intro_man(new_intro)
        replace_room_field(room_id, 'introduction', room.get_intro())
        return jsonify({'introduction': room.storyline.introduction})
    else:
        return 'cannot edit introduction', 404


@app.route('/api/regenerate-story-phase/<phase>', methods=['POST'])
def regenerate_story_phase(phase):
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        phase_int = int(phase)
        room.regen_story_by_phase(phase_int)
        replace_room_field(room_id, 'story_phases',
                           room.get_story_phases())
        return jsonify({'story_phase': room.get_story_by_phase(phase_int)})
    else:
        return 'cannot regen story by phase', 404


@app.route('/api/edit-story-phase', methods=['POST'])
def edit_story_phase():
    phase = int(request.json.get('phase'))
    text = request.json.get('text')
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.set_story_by_phase_man(phase, text)
        replace_room_field(room_id, 'story_phases',
                           room.get_story_phases())
        return jsonify({'story_phase': room.get_story_by_phase(phase)})
    else:
        return 'cannot regen story by phase', 404


@app.route('/api/regenerate-conclusion', methods=['POST'])
def regenerate_conclusion():
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.regen_conclusion()
        replace_room_field(room_id, 'conclusion', room.get_conclusion())
        return jsonify({'conclusion': room.get_conclusion()}), 200
    else:
        return 'cannot regen room', 404


@app.route('/api/edit-conclusion/<new_conc>', methods=["POST"])
def edit_conclusion(new_conc):
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.set_conclusion_man(new_conc)
        replace_room_field(room_id, 'conclusion', room.get_conclusion())
        return jsonify({'conclusion': room.get_conclusion()}), 200
    else:
        return 'cannot edit conclusion', 404


@app.route('/api/regenerate-failure', methods=['POST'])
def regenerate_failure():
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.regen_failure()
        replace_room_field(room_id, 'failure', room.get_failure())
        return jsonify({'failure': room.get_failure()}), 200
    else:
        return 'cannot regen room', 404


@app.route('/api/edit-failure/<new_failure>', methods=["POST"])
def edit_failure(new_failure):
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.set_failure_man(new_failure)
        replace_room_field(room_id, 'failure', room.get_failure())
        return jsonify({'failure': room.get_failure()}), 200
    else:
        return 'cannot edit failure', 404


@app.route("/api/change-theme/<theme>", methods=["POST"])
def change_theme(theme):
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        room = set_room(room_id)
        room.theme = theme
        replace_room_field(room_id, 'theme', room.theme)
        return '', 200
    else:
        return 'cannot change theme', 404


@app.route('/api/change-puzzle/', methods=['POST'])
def change_puzzle():
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        phase = int(request.json.get('phase'))
        new_puzzle_enum = int(request.json.get('new_puzzle'))
        room = set_room(room_id)
        room.set_puzzle(phase, new_puzzle_enum)
        replace_room_field(room_id, 'puzzles', room.get_puzzles())
        return '', 200
    else:
        return 'cannot change puzzle', 404


@app.route('/api/change-solution/', methods=['POST'])
def change_solution():
    if 'curr_room_id' in session:
        room_id = session['curr_room_id']
        solution = request.json.get('solution')
        phase = int(request.json.get('phase'))
        room = set_room(room_id)
        room.set_solution(phase, solution)
        replace_room_field(room_id, 'solutions', room.get_solutions())
        return '', 200
    else:
        return 'cannot change solution', 404


@app.route('/api/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    account = get_user(email, password)
    if account is not None:
        set_session_details(email, account)
        return jsonify({'creator_id': account})
    else:
        return 'login wrong', 401


@app.route('/api/sign-up', methods=['POST'])
def signUp():
    email = request.json.get('email')
    password = request.json.get('password')
    account = add_user(email, password)
    if account is not None:
        # user.set_details(email, account)
        set_session_details(email, account)
        return jsonify({'creator_id': account})
    else:
        return 'failed to sign up', 401


@app.route('/api/my-rooms', methods=['GET'])
def all_rooms_for_id():
    if "logged_in" in session:
        rooms = get_all_rooms_for_id(session['creator_id'])
        return jsonify({'rooms': rooms})
    else:
        return 'not logged in', 401


@app.route('/api/public-rooms', methods=['GET'])
def public_rooms():
    if "logged_in" in session:
        rooms = get_public_rooms()
        return jsonify({'rooms': rooms})
    else:
        return 'not logged in', 401


@app.route('/api/delete-room/<room_id>', methods=['POST'])
def delete_room(room_id):
    # if user.logged_in:
    if "logged_in" in session:
        deleted = delete_room_with_id(room_id)
        return jsonify({'deleted': deleted})
    else:
        return 'not logged in', 401


@app.route('/api/play-room/<room_id>', methods=['POST'])
def play_room(room_id):
    if is_valid_id(room_id):
        session['curr_room_id'] = room_id
        return jsonify({'done': 1})
    else:
        return 'no room', 404


@app.route('/api/edit-room/<room_id>', methods=['POST'])
def edit_room(room_id):
    session['curr_room_id'] = room_id
    return jsonify({'done': 1})


@app.route('/api/get-pdf/<room_id>', methods=['GET'])
def get_pdf(room_id):
    try:
        session['curr_room_id'] = room_id
        room = set_room(session['curr_room_id'])
        url = room.regen_room()
        return send_file(url, mimetype='application/pdf')
    except Exception:
        return "Error retrieving PDF"


@app.route('/api/get-playing-game-pdf', methods=['GET'])
def get_playing_game_pdf():
    try:
        room = set_room(session['curr_room_id'])
        room.include_storyline = False
        url = room.regen_room()
        room.include_storyline = True
        return send_file(url, mimetype='application/pdf')

    except Exception:
        return "Error retrieving PDF"

# @app.route("/api/change-keywords/<keywords>", methods=["POST"])
# def change_keywords(keywords):
#     global room
#     room.keywords = keywords
#     return '', 200


# @app.route("/api/change-difficulty/<difficulty>", methods=["POST"])
# def change_difficulty(difficulty):
#     global room
#     room.difficulty = difficulty
#     return '', 200


# @app.route("/api/change-length/<length>", methods=["POST"])
# def change_length(length):
#     global room
#     room.length = length
#     return '', 200


# @app.route("/api/change-whitelist/<whitelist>", methods=["POST"])
# def change_whitelist(whitelist):
#     global room
#     room.whitelist = whitelist
#     return '', 200


# @app.route("/api/change-blacklist/<blacklist>", methods=["POST"])
# def change_blacklist(blacklist):
#     global room
#     room.blacklist = blacklist
#     return '', 200


@app.route('/api/room-state')
def get_room_state():
    if 'curr_room_id' in session:
        room = set_room(session['curr_room_id'])
        return jsonify({'id': room.id,
                        'name': room.name,
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
                        })
    else:
        return 'No room', 404


def set_room(room_id):
    room_doc = find_room(room_id)
    theme = Theme(room_doc['theme'])
    keywords = room_doc['keywords']
    difficulty = Difficulty(room_doc['difficulty'])
    length = room_doc['length']
    whitelist = room_doc['whitelist']
    blacklist = room_doc['blacklist']
    room = Room(theme, keywords, difficulty, length,
                whitelist, blacklist, include_storyline=False)
    room.id = str(room_doc['_id'])
    room.name = room_doc['name']
    room.storyline.introduction = room_doc['introduction']
    room.storyline.phases = room_doc['story_phases']
    room.storyline.conclusion = room_doc['conclusion']
    room.storyline.failure = room_doc['failure']
    room.puzzles = room_doc['puzzles']
    room.solutions = room_doc['solutions']
    room.set_solutions(room.solutions)
    room.is_public = room_doc['is_public']
    room.include_storyline = True
    session['curr_room_id'] = room_id
    return room


if __name__ == '__main__':
    port = 8080
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port)
