import os
from flask import Flask, request, jsonify, send_file
import random

from Game import Game

app = Flask(__name__)

ongoing_games = {}

@app.route('/newGame/', methods=['GET'])
def newGame():
    words = ['Augusto', 'Queiroz', 'Hugo', 'Lispector', 'Erik', 'Zambom', 'Pedro', 'Brant', 'Danilo', 'Freitas', 'Andre', 'Neto', 'Yuri', 'Monteiro']
    random.shuffle(words)
    game_id = ''.join(words[:3])

    songs = os.listdir('songs')
    random.shuffle(songs)
    song_path = 'songs/' + songs[0] # Randomly choose a song
    ongoing_games[game_id] = Game(game_id, song_path)
    ongoing_games[game_id].dismorph()

    return jsonify({'gameID': game_id})

@app.route('/game/<game_id>/getSong', methods=['GET'])
def get_song(game_id):
    try:
        song_path = ongoing_games[game_id].get_song()
        return send_file(song_path, attachment_filename='%s.mid' % game_id)
    except KeyError:
        return 'The provided GameID does not match any ongoing game.', 404

@app.route('/game/<game_id>/changeTempo', methods=['GET'])
def change_tempo(game_id):
    #request.form['speedScalingFactor']
    try:
        ongoing_games[game_id].change_tempo(float(request.args.get('speedScalingFactor', None)))
        song_path = ongoing_games[game_id].get_song()
        return send_file(song_path, attachment_filename='%s.mid' % game_id)
    except KeyError: # The provided game id does not exist
        return 'The provided GameID does not match any ongoing game.', 404

@app.route('/game/<game_id>/changePitch', methods=['GET'])
def change_pitch(game_id):
    #request.form['transposeValue']
    try:
        ongoing_games[game_id].change_pitch(int(request.args.get('transposeValue', 0)))
        song_path = ongoing_games[game_id].get_song()
        return send_file(song_path, attachment_filename='%s.mid' % game_id)
    except KeyError: # The provided game id does not exist
        return 'The provided GameID does not match any ongoing game.', 404

@app.route('/game/<game_id>/shiftInstruments', methods=['GET'])
def shift_instruments(game_id):
    try:
        ongoing_games[game_id].shift_instruments(request.args.get('shift_right', False))
        song_path = ongoing_games[game_id].get_song()
        return send_file(song_path, attachment_filename='%s.mid' % game_id)
    except KeyError: # The provided game id does not exist
        return 'The provided GameID does not match any ongoing game.', 404

@app.route('/game/<game_id>/confirmAnswer', methods=['GET'])
def confirm_answer(game_id):
    try:
        game = ongoing_games[game_id]
        return jsonify({
            'result': game.is_solved(),
            'final_speed_scaling_factor': game.speed_scaling_factor,
            'final_transpose_value': game.transpose_value,
            'final_number_of_shifts': game.times_shifted
            })
    except KeyError: # The provided game id does not exist
        return 'The provided GameID does not match any ongoing game.', 404

if __name__ == '__main__':
    app.run(threaded=True, port=5000)