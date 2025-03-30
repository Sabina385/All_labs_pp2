import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0),(255,0,255)] #(красный, зеленый, синий, черный,пурпурный).
COLOR_BUTTONS = [(10 + i * 40, 10, 30, 30) for i in range(len(COLORS))]
'''
(10 + i * 40, 10, 30, 30) - формула для координат кнопки:

10 + i * 40 - x-координата первой кнопки 10, каждая следующая отстоит на 40 пикселей.

10 - y-координата (все кнопки расположены на одной линии).

30, 30 - ширина и высота кнопки.

(10, 10, 30, 30) - красная
(50, 10, 30, 30) - зеленая
(90, 10, 30, 30) - синяя
4(130, 10, 30, 30) - черная


'''

SHAPES = ["draw", "rect", "circle", "eraser"]
SHAPE_BUTTONS = [(200 + i * 80, 10, 70, 30) for i in range(len(SHAPES))]

'''
(200 + i * 80, 10, 70, 30)- координаты кнопок:

200 + i * 80 - x-координата первой кнопки 200, каждая следующая отстоит на 80 пикселей.

10 - y-координата (все кнопки расположены на одной линии).

70, 30 - ширина и высота кнопки

(200, 10, 70, 30) - кнопка "draw"
(280, 10, 70, 30) - кнопка "rect"
(360, 10, 70, 30) - кнопка "circle"
(440, 10, 70, 30) - кнопка "eraser"


'''

current_color = BLACK
mode = "draw"
start_pos = None # Начальная точка для рисования фигур
last_pos = None #Последняя позиция кисти 
brush_size = 5

#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint in Pygame")

def draw_ui():
    for i, rect in enumerate(COLOR_BUTTONS): #enumerate() позволяет получить индекс (i) и параметры кнопки (rect).
        pygame.draw.rect(screen, COLORS[i], rect) #Рисуем кнопки цветов
        '''
        screen- где рисуем (главный экран).
        COLORS[i]- цвет кнопки (красный, зеленый, синий, черный).
        rect - координаты кнопки (x, y, ширина, высота).
        
        '''
    for i, rect in enumerate(SHAPE_BUTTONS):
        pygame.draw.rect(screen, (200, 200, 200), rect) #Цвет (200, 200, 200) – серый. rect – координаты кнопки.
        font = pygame.font.Font(None, 24) #загружаем шрифт, размер 24px.
        text = font.render(SHAPES[i], True, (0, 0, 0)) #True – включает сглаживание.(0, 0, 0) – цвет текста (черный).
        screen.blit(text, (rect[0] + 5, rect[1] + 5)) #rect[0] + 5 – сдвигаем текст на 5px вправо. rect[1] + 5 – сдвигаем текст на 5px вниз.#Это нужно, чтобы текст не прижимался к краю кнопки.



#screen
canvas = pygame.Surface((WIDTH, HEIGHT)) #отдельная поверхность, на которой рисуются фигуры.(холст)
canvas.fill(WHITE)

running = True
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))#Отрисовываем canvas (на нем сохраняются все нарисованные элементы).
    draw_ui()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # проверяет, была ли нажата любая кнопка мыши.
            x, y = event.pos #event.pos – кортеж с координатами клика (x, y).
            for i, rect in enumerate(COLOR_BUTTONS):
                if pygame.Rect(rect).collidepoint(x, y):
                    current_color = COLORS[i]
            '''
            pygame.Rect(rect) - создает прямоугольник (Rect) c координатами кнопки
            .collidepoint(x, y) - проверяет, попала ли точка (x, y) внутрь этого прямоугольника.
            COLORS[i] - получаем цвет из списка COLORS (по индексу кнопки).
            current_color = COLORS[i] - устанавливаем этот цвет в переменную current_color.
            '''
            for i, rect in enumerate(SHAPE_BUTTONS):
                if pygame.Rect(rect).collidepoint(x, y):
                    mode = SHAPES[i]
            start_pos = event.pos # запоминаем точку начала рисования.
            last_pos = event.pos # запоминаем последнюю позицию.
        elif event.type == pygame.MOUSEBUTTONUP: #содержит координаты точки, где пользователь отпустил кнопку мыши.
            end_pos = event.pos #сохраняем эту точку в переменную end_pos.
            if mode == "rect":
                pygame.draw.rect(canvas, current_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
                '''
                Первый параметр start_pos - верхний левый угол прямоугольника.
                Второй параметр (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]):
                end_pos[0] - start_pos[0] - ширина прямоугольника.
                end_pos[1] - start_pos[1] - высота прямоугольника.
                pygame.draw.rect(canvas, current_color, ..., 2):
                Рисуем прямоугольник на canvas (основном холсте).
                current_color - цвет прямоугольника.
                2 - толщина границы.
                start_pos - координаты точки, где пользователь нажал мышь.
                end_pos - координаты точки, где пользователь отпустил мышь.
                Оба эти значения - это кортежи вида (x, y), где:
                start_pos[0]- координата X начальной точки (левая граница).
                start_pos[1] - координата Y начальной точки (верхняя граница).
                end_pos[0] - координата X конечной точки (правая граница).
                end_pos[1] - координата Y конечной точки (нижняя граница).
                '''
            elif mode == "circle":
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)#Используется формула расстояния между двумя точками по теореме Пифагора.Это означает, что круг будет вписан в воображаемый прямоугольник между start_pos и end_pos.
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2) #start_pos – центр круга (начальная точка).
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]: #MOUSEMOTION (движение мыши) и Левая кнопка мыши зажата
            if mode == "draw":
                pygame.draw.line(canvas, current_color, last_pos, event.pos, brush_size)#Рисуем линию
                pygame.draw.circle(canvas, current_color, event.pos, brush_size // 2)#Рисуем маленький круг в точке event.pos,это нужно, чтобы заполнить возможные пробелы между линиями. brush_size // 2 означает, что радиус круга будет в два раза меньше
                last_pos = event.pos #теперь last_pos – это новая точка. Следующий шаг соединит её с новой позицией, создавая плавное рисование.
            elif mode == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, event.pos, 15)#Толщина ластика – 10.
                pygame.draw.circle(canvas, WHITE, event.pos, 5) #Рисуем маленький круг, чтобы не было пробелов
                last_pos = event.pos #Обновляем предыдущую точку, чтобы ластик продолжал стирать плавно.
    
    pygame.display.flip()

pygame.quit()
sys.exit()