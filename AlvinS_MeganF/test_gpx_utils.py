import gpx_utils as gu

def test_get_coords_from_gpx():
    expected = (-75.742631,45.3888995)
    actual = gu.get_coords_from_gpx(gpx)
    assert expected == actual