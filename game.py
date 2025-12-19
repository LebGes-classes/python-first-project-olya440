import os
import time
import msvcrt
from snake import (
    Snake,
)
from food import (
    Food,
)
from points import (
    Point,
)
from controls import (
    Controls,
)
from game_commands import (
    GameCommands,
)
from direction import (
    Direction,
)

MOVE_DELAY_INITIAL = 0.3    # Константа задержки движения
MOVE_DELAY_DECREMENT = 0.05 # Константа задержки движения
MIN_MOVE_DELAY = 0.1        # Константа задержки движения

class Game:
    """Управляет основной логикой игры."""

    def __init__(self, width=20, height=10):
        """Инициализация игры.

        Args:
            width (int): Ширина поля. Значение по умолчанию 20.
            height (int): Высота поля. Значение по умолчанию 10.
        """

        self.width = width
        self.height = height
        self.score = 0
        self.level = 0
        self.state = GameCommands.MENU

    def draw(self):
        """Отрисовывает игровое поле в консоли."""

        field = [[' ' for _ in range(self.width)] for _ in range(self.height)] # Создаём пустое поле

        for segment in self.snake.body[1:]: # Рисуем тело змейки
            if 0 <= segment.x < self.width and 0 <= segment.y < self.height:
                field[segment.y][segment.x] = '█'

        head = self.snake.head() # Рисуем голову
        if 0 <= head.x < self.width and 0 <= head.y < self.height:
            field[head.y][head.x] = '■'

        if 0 <= self.food.position.x < self.width and 0 <= self.food.position.y < self.height: # Рисуем яблочки (это я запомнила, что Вы сказали, что она их ест)
            field[self.food.position.y][self.food.position.x] = '●'

        os.system('cls' if os.name == 'nt' else 'clear') # Очистка консоли

        print('┌' + '─' * self.width + '┐') # Вывод
        for row in field:
            print('│' + ''.join(row) + '│')
        print('└' + '─' * self.width + '┘')
        print(f"Счёт: {self.score} | Уровень: {self.level + 1} | Управление: Arrows | Выход: Q")

    def handle_input(self):
        """Обрабатывает нажатия клавиш пользователя."""

        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in (b'\x00', b'\xe0'):
                key = msvcrt.getch()
                if key == Controls.UP.key:      # Верхняя стрелка
                    self.snake.change_direction(Direction.UP)
                elif key == Controls.DOWN.key:    # Нижняя стрелка
                    self.snake.change_direction(Direction.DOWN)
                elif key == Controls.LEFT.key:    # Левая стрелка
                    self.snake.change_direction(Direction.LEFT)
                elif key == Controls.RIGHT.key:    # Правая стрелка
                    self.snake.change_direction(Direction.RIGHT)
            elif key == Controls.QUIT.key:        # Выход
                self.state = GameCommands.MENU

    def update(self):
        """Обновляет состояние игры: движение, проверка столкновений, рост."""

        self.snake.move()

        if self.snake.check_collision(self.width, self.height):
            self.state = GameCommands.OVER

            return

        if self.snake.head() == self.food.position:
            if len(self.snake.body) % 3 == 0:
                self.level += 1
            self.snake.grow()
            self.food.respawn(self.width, self.height, self.snake.body)
            self.score += 1

    def run(self):
        """Запускает основной игровой цикл."""

        start_pos = Point(self.width // 2, self.height // 2)
        self.snake = Snake(start_pos)
        self.snake.move_delay = MOVE_DELAY_INITIAL # Обновляем начальную задержку змейки из константы
        self.food = Food(self.width, self.height, self.snake.body)

        while self.state == GameCommands.RUN:
            self.handle_input()
            self.update()
            self.draw()
            time.sleep(self.snake.move_delay)

    def execute(self):
        """Основной исполнительный цикл игры, управляющий состояниями."""

        from menu import Menu  # Импорт внутри метода, чтобы избежать циклической зависимости
        menu = Menu(self.width, self.height)

        while True:
            if self.state == GameCommands.MENU:
                self.state = menu.show()
            elif self.state == GameCommands.SHOW_RULES:
                menu.show_rules()
                self.state = GameCommands.MENU
            elif self.state == GameCommands.RUN:
                self.run()
            elif self.state == GameCommands.QUIT:
                print("До свидания!")
                break
            elif self.state == GameCommands.OVER:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("💀 ИГРА ОКОНЧЕНА!")
                print(f"Ваш счёт: {self.score}")
                print("Нажмите любую клавишу для возврата в меню...")
                time.sleep(1)
                msvcrt.getch()
                self.state = GameCommands.MENU