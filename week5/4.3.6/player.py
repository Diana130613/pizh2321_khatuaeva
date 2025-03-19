from abc import ABC, abstractmethod


class Player(ABC):
    """
    Абстрактный класс Player с базовыми методами play() и stop().
    """
    @abstractmethod
    def play(self) -> None:
        """Запуск воспроизведения."""
        ...

    @abstractmethod
    def stop(self) -> None:
        """Остановка воспроизведения."""
        ...


class AudioPlayer(Player):
    def __init__(self, title: str, duration: int):
        self.title = title
        self._duration = duration
        self._volume = 50
        self._is_playing = False

    def play(self) -> None:
        self._is_playing = True
        print(f"Воспроизведение аудио: {self.title} длительностю в: {self._duration} секунд на уровне громкости {self._volume}.")

    def stop(self) -> None:
        self._is_playing = False
        print(f"Воспроизведение {self.title} остановлено.")

    def set_volume(self, volume: int) -> None:
        """Установить уровень громкости (общедоступный метод)"""
        if 0 <= volume <= 100:
            self._volume = volume
            print(f"Громкость установлена на {self._volume}.")
        else:
            print("Установите громкость от 0 до 100.")


class VideoPlayer(Player):
    def __init__(self, title: str, duration: int, resolution: str):
        self.title = title
        self._duration = duration
        self._volume = 50
        self._is_playing = False
        self.resolution = resolution

    def play(self) -> None:
        self._is_playing = True
        print(f"Воспроизведение видео: {self.title} длительностю в: {self._duration} секунд в разрешении {self.resolution} на уровне громкости {self._volume}.")

    def stop(self) -> None:
        self._is_playing = False
        print(f"Видео {self.title} остановлено.")

    def set_volume(self, volume: int) -> None:
        """Установить уровень громкости (общедоступный метод)"""
        if 0 <= volume <= 100:
            self._volume = volume
            print(f"Громкость видео установлена на {self._volume}.")
        else:
            print("Пожалуйста, установите громкость от 0 до 100.")


class DvdPlayer(Player):
    def __init__(self, title: str):
        self.title = title
        self._current_position = 0
        self._is_playing = False

    def play(self, position: int = 0) -> None:
        if not self._is_playing:
            self._is_playing = True
            self._current_position = position
            print(f"Воспроизведение DVD: {self.title} с позиции {self._current_position}.")
        else:
            print(f"DVD {self.title} уже воспроизводится с позиции {self._current_position}.")

    def stop(self) -> None:
        if self._is_playing:
            self._is_playing = False
            print(f"DVD {self.title} остановлено на позиции {self._current_position}.")
        else:
            print(f"DVD {self.title} не воспроизводится.")

    def set_position(self, position: int) -> None:
        """Установить текущую позицию воспроизведения (общедоступный метод)"""
        if position >= 0:
            self._current_position = position
