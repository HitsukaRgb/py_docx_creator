from pathlib import Path
from tempfile import TemporaryDirectory


def temp_dir(func):
    """
    Декоратор прокидывающий первым позиционным аргументом (после self)
    путь до локальной директории типа Path
    """

    def wrapper(self, *args, **kwargs):
        with TemporaryDirectory() as directory:
            dir_path = Path(directory)
            return func(self, dir_path, *args, **kwargs)

    return wrapper
