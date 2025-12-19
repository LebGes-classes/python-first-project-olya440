from enum import Enum

class GameCommands(Enum):
    """Перечисление команд для управления состоянием игры.

    Attributes:
        MENU (int): Главное меню.
        RUN (int): Игровой процесс.
        OVER (int): Игра окончена.
        SHOW_RULES (int): Просмотр правил.
        QUIT (int): Выход из игры.
    """

    MENU = 0
    RUN = 1
    OVER = 2
    SHOW_RULES = 3
    QUIT = 4