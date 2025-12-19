import os
import msvcrt
from controls import (
    Controls,
)
from game_commands import (
    GameCommands,
)

class Menu:
    """Предоставляет пользовательское меню."""

    def __init__(self, width=20, height=10):
        """Инициализирует объект меню.

        Args:
            width (int): Ширина меню.
            height (int): Высота меню.
        """

        self.options = [("start", GameCommands.RUN), ("rules", GameCommands.SHOW_RULES), ("quit", GameCommands.QUIT)]
        self.selected = 0 # изначально выбран первый пункт ("start")
        self.width = width
        self.height = height

    def clear(self):
        """Очищает консоль."""

        os.system("cls")

    def draw(self):
        """Отрисовывает меню в консоли."""

        self.clear()

        menu_lines = []  # подготовка строк меню
        for i, option in enumerate(self.options):
            text = option[0]
            if i == self.selected:
                menu_lines.append(f"[ {text} ]") # выделенный пункт в скобках
            else:
                menu_lines.append(f"  {text}  ") # обычный пункт 

        title = "SNAKE" # расчёт вертикального центрирования

        content_height = 1 + len(menu_lines)   # заголовок + опции
        top_padding = (self.height - content_height) // 2

        print("┌" + "─" * self.width + "┐") # верхняя рамка

        for row in range(self.height): # внутренняя область
            line = ""

            if row == top_padding:  # строка с заголовком
                line = title.center(self.width)

            elif top_padding < row <= top_padding + len(menu_lines): # опции меню
                menu_index = row - top_padding - 1
                line = menu_lines[menu_index].center(self.width)

            else: 
                line = " " * self.width # пустое пространство

            print("│" + line + "│")

        print("└" + "─" * self.width + "┘") # нижняя рамка

    def handle_input(self):
        """Обрабатывает ввод пользователя и обновляет состояние меню.

        Returns:
            GameCommands or None: Выбранная команда или None, если выбор не сделан.
        """

        key = msvcrt.getch() #возвращает байт, соответствующий нажатой клавише, без Enter

        if key in (b"\x00", b"\xe0"): # обработка специальных клавиш (стрелки)
            key = msvcrt.getch()

            if key == Controls.UP.key:
                self.selected = (self.selected - 1) % len(self.options) # позволяет переходить с первого пункта на последний при движении вверх
            elif key == Controls.DOWN.key:
                self.selected = (self.selected + 1) % len(self.options) # позволяет переходить с последнего пункта на первый при движении вниз

        elif key == b"\r": # код клавиши Enter
            return self.options[self.selected][1]

        return None

    def show(self): # бесконечно рисует меню и ждёт ввода
        """Отображает меню и обрабатывает ввод до выбора опции.

        Returns:
            GameCommands: Выбранная команда пользователя.
        """

        while True:
            self.draw()
            choice = self.handle_input()

            if choice:
                return choice

    def show_rules(self):
        """Отображает правила игры и ждёт нажатия любой клавиши."""

        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            '\n ПРАВИЛА:\n'
            '- Управляйте змейкой с помощью стрелок.\n'
            '- Ешьте еду (●), чтобы расти и набирать очки.\n'
            '- Не врезайтесь в стены или в своё тело.\n'
            '- Во время игры нажмите Q, чтобы выйти.\n'
            'Нажмите любую клавишу, чтобы вернуться в меню.\n'
        )


        msvcrt.getch() # ожидание нажатия любой клавиши
