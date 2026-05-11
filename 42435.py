import pygame

class Alien:
    def __init__(self): #파이터 클래스를 만들 때 초기화 작업
        # 비행기 이미지 변수, 경로에 따라 실행 위치를 옮겨야 함
        image = pygame.image.load("assets/images/alien1.png")
         # 이미지 크기 변경
        self.scale_up_image = pygame.transform.scale(
        image, # 어느 이미지를 변경할 것인지
       (image.get_width() * 2, image.get_height() * 2) # 어느 수치만큼 늘릴 것인지
        )
        # 이미지 위치 조정
             # 맵 가로 중앙 - 이미지의 가로 중앙점
        self.x = 0
        self.y = 0
    def draw(self, suface):
        suface.blit(self.scale_up_image, (self.x,self.y))
