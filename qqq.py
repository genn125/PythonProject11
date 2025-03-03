from pathlib import Path

# Задаём корневой путь проекта.
root_path = Path(__file__).resolve().parent.parent

print(root_path)