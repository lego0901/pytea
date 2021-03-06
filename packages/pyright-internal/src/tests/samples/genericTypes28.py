# This sample tests that Optional types can be matched
# to Type[T] expressions.

from typing import Generic, Literal, Optional, Type, TypeVar

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2", bound=None)


def foo1(a: Type[_T1]) -> _T1:
    return a()


a = foo1(Optional[int])


def foo2(a: Type[_T2]) -> _T2:
    return a()


b = foo2(type(None))

# This should generate an error because None is
# not a type; it's an instance of the NoneType class.
c = foo2(None)


class Foo(Generic[_T1]):
    def __init__(self, value: _T1) -> None:
        ...


def bar(value: _T1) -> Type[Foo[_T1]]:
    baz = Foo(value)
    qux = type(baz)
    t1: Literal["Type[Foo[_T1]]"] = reveal_type(qux)
    return qux
