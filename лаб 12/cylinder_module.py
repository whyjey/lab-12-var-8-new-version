import math
from turtle import right

def total_surface_area(radius, height):
    """Обчислює повну площу поверхні прямого циліндра"""
    return 2 * math.pi * radius * (radius + height)

def lateral_surface_area(radius, height):
    """Обчислює площу бічної поверхні прямого циліндра"""
    return 2 * math.pi * radius * height

def cylinder_volume(radius, height):
    """Обчислює об'єм прямого циліндра"""
    return math.pi * radius ** 2 * height
if __name__ == "__main__":
    # Запитуємо радіус і висоту циліндра
    radius = float(input("Введіть радіус циліндра: "))
    height = float(input("Введіть висоту циліндра: "))

    # Використання функцій модуля
    total_area = cylinder_module.total_surface_area(radius, height)
    lateral_area = cylinder_module.lateral_surface_area(radius, height)
    volume = cylinder_module.cylinder_volume(radius, height)

    # Виведення результатів
    print(f"Повна площа поверхні циліндра: {total_area:.2f}")
    print(f"Площа бічної поверхні циліндра: {lateral_area:.2f}")
    print(f"Об'єм циліндра: {volume:.2f}")
10
