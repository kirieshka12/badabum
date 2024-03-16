from pygame import *
window = display.set_mode((700,500))
display.set_caption('Догонялки')
background = transform.scale(image.load('iraq.png'), (700, 500))
sprite1 = transform.scale(image.load('leha.png'), (100,100))
sprite2 = transform.scale(image.load('obamka.png'), (100,100))
#window.blit(background, (0, 0))
x1 = 0
y1 = 400

x2 = 300
y2 = 400
clock = time.Clock()
FPS = 60
game = True

while game:
    window.blit(background, (0,0))
    window.blit(sprite1, (x1,y1))
    window.blit(sprite2, (x2,y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    key_pressed = key.get_pressed()
    if key_pressed[K_UP]:
        y2 -= 10
    if key_pressed[K_DOWN]:
        y2 += 10
    if key_pressed[K_RIGHT]:
        x2 += 10
    if key_pressed[K_LEFT]:
        x2 -= 10
  
    if key_pressed[K_w]:
        y1 -= 10
    if key_pressed[K_s]:
        y1 += 10
    if key_pressed[K_d]:
        x1 += 10
    if key_pressed[K_a]:
        x1 -= 10



    
    display.update()
    clock.tick(FPS)