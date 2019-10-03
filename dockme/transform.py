import numpy as np

def _log10_transform(x):
	
	if not isinstance(x, float):
		raise TypeError

	if x > 0.0:
		return np.log10(x)
	else:
		return 0.0



