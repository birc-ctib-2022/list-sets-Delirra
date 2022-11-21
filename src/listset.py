"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        self.data = list(init)
        for element in init:
            self.add(element)


    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        for element in self.data:
            if element == x:
                return True
        return False

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        if self.data:
            return True
        return False

    def add(self, x: T) -> None:
        """Add x to the set."""
        if x not in self:
            self.data.append(x)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        if x in self:
            self.data.remove(x)


x = ListSet([1,2,3,4])
print(x.data)
x.add(5)
x.remove(2)
print(x.data)
print(bool(x))
x = ListSet([])
print(x.data)
print(bool(x))