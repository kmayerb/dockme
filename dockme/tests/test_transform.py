import pytest
from dockme import transform

test_data = [
(1.0, 0.0, None),
(10.0, 1.0, None),
(100.0, 2.0, None),
(None, None, TypeError),
(-1.0, 0.0, None),
("A", None, TypeError)]

@pytest.mark.parametrize("x, expect, expected_error", test_data)
def test__log10_transform(x, expect, expected_error):
	try:
		assert transform._log10_transform(x) == expect
	except:
		with pytest.raises(expected_error):
			transform._log10_transform(x) == expect
