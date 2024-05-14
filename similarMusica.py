import pygame
import os
class SimilarMusica:
    def __init__(self):
        
        self.playing = False
        self.playback_position = None
        self.song_list = []
        self.current_index = 0
        self.previous_pos = 0
        self.song_length = 0

    def play_pause(self):
        print("Botón de reproducción/pausa presionado")
        if pygame.mixer.music.get_busy():
            if self.playing:
                print("Pausando la reproducción")
                pygame.mixer.music.pause()
                self.playing = False
                self.playback_position = pygame.mixer.music.get_pos() / 1000
            else:
                print("Reanudando la reproducción")
                pygame.mixer.music.unpause()
                self.playing = True
                if self.playback_position is not None:
                    print(f"Reanudando desde la posición: {self.playback_position}")
                    pygame.mixer.music.set_pos(self.playback_position)
        else:
            if self.playback_position is not None:
                print("Reanudando desde la posición donde se pausó")
                pygame.mixer.music.play(start=self.playback_position)
                self.playing = True
            else:
                print("No hay música reproduciéndose")


    def next_song(self):
        if self.song_list:
            self.previous_pos = 0
            self.current_index = (self.current_index + 1) % len(self.song_list)
            self.play_selected_song(self.song_list[self.current_index])


    def prev_song(self):
        if self.song_list:
            self.previous_pos = 0
            self.current_index = (self.current_index - 1) % len(self.song_list)
            self.play_selected_song(self.song_list[self.current_index])

    def play_selected_song(self, song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.current_song.set(os.path.basename(song))
        self.song_length = pygame.mixer.Sound(song).get_length()
        self.playing = True
        self.update_progress()

   