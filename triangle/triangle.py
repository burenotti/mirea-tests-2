import math


class Triangle:
    """

    Represents a triangle using its sides

    :param a: First side of the triangle
    :param b: Second side of the triangle
    :param c: Third side of the triangle
    :raises InvalidArgumentsError: if triangle with given sides does not exist
    :returns: Square of triangle with given sides
    """

    def __init__(self, a: float, b: float, c: float) -> None:
        self.__check_constraints(a, b, c)
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)

    @property
    def a(self) -> float:
        return self._a

    @property
    def b(self) -> float:
        return self._b

    @property
    def c(self) -> float:
        return self._c

    def with_sides(
            self,
            a: float | None = None,
            b: float | None = None,
            c: float | None = None,
    ) -> "Triangle":
        """

        Returns new triangles with updated sides

        :param a: New first side of the triangle
        :param b: New second side of the triangle
        :param c: New third side of the triangle
        :raises InvalidArgumentsError: if triangle with given sides does not exist
        :return: triangle with updated sides
        """
        return Triangle(a or self.a, b or self.b, c or self.c)

    def is_right(self, places: int = 7) -> bool:
        """

        Check if triangle is right by checking the Pythagorean theorem.

        :param places: Precision of checking. 7 by default.
        :returns: true if triangle is right
        """

        # Check if Pythagorean theorem is satisfied
        c = max(self.a, self.b, self.c)
        if c == self.a:
            a, b = self.b, self.c
        elif c == self.b:
            a, b = self.a, self.c
        else:
            a, b = self.a, self.b

        return a * a + b * b == c * c
        # return round(a * a + b * b, places) == round(c * c, places)

    def square(self) -> float:
        """

        Calculates square of the triangle

        :return: square of the triangle
        """
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

    @staticmethod
    def __check_constraints(a: float, b: float, c: float) -> None:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError(
                f"All sides must be positive, but ({a}, {b}, {c}) were given"
            )

        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError(
                f"Triangle with sides ({a}, {b}, {c}) does not exists"
            )
