import music21

class Game:
    def __init__(self, song_path: str):
        self.song = music21.converter.parse(song_path)

    def dismorph(self):
        # generate the disturbances to the original song
        pass

    def change_tempo(self, speed_scaling_factor):
        # Change the tempo of the song
        pass

    def change_pitch(self, transpose_value: int):
        # Change the pitch of the song
        pass

    def is_solved(self) -> bool:
        # Verify if the song has been correctly resolved
        return False