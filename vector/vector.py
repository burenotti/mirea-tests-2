from __future__ import annotations

from typing import Iterator, Callable


class Vector3D:

    def __init__(self, x: float | int, y: float | int, z: float | int) -> None:
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __iter__(self) -> Iterator[float]:
        return iter((self.x, self.y, self.z))

    def apply(self, func: Callable[[float], float]) -> Vector3D:
        return Vector3D(func(self.x), func(self.y), func(self.z))

    def __eq__(self, right: Vector3D) -> bool:
        return self.x == right.x and self.y == right.y and self.z == right.z

    def __add__(self, right: Vector3D | int | float) -> Vector3D:
        if isinstance(right, Vector3D):
            return Vector3D(self.x + right.x, self.y + right.y, self.z + right.z)
        elif isinstance(right, (int, float)):
            return self.apply(lambda coord: coord + right)

        raise NotImplemented

    def __radd__(self, left: Vector3D | int | float) -> Vector3D:
        return self.__add__(left)

    def __neg__(self) -> Vector3D:
        return Vector3D(-self.x, -self.y, -self.z)

    def __sub__(self, right: Vector3D | int | float) -> Vector3D:
        if isinstance(right, Vector3D):
            return self + (-right)
        elif isinstance(right, float):
            return self.apply(lambda coord: coord - right)
        else:
            return NotImplemented

    def __rsub__(self, left: Vector3D) -> Vector3D:
        return Vector3D(left.x - self.x, left.y - self.y, left.z - self.z)

    def __mul__(self, right: Vector3D | int | float) -> Vector3D:
        if isinstance(right, Vector3D):
            return Vector3D(self.x * right.x, self.y * right.y, self.z * right.z)
        elif isinstance(right, (int, float)):
            return self.apply(lambda coord: coord * right)
        else:
            return NotImplemented

    def __rmul__(self, left: Vector3D | int | float) -> Vector3D:
        return self.__mul__(left)

    def __truediv__(self, right: Vector3D | int | float) -> Vector3D:
        if isinstance(right, Vector3D):
            return Vector3D(self.x / right.x, self.y / right.y, self.z / right.z)
        elif isinstance(right, (int, float)):
            return self.apply(lambda coord: coord / right)
        else:
            return NotImplemented

    def __rtruediv__(self, left: Vector3D) -> Vector3D:
        return Vector3D(left.x / self.x, left.y / self.y, left.z / self.z)

    def __repr__(self) -> str:
        return f"Vector3D(x={self.x}, y={self.y}, z={self.z})"


# Функции для тестирования: +, -, *, /, apply. Проверить, что можно распаковать вектор в переменные как x, y, z = vec
# Ошибка: Падает при вычитании из вектора целого числа.
# Решение: Поправить в __sub__ isinstance(right, float) на isinstance(right, (int, float)).
print(Vector3D(2, 3, 4) + Vector3D(1, 2, 3))
print(Vector3D(2, 3, 4) + 11.0)
print(Vector3D(2, 3, 4) + 11)
print(1 + Vector3D(2, 3, 4))
print(2 * Vector3D(2, 3, 4))
print(Vector3D(2, 3, 4) / Vector3D(2, 3, 4))
