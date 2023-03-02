import pytest
from project import bufculator
from project import distortion
from project import delay1


def test_bufculator():
    assert bufculator(256, 44100)  == 0.005804988662131519


def test_distortion():
    with pytest.raises(TypeError):
        distortion()


def test_delay1():
    with pytest.raises(TypeError):
        delay1()
