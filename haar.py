from cv2 import imread
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle
# Загружаем фотокарточку
pixels = imread('test4.jpg')
# Загружаем результаты тренеровок в классификатор
classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
# Формируем рамку на основе фотографии
bboxes = classifier.detectMultiScale(pixels)
for box in bboxes:
    x, y, width, height = box
    x2, y2 = x + width, y + height
    rectangle(pixels, (x, y), (x2, y2), (0,0,255), 1)
# Показываем результат
imshow('face detection', pixels)
# Закрытие окна на нажатие кнопки
waitKey(0)
# close the window
destroyAllWindows()