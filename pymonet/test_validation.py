from pymonet.validation import Validation
from pymonet.utils import increase, identity
from pymonet.monad_law_tester import MonadLawTester
from pymonet.transform_monad_tester import TransformMonadTester

from hypothesis import given
from hypothesis.strategies import text

import re


def test_validation_map():
    assert Validation.success(42).map(increase) == Validation.success(43)


def test_validation_bind():
    assert (Validation
            .success(42)
            .bind(lambda value: Validation.success(value + 1))) == Validation.success(43)


def test_validation_is_success():
    assert Validation.success().is_success()


def test_validation_is_fail():
    assert Validation.fail(['fail']).is_fail()


def validate_length(value):
    if len(value) < 5:
        return Validation.fail(['value not long enough'])
    return Validation.success()


def validate_uppercase(value):
    if value[0].upper() != value[0]:
        return Validation.fail(['value not uppercase'])
    return Validation.success()


def validate_contains_special_character(value):
    if re.match(r'^[a-zA-Z0-9_]*$', value):
        return Validation.fail(['value not contains special character'])
    return Validation.success()


def validate(value):
    return (Validation.success(value)
            .ap(validate_length)
            .ap(validate_uppercase)
            .ap(validate_contains_special_character))


def test_validation_applicative():
    assert validate('Success$') == Validation.success('Success$')

    assert validate('Success') == Validation(value='Success', errors=['value not contains special character'])

    assert validate('success$') == Validation(value='success$', errors=['value not uppercase'])
    assert validate('S$') == Validation(value='S$', errors=['value not long enough'])

    assert validate('success') == Validation(value='success', errors=[
        'value not uppercase',
        'value not contains special character'
    ])
    assert validate('s$') == Validation(value='s$', errors=[
        'value not long enough',
        'value not uppercase'
    ])
    assert validate('success') == Validation(value='success', errors=[
        'value not uppercase',
        'value not contains special character'
    ])

    assert validate('s') == Validation(value='s', errors=[
        'value not long enough',
        'value not uppercase',
        'value not contains special character'
    ])


@given(text())
def test_validation_transform(integer):
    TransformMonadTester(monad=Validation.success, value=integer).test()