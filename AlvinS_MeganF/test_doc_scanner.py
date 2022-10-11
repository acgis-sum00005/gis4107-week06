import doc_scanner as ds

def test_has_x_code_True():
    expected = True
    actual = ds.has_x_code('Top secret message Tx6op3')
    assert expected == actual

def test_has_x_code_False():
    expected = False
    actual = ds.has_x_code('Top secret message')
    assert expected == actual

def test_get_x_code_position_not_found():
    expected = -1
    actual = ds.get_x_code_position('Hello my old friend')
    assert expected == actual

