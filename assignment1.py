import doctest
PI = 3.14

def print_guy():
    """prints the picture of a guy
  """
    print("   ____")
    print("  |    |")
    print("'_|><><|_'")
    print("|________|")
    print("  /    \\")
    print(" |\"0 0\"|")
    print("  \ \/ /")
    
    
def print_bear():
    """prints the picture of a bear
    """
    print('   {}__{}')
    print('  {"0  0"}')
    print('    {^}')
    print('{0}/~~~\{0}')
    print('  /~~~~~\\')
    print('{0}     {0}')


def print_logo():
    """prints two copies of the above figures in alternating orders with a
    spacer line at the front, between figures, and at the end.
    """
    spacer_line = '/~~~~~~~~\\'
    print(spacer_line)
    print_guy()
    print(spacer_line)    
    print_bear()
    print(spacer_line)
    print_guy()
    print(spacer_line)    
    print_bear()
    print(spacer_line)    
    
    

def calculate_surface_area(height: float, diameter: float):
    """takes given measurement of a cylinder's height and diameter and
    calculates and prints the surface area of the cylinder.
    >>> calculate_surface_area(1.2, 3.5)
    cylinder area: 32.4
    >>> calculate_surface_area(0, 0)
    cylinder area: 0.0
    """
    cylinder_cir = 2 * PI * (diameter/2)
    top_area = (PI * (diameter/2)**2)
    wall_area = (cylinder_cir * height)
    total_area = (2*top_area) + wall_area
    print(f'cylinder area: {total_area:.1f}')