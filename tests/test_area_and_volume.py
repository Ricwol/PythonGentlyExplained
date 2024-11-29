from exercises.area_and_volume import (
    area,
    perimeter,
    surfaceArea,
    volume
)


def test_area_square():
   assert area(10, 10) == 100


def test_area_line():
    assert area(0, 9999) == 0


def test_area_rectangle():
    assert area(5, 8) == 40


def test_perimeter_square():
    assert perimeter(10, 10) == 40


def test_perimeter_line():
    assert perimeter(0, 9999) == 19998


def test_perimeter_rectangle():
    assert perimeter(5, 8) == 26


def test_volume_cube():
    assert volume(10, 10, 10) == 1000


def test_volume_zero_width_cube():
    assert volume(9999, 0, 9999) == 0


def test_volume_rectangular_prism():
    assert volume(5, 8, 10) == 400


def test_surfaceArea_cube():
    assert surfaceArea(10, 10, 10) == 600


def test_surfaceArea_zero_width_cube():
    assert surfaceArea(9999, 0, 9999) == 199960002


def test_surfaceArea_rectangular_prism():
    assert surfaceArea(5, 8, 10) == 340
