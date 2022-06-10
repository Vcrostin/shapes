import pytest
import shapes
import math

rectangle = shapes.rectangle(16, 18)
square = shapes.square(2)
circle = shapes.circle(7)
tangle = shapes.triangle(A=2, B=3, C=3)
cylinder = shapes.cylinder(3, 10)


def test_rectrangle_perimeter():
    assert rectangle.perimeter == 68.0, "test failed"
    assert type(rectangle.perimeter) == float, "datatype error"

def test_rectangle_area():
    assert rectangle.area == 288.0, "test failed"
    assert type(rectangle.area) == float, "datatype error"

def test_square_area():
    assert square.area == 4.0, "test failed"
    assert type(square.area) == float, "datatype error"

def test_square_perimeter():
    assert square.perimeter == 8.0, "test failed"
    assert type(square.perimeter) == float, "datatype error"

def test_circle_perimeter():
    assert circle.perimeter == 43.982297150257104, "test failed"
    assert type(circle.perimeter) == float, "datatype error"

def test_circle_area():
    assert circle.area == 153.93804002589985, "test failed"
    assert type(circle.area) == float, "datatype error"

def test_triangle_area():
    assert tangle.perimeter == 8.0, "test failed"
    assert type(tangle.perimeter) == float, "datatype error"

def test_cube_volume_null():
    cube = shapes.cube(0, 0, 0)
    assert cube.volume == 0, "test failed"
    assert type(cube.volume) == float, "datatype error"
    cube2 = shapes.cube(0, 1, 0)
    cube3 = shapes.cube(1, 0, 1)
    assert cube.volume == cube2.volume and cube.volume == cube3.volume, "test failed"

def test_cube_volume_full():
    cube = shapes.cube(1, 1, 1)
    assert cube.volume == 1, "test failed"
    assert type(cube.volume) == float, "datatype error"
    cube2 = shapes.cube(10, 10, 10)
    assert cube2.volume == 1000, "test failed"
    assert type(cube2.volume) == float, "datatype error"

def test_cube_surface_area_null():
    cube = shapes.cube(0, 0, 0)
    assert cube.surface_area == 0, "test failed"
    assert type(cube.surface_area) == float, "datatype error"

def test_cube_surface_area_full():
    cube = shapes.cube(1, 1, 1)
    assert cube.surface_area == 6, "test failed"
    assert type(cube.surface_area) == float, "datatype error"
    cube2 = shapes.cube(10, 10, 10)
    assert cube2.surface_area == 600, "test failed"
    assert type(cube2.surface_area) == float, "datatype error"
    cube3 = shapes.cube(10, 5, 1)
    assert cube3.surface_area == 130, "test failed"
    assert type(cube3.surface_area) == float, "datatype error"
    cube4 = shapes.cube(10, 5, 0)
    assert cube4.surface_area == 120, "test failed"
    assert type(cube4.surface_area) == float, "datatype error"

def test_cylinder_volume():
    assert cylinder.volume == math.pi * 90, "test failed"
    assert type(cylinder.volume) == float, "datatype error"

def test_cylinder_total_surf_area():
    assert cylinder.totalSurfaceArea == math.pi * 78, "test failed"
    assert type(cylinder.totalSurfaceArea) == float, "datatype error"

def test_cylinder_lateral_surf_area():
    assert cylinder.lateralSurfaceArea == math.pi * 60, "test failed"
    assert type(cylinder.totalSurfaceArea) == float, "datatype error"
