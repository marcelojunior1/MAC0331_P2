from . import brute_force
from . import projeto2


children = [('brute_force', 'Brute_force', 'Forca\nBruta'), 
			('projeto2', 'Projeto2', 'Interseção-SH-P2')]

__all__ = [a[0] for a in children]
