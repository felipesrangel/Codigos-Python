import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex0021.mp3')
pygame.mixer.music.play()
input()
pygame.mixer.wait()
