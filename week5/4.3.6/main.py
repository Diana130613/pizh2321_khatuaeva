# Программирование на языке высокого уровня (Python).
# Задание №4.3.1. Вариант 6
#
# Выполнила: Хатуаева Д.Т.
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dana.khatuaeva@gmail.com
from player import AudioPlayer
from player import VideoPlayer
from player import DvdPlayer

if __name__ == "__main__":
    audio_player = AudioPlayer("Spring Day", 329)
    audio_player.play()
    audio_player.set_volume(70)
    audio_player.stop()

    print("---------")

    video_player = VideoPlayer("Титаник", 11640, "1920x1080")
    video_player.play()
    video_player.set_volume(75)
    video_player.stop()

    print("---------")

    dvd_player = DvdPlayer("Операция Ы и другие приключения Шурика")
    dvd_player.play(10)
    dvd_player.set_position(20)
    dvd_player.stop()
