from midiutil.MidiFile import *
import pygame
import makeSound as ms

class PlayNotes():
    def __init__():
        degrees = [60, 62, 64, 65, 67, 69, 71, 72]
        track = 0
        channel = 0
        time = 0
        duration = 4
        tempo = 120
        volume = 15
        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)
        for pitch in degrees:
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
            time = time + 2
            volume = volume + 15
        with open("major-scale.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)

        midi_file = 'major-scale.mid'
        freq = 44100  # audio CD quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo
        buffer = 1024  # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(1.0)
        try:
            ms.play_music(midi_file)
        except KeyboardInterrupt:
            # if user hits Ctrl/C then exit
            # (works only in console mode)
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit

