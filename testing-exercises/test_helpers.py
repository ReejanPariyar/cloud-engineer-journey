from helpers import bytes_to_mb

def test_bytes_to_mb():
    assert bytes_to_mb(1048576) == 1.0
    assert bytes_to_mb(0) == 0.0

