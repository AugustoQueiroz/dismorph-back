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

    def change_tempo(self, speed_scaling_factor):
        # Change the tempo of the song
        pass

    def change_pitch(self, transpose_value: int):
        # Change the pitch of the song
        pass

    def is_solved(self) -> bool:
        # Verify if the song has been correctly resolved
        return False

    def get_song(self):
        return