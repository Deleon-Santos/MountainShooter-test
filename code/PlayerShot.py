import pygame
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        try:
            self.sound = pygame.mixer.Sound('./asset/tiro3.flac')
        except pygame.error as e:
            print(f"Erro ao carregar o som de disparo: {e}")
            self.sound = None  # Trata o erro para evitar que o programa crashe
        

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]
        if self.sound:  # Verifica se o som foi carregado com sucesso.
            self.sound.set_volume(0.1)
            self.sound.play()
