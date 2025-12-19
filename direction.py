from enum import Enum


class Direction(Enum):
    """Направления движения. Каждое — это вектор (dx, dy).

    Args:
        UP: Направление вверх, вектор (0, -1)
        DOWN: Направление вниз, вектор (0, 1)
        LEFT: Направление влево, вектор (-1, 0)
        RIGHT: Направление вправо, вектор (1, 0)
    """

    UP = (0, -1)    # y уменьшается → вверх
    DOWN = (0, 1)   # y увеличивается → вниз
    LEFT = (-1, 0)  # x уменьшается → влево
    RIGHT = (1, 0)  # x увеличивается → вправо

    @property
    def delta(self): #приращение координат при движении в этом направлении.
        """Возвращает (dx, dy) как кортеж.

        Returns:
            tuple: Вектор смещения (dx, dy).
        """

        return self.value

    def opposite(self):
        """Возвращает противоположное направление.

        Returns:
            Direction: Противоположное направление.
        """

        if self == Direction.UP:

            return Direction.DOWN

        if self == Direction.DOWN:

            return Direction.UP

        if self == Direction.LEFT:

            return Direction.RIGHT

        return Direction.LEFT


