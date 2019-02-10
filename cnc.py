#!/usr/bin/env python 
import time
import socket
import pygame
from pygame.locals import *

HOST = '192.168.4.1'
PORT = 80
ADDR = (HOST,PORT)
BUFSIZE = 4096

def display(str):
    text = font.render(str, True, (255, 255, 255), (159, 182, 205))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery

    screen.blit(text, textRect)
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode( (640,480) )
pygame.display.set_caption('Python numbers')
screen.fill((159, 182, 205))

font = pygame.font.Font(None, 17)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
	client.send('w')
    elif keys[K_DOWN]:
	client.send('s')
    elif keys[K_LEFT]:
	client.send('a')
    elif keys[K_RIGHT]:
	client.send('d')
    elif keys[K_ESCAPE]:
	break
    time.sleep(0.05)

client.close()
