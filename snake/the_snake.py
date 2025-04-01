from random import randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
CENTER_POSITION = ((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Цвет текста
TEXT_COLOR = (255, 0, 0)

# Скорость движения змейки:
SPEED = 13

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """
    Базовый класс для игровых объектов.

    Атрибуты:
        position: Координата центра объекта.
        body_color: Цвет объекта.
    """

    def __init__(self) -> None:
        """Инициализация объекта."""
        self.position = CENTER_POSITION
        self.body_color = None

    def draw(self):
        """Отрисовка объекта."""
        pass


class Apple(GameObject):
    """
    Класс для представления яблока.

    Атрибуты:
        position: Координата яблока.
        body_color: Цвет яблока.
    """

    def __init__(self) -> None:
        """Инициализация яблока."""
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self) -> None:
        """Установка случайной позиции яблока. """
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )

    def draw(self):
        """Рисование яблока на игровом поле."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """
    Класс для представления змеи.

    Атрибуты:
        length: Длина змейки.
        positions: Список позиций сегментов змейки.
        direction: Текущее направление движения.
        next_direction: Следующее направление движения.
        body_color: Цвет змейки.
    """

    def __init__(self) -> None:
        """Инициализация змеи."""
        self.length = 1
        self.position = None
        self.positions = [CENTER_POSITION]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR

    def update_direction(self) -> None:
        """Обновление текущего направления движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Перемещение змейки на один шаг вперед."""
        if len(self.positions) > self.length:
            self.positions.pop()

        self.update_direction()
        hx, hy = self.get_head_position()
        dx, dy = self.direction
        new_x = (hx + dx * GRID_SIZE) % SCREEN_WIDTH
        new_y = (hy + dy * GRID_SIZE) % SCREEN_HEIGHT
        new_position = (new_x, new_y)
        if len(self.positions) > 1:
            self.last = self.positions[-1]
        else:
            self.last = None
        self.positions.insert(0, new_position)

    def draw(self):
        """Отрисовка змейки на экране."""
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self) -> tuple[int, int]:
        """Возвращение координаты головы."""
        return self.positions[0]

    def reset(self):
        """Сброс состояние до начального."""
        self.__init__()


def handle_keys(game_object):
    """Обработка событий клавиатуры."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """ Основная функция программы."""
    pygame.init()
    apple = Apple()
    snake = Snake()

    font = pygame.font.SysFont(None, 24)

    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.move()

        pygame.display.update()

        # Если змейка попадает на яблоко
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            while apple.position in snake.positions:
                apple.randomize_position()
        length = font.render("Длина: {}".format(snake.length), True, TEXT_COLOR)

        # Проверка на столкновение с собой
        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        screen.blit(length, (5, 5))
        pygame.display.update()


if __name__ == '__main__':
    main()
