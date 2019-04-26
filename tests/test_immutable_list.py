from pymonet.immutable_list import ImmutableList


def test():
    assert ImmutableList(1).length == 1
    assert ImmutableList(1).unshift(0).length == 2


def test_to_list():
    assert ImmutableList(1).unshift(0).to_list() == [0, 1]


def test_of():
    assert ImmutableList.of(1, 2, 3, 4).to_list() == [1, 2, 3, 4]


def test_map():
    assert ImmutableList.of(1, 2, 3, 4).map(lambda item: item + 1) == ImmutableList.of(2, 3, 4, 5)


def test_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda item: item % 2 == 0) == ImmutableList.of(2, 4)


def test_empty_filter():
    assert ImmutableList.of(1, 2, 3, 4).filter(lambda item: False) == ImmutableList.empty()


def test_plus_operator():
    assert ImmutableList.of(1, 2) + ImmutableList.of(3, 4) == ImmutableList.of(1, 2, 3, 4)


def test_find_positive():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda item: item % 2 == 0) == 2


def test_find_negative():
    assert ImmutableList.of(1, 2, 3, 4).find(lambda item: item < 0) == None


def test_unshift():
    assert ImmutableList.of(1, 2).unshift(0) == ImmutableList.of(0, 1, 2)
