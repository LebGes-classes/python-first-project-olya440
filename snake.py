from points import (
    Point,
)
from direction import (
    Direction,
)


class Snake:
    """Змейка: список точек (тело), голова — первый элемент."""

    def __init__(self, start_pos):
        """Инициализация змейки длиной 3.

        Args:
            start_pos (Point): Начальная позиция головы.
        """
        self.body = [
            start_pos,
            Point(start_pos.x - 1, start_pos.y),
            Point(start_pos.x - 2, start_pos.y)
        ]
        self.direction = Direction.RIGHT  # изначально движется вправо
        self.move_delay = 0.3  # используется константа из game.py, но значение вставлено напрямую

    def move(self):
        """Перемещает змейку на одну клетку в текущем направлении."""

        head = self.body[0]
        dx, dy = self.direction.delta
        new_head = Point(head.x + dx, head.y + dy)
        self.body.insert(0, new_head)  # добавляем новую голову в начало
        self.body.pop()  # удаляем последний элемент (хвост)

    def grow(self):
        """Увеличивает длину змейки, добавляя копию хвоста."""
        
        self.body.append(Point(self.body[-1].x, self.body[-1].y))

    def change_direction(self, direction):
        """Меняем направление, но нельзя поворачиваться на 180 градусов.

        Args:
            direction (Direction): Новое направление движения.
        """
        
        if direction == self.direction:

            return

        if direction == self.direction.opposite():

            return

        self.direction = direction

    def head(self):
        """Возвращает голову змейки.

        Returns:
            Point: Текущая позиция головы.
        """

        return self.body[0]

    def check_collision(self, width, height):
        """Проверяет столкновение со стеной или с собой.

        Args:
            width (int): Ширина игрового поля.
            height (int): Высота игрового поля.

        Returns:
            bool: True, если произошло столкновение.
        """

        head = self.head()
        
        if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height: # столкновение со стеной

            return True

        if head in self.body[1:]: # столкновение с собой

            return True


        return False
