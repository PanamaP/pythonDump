# Elfar Snær Arnarson
# 27. April 2020
# Lokaverkefni

import pygame
import sys
from pygame import *
from os import path

vec = pygame.math.Vector2

#To open map
import pytmx


#  Video settings
WIDTH = 1024
HEIGHT = 768
TILESIZE = 32
window_size = WIDTH, HEIGHT

GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
#  Player settings
P_SPEED = 200
P_IMG = 'tile_0004.png'
P_gravity = 0.8

##

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def get_key(self):
        self.vel = vec(0, 0)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[K_a]:
            self.vel.x = -P_SPEED
        if key[pygame.K_RIGHT] or key[K_d]:
            self.vel.x = P_SPEED
        if key[pygame.K_UP] or key[K_w]:
            self.vel.y = -P_SPEED
        if key[pygame.K_DOWN] or key[K_s]:
            self.vel.y = P_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def update(self):
        self.get_key()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        if self.rect.right > 1600:
            self.rect.right = 1600
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 960:
            self.rect.bottom = 960
        if self.rect.top < 0:
            self.rect.top = 0



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Lokaverkefni")
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        folder = path.dirname(__file__)
        img_folder = path.join(folder, 'img')
        map_folder = path.join(folder, 'maps')
        self.map = TileMap(path.join(map_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pygame.image.load(path.join(img_folder, P_IMG)).convert_alpha()

    def new(self):
        self.allSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'Player':
                self.player = Player(self, tile_object.x, tile_object.y)
            self.camera = Camera(self.map.width, self.map.height)
        self.pause = False

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000
            self.events()
            if self.pause == False:
                self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.allSprites.update()
        self.camera.update(self.player)

    def paused(self):
        bigFont = pygame.font.Font(pygame.font.get_default_font(), 115)
        smallFont = pygame.font.Font(pygame.font.get_default_font(), 25)
        screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

        pauseText = bigFont.render("Paused", 1, (255, 255, 255))
        pauseBox = Rect(300, 300, 80, 30)
        pauseTextLower = smallFont.render("Click 'p' to resume", 1, (255, 255, 255))
        pauseLowBox = Rect(310, 400, 80, 30)

        pygame.draw.rect(screen, (0, 0, 255), pauseBox)
        self.screen.blit(pauseText, pauseBox)

        pygame.draw.rect(screen, (0, 0, 0), pauseLowBox)
        self.screen.blit(pauseTextLower, pauseLowBox)

    def draw(self):
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.allSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        if self.pause:
            self.paused()
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_p:
                    if self.pause == False:
                        self.pause = True
                    elif self.pause == True:
                        self.pause = False




class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class TileMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)


    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - WIDTH), x)
        y = max(-(self.height - HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)


g = Game()
while True:
    g.new()
    g.run()
