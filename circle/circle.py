from __future__ import annotations

import math


class Circle:
    """

    Represents circle using its radius
    :argument x: x coordinate of the center of the circle
    :argument y: y coordinate of the center of the circle
    :argument radius: Radius of the circle
    :raises: ValueError
    """

    def __init__(self, x: float, y: float, radius: float) -> None:
        if radius <= 0:
            raise ValueError(
                f"Radius must be positive, but value {radius} was provided"
            )

        self._x = x
        self._y = y
        self._radius = radius

    @property
    def radius(self) -> float:
        """

        Returns radius of the circle

        :return: radius of the circle
        """
        return self._radius

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def square(self) -> float:
        """

        Calculates square of the circle

        :return: Radius of the circle
        """
        return (self._radius * math.pi) ** 2

    def point_inside(self, x: int, y: int) -> bool:
        distance = (y - self.y) ** 2 + (x - self.x) ** 2
        return distance <= self.radius ** 2

    def point_on_circle(self, x: int, y: int, places: int = 7) -> bool:
        distance = (y - self.y) ** 2 + (x - self.x) ** 2
        return round(distance, places) == round(self.radius ** 2, places)

    def patch(
            self,
            x: float | None = None,
            y: float | None = None,
            radius: float | None = None,
    ) -> Circle:
        return Circle(x or self.x, y or self.y, radius or self.radius)

    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
