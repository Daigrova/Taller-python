from GameObjects import *

screen = Screen()

background = Background(screen.get_size()[0], screen.get_size()[1])


cursor = Finger()
face = Face(background.get_bg() )
screen.add_objects_screen(cursor, face)

clock = pygame.time.Clock()

screen.screen_update(background.get_bg())


while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            if cursor.click(face):
                face.isClicked()
                


        elif event.type == MOUSEBUTTONUP:
            cursor.unclick()
            if face.clicked:
                face.unclicked()


    screen.screen_update(background.get_bg())
    clock.tick(60)

