import gpx_utils as gu

def test_get_coords_from_gpx():
    expected = ('45.3888995','-75.7472631')
    actual = gu.get_coords_from_gpx('trkpt lat="45.3888995" lon="-75.7472631"')
    assert expected == actual