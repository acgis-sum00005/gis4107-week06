import code_parser as cp

def test_code_parser():
    expected = ('BO-642')
    actual = cp.building_code('20-WBO-109642-809')
    assert expected == actual
