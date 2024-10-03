from __future__ import annotations

from datetime import datetime
from dateutil.relativedelta import relativedelta


class Person:

    def __init__(
            self,
            first_name: str,
            last_name: str,
            birth_date: datetime,
            middle_name: str | None = None,
            death_date: datetime | None = None,
            children: list[Person] | None = None,
    ) -> None:
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.children = children or []

    @property
    def is_alive(self) -> bool:
        return self.death_date is None

    @property
    def age(self) -> int:
        if self.death_date is not None:
            return relativedelta(self.death_date, self.birth_date).years

        return relativedelta(datetime.now(), self.birth_date).years

    @property
    def full_name(self) -> str:
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

        return f"{self.first_name} {self.last_name}"

    @property
    def has_children(self) -> bool:
        return len(self.children) > 0

    def is_parent_of(self, person: Person) -> bool:
        return person in self.children

    def is_child_of(self, person: Person) -> bool:
        q = [person]
        while q:
            relative = q.pop()
            if self is relative:
                return True
            # q.extend(relative.children)
        return False
