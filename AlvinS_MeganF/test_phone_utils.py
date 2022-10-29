import phone_utils as pu

def test_is_valid_phone_number():
    expected = True
    actual = pu.is_valid_phone_number(600-600-6000)
    assert expected == actual

def test_is_valid_phone_number():
    expected = False
    actual = pu.is_valid_phone_number(1234-567-6000)
    assert expected == actual

def test_is_valid_phone_number():
    expected = False
    actual = pu.is_valid_phone_number(AS1-222-2222)
    assert expected == actual
    