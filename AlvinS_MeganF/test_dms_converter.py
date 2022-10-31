import dms_converter as dc

def test_dms2dd():
    expected = (-75.75083333333333, 45.38472222222222)
    actual = dc.dms2dd('075 45 03 W 45 23 05 N\n')
    assert expected == actual

def test_dms2dd():
    expected = (74.75083333333333, 45.38472222222222)
    actual = dc.dms2dd('074 45 03 E 45 23 05 N\n')
    assert expected == actual

def test_dms2dd():
    expected = (None, None)
    actual = dc.dms2dd('189 45 03 E 45 23 05 S\n')
    assert expected == actual

def test_dms2dd():
    expected = (None, None)
    actual = dc.dms2dd('075 45 03 W 95 23 05 s\n')
    assert expected == actual