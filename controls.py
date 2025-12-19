from enum import Enum

class Controls(Enum):
    """Перечисление управляющих клавиш игры.

    Args:
        UP    (bytes): Клавиша стрелки вверх (↑)
        DOWN  (bytes): Клавиша стрелки вниз (↓)
        LEFT  (bytes): Клавиша стрелки влево (←)
        RIGHT (bytes): Клавиша стрелки вправо (→)
        QUIT  (bytes): Клавиша выхода из игры ('q')
    """

    UP = b'H'
    DOWN = b'P'
    LEFT = b'K'
    RIGHT = b'M'
    QUIT = b'q'

    @property
    def key(self):
        """Возвращает байтовое значение клавиши.

        Returns:
                bytes: Значение клавиши.
        """

        return self.value