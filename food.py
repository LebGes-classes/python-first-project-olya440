import random
from points import (
    Point,
)

class Food:
    """Еда — одна точка на поле."""

    def __init__(self, width, height, snake_body):
        """Инициализирует позицию еды.

        Args:
            width (int): Ширина поля.
            height (int): Высота поля.
            snake_body (list[Point]): Текущее тело змейки.
        """

        self.position = self._generate_position(width, height, snake_body)

    def _generate_position(self, width, height, snake_body):
        """Генерирует случайную позицию, не совпадающую со змейкой.

        Args:
            width (int): Ширина поля.
            height (int): Высота поля.
            snake_body (list[Point]): Текущее тело змейки.

        Returns:
            Point: Новая позиция еды.
        """

        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pos = Point(x, y)
            if pos not in snake_body:
                return pos

    def respawn(self, width, height, snake_body):
        """Перемещает еду в новое место.

        Args:
            width (int): Ширина поля.
            height (int): Высота поля.
            snake_body (list[Point]): Текущее тело змейки.
        """

        self.position = self._generate_position(width, height, snake_body)