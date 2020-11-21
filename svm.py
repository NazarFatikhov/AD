import numpy as np
import pygame
from sklearn import svm


def get_line(points, cluster):
    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(points, cluster)

    # получение коэффицентов w и b из (w * x - b = 0)
    weights = clf.coef_[0]
    w = weights[0]
    b = weights[1]

    # Описываем нахождение прямой по двум координатам.
    x_line = np.linspace(0, 600, 2)
    y_line = (- w * x_line - (clf.intercept_[0])) / b

    return x_line, y_line


pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))
pygame.display.update()

points = []
cluster = []

play = True

while play:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(screen, (255, 0, 0), i.pos, 10)
                points.append(i.pos)
                cluster.append(1)
            elif i.button == 3:
                pygame.draw.circle(screen, (0, 255, 0), i.pos, 10)
                points.append(i.pos)
                cluster.append(0)
            elif i.button == 2:
                screen.fill((255, 255, 255))
                points = []
                cluster = []
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_r:
                x_line_coords, y_line_coords = get_line(points, cluster)
                pygame.draw.line(screen, (0, 0, 0),
                                 (x_line_coords[0], y_line_coords[0]),
                                 (x_line_coords[1], y_line_coords[1]))
        pygame.display.update()
