class Point:
    def __init__(self, x, y):
        """Инициализация точки.

        Args:
            x (int): Координата по горизонтали.
            y (int): Координата по вертикали.
        """

        self.x = x
        self.y = y

    def __eq__(self, other):
        """Сравнение двух точек по координатам.

        Args:
            other (Point): Другая точка.

        Returns:
            bool: True, если координаты совпадают, иначе False.
        """

        return self.x == other.x and self.y == other.y

