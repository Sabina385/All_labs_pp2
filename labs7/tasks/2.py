import pygame


pygame.init()

LovesongPath=r"C:\Users\ACER\Desktop\All_labs_PP2\music\Adele_-_Lovesong_12493379.mp3"
UnforgettablePath=r"C:\Users\ACER\Desktop\All_labs_PP2\music\French_Montana_feat_Swae_Lee_-_Unforgettable_56818388.mp3"
dimondsPath=r"C:\Users\ACER\Desktop\All_labs_PP2\music\Rihanna_-_Diamonds_48197562.mp3"

screen=pygame.display.set_mode((406,600))
pygame.display.set_caption("MP3 PLAYER")

BG_COLOR = (255, 255, 255)
clock=pygame.time.Clock()
image=pygame.image.load(r"C:\Users\ACER\Desktop\All_labs_PP2\play_pause-1024.webp")
image = pygame.transform.scale(image, (406, 600))

musicList = [LovesongPath, UnforgettablePath,dimondsPath]
pygame.mixer.music.load(musicList[0]) 

pygame.mixer.music.play(-1)

Play=False
running=True

musicNames = ["Lovesong-Adele", "Unforgettable", "Rihanna-Diamonds"]

font = pygame.font.SysFont(None, 31)

index=0
while running:
    screen.fill(BG_COLOR)  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             running=False
             
    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                Play=not Play
                
                if Play:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause() 
                    
            elif event.key==pygame.K_RIGHT:
                index+=1
                if index==len(musicList):
                    index=0
                pygame.mixer.music.load(musicList[index])   
                pygame.mixer.music.play() 
                
            elif event.key==pygame.K_LEFT:
                index-=1
                if index==-1:
                    index=len(musicList)-1
                pygame.mixer.music.load(musicList[index])   
                pygame.mixer.music.play()  
    screen.blit(image,(0,0))
    pygame.draw.rect(screen, (0, 0, 0), (20, 20, 200, 40))
    text_surface = font.render(musicNames[index], True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))
                
    pygame.display.flip()   
    clock.tick(60)