import random
import music21

class Game:
    def __init__(self, id: str, song_path: str):
        self.id = id
        self.song = music21.converter.parse(song_path)

    def __get_song_instruments(self):
        instruments = []
        for i in self.song.recurse():
            if "Instrument" in i.classes:
                instruments.append(i)
        return instruments

    def dismorph(self):
        # generate the disturbances to the original song
        self.speed_scaling_factor = random.random() * random.randint(1, 5)
                        # TODO - Fix these values ^
        self.change_tempo(self.speed_scaling_factor)
        self.transpose_value = random.randint(-100, 100)
                        # TODO - Fix these values ^
        self.change_pitch(self.transpose_value)
        self.times_shifted = 0
        # for _ in range(random.randint(1, len(self.__get_song_instruments())-1)):
        #     self.shift_instruments()

    def change_tempo(self, speed_scaling_factor: float):
        # Change the tempo of the song
        self.song = self.song.scaleOffsets(speed_scaling_factor).scaleDurations(speed_scaling_factor)
        self.speed_scaling_factor *= speed_scaling_factor

    def change_pitch(self, transpose_value: int):
        # Change the pitch of the song
        for part in self.song.parts:
            for pitch in part.pitches:
                pitch.transpose(transpose_value, inPlace=True)
        
        self.transpose_value += transpose_value

    def shift_instruments(self, shift_right=False):
        instruments = self.__get_song_instruments()

        if len(instruments) <= 1:
            return self.song

        if shift_right:
            lastElement = instruments.pop(-1)
            instruments.insert(0, lastElement)
            self.times_shifted = (self.times_shifted + 1) % len(instruments)
        else: # shift_left
            firstElement = instruments.pop(0)
            instruments.append(firstElement)
            self.times_shifted = self.times_shifted - 1 if self.times_shifted > 0 else len(instruments) - 1

        count = 0
        for i in self.song.recurse():
            if "Instrument" in i.classes:
                i.midiProgram = instruments[count].midiProgram
                count = count + 1

    def is_solved(self) -> bool:
        # Verify if the song has been correctly resolved
        return (self.speed_scaling_factor == 1) and (self.transpose_value == 0) and (self.times_shifted == 0)

    def get_song(self):
        song_path = './ongoing_game_songs/%s.mid' % self.id
        self.song.write('midi', song_path)
        return song_path