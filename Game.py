import random
import music21

class Game:
    def __init__(self, id: str, song_path: str):
        self.id = id
        self.song = music21.converter.parse(song_path)

    def dismorph(self):
        # generate the disturbances to the original song
        self.speed_scaling_factor = random.randint(0, 100)
        self.transpose_value = random.randint(-100, 100)
                        # TODO - Fix these values ^

    def change_tempo(self, speed_scaling_factor: float):
        # Change the tempo of the song
        self.song = self.song.scaleOffsets(speed_scaling_factor).scaleDurations(speed_scaling_factor)

    def change_pitch(self, transpose_value: int):
        # Change the pitch of the song
        for part in self.song.parts:
            for pitch in part.pitches:
                pitch.transpose(transpose_value, inPlace=True)
        
        self.transpose_value += transpose_value

    def is_solved(self) -> bool:
        # Verify if the song has been correctly resolved
        return False

    def get_song(self):
        song_path = './ongoing_game_songs/%s.mid' % self.id
        self.song.write('midi', song_path)
        return song_path