"""
vectores.py

Nombre: Javier Eduardo Basurto Chamorro

Módulo que implementa la clase Vector con operaciones básicas y avanzadas:
- Producto por escalar
- Producto de Hadamard
- Producto escalar
- Descomposición en componentes paralela y perpendicular

Test unitarios:

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])

Producto por escalar:
>>> v1 * 2
Vector([2, 4, 6])

Producto de Hadamard:
>>> v1 * v2
Vector([4, 10, 18])

Producto escalar:
>>> v1 @ v2
32

Componentes paralela y perpendicular:
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])

Comprobación:
>>> v1 == (v1 // v2) + (v1 % v2)
True

"""
class Vector:
    """
    Clase que representa un vector matemático.
    """

    def __init__(self, iterable):
        """
        Constructor del vector.
        """
        self.vector = [valor for valor in iterable]
        return None

    def __repr__(self):
        """
        Representación del vector.
        """
        return f"Vector({self.vector})" 
    
    def __str__(self):
        """
        Representación del vector.
        """
        return str(self.vector)
    
    def __getitem__(self, key):
        """
        Devuelve el elemento key de un tipo compuesto o contenedor
        """
        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Escribe el valor value en la posición key del vector.
        """
        self.vector[key] = value
        
    def __len__(self):
        """
        Devuelve el número de elementos del vector
        """       
        return len(self.vector)
        
    def __iter__(self):
        """
        Permite iterar sobre las componentes del vector.
        """
        return iter(self.vector)
        
    def __eq__(self, other):
        """
        Comprueba igualdad entre vectores.
        """
        return isinstance(other, Vector) and self.vector == other.vector
         
    def __add__(self, other):
        """
        Implementa suma de vectores.
        - Si 'other' es escalar: suma cada componente.
        - Si 'other' es Vector: suma componente a componente.
        """
        if isinstance(other, (int, float, complex)):
            return Vector([x + other for x in self])
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Los vectores deben tener la misma longitud")
            return Vector([x + y for x, y in zip(self, other)])
        return NotImplemented

    __radd__ = __add__  
    
    def __neg__(self):
        """
        Devuelve el vector opuesto (-v).
        """
        return Vector([-1 * item for item in self])
   
    def __sub__(self, other):
        """
        Implementa resta vectorial o resta con escalar.
        """
        if isinstance(other, (int, float, complex, Vector)):
            return self + (-other)
        return NotImplemented
        
    def __rsub__(self, other):
        """
        Resta reversa: other - self.
        """
        return (-self) + other

    def __mul__(self, other):
        """
        Implementa la multiplicación:
        - Vector * escalar
        - Producto de Hadamard (vector * vector)
        """
        if isinstance(other, (int, float)):
            return Vector([x * other for x in self.data])

        if isinstance(other, Vector):
            if len(self.data) != len(other.data):
                raise ValueError("Vectores de distinta dimensión")
            return Vector([a * b for a, b in zip(self.data, other.data)])

        raise NotImplemented("Operación no soportada")

    def __rmul__(self, other):
        """
        Permite escalar * vector
        """
        return self * other

    def __matmul__(self, other):
        """
        Producto escalar (dot product).
        """
        if not isinstance(other, Vector):
            raise TypeError("Producto escalar solo entre vectores")

        if len(self.data) != len(other.data):
            raise ValueError("Vectores de distinta dimensión")

        return sum(a * b for a, b in zip(self.data, other.data))

    def norm_squared(self):
        """
        Norma al cuadrado del vector.
        """
        return sum(x ** 2 for x in self.data)

    def __floordiv__(self, other):
        """
        Componente paralela de self respecto a other.
        """
        if not isinstance(other, Vector):
            raise TypeError("Operación solo entre vectores")

        factor = (self @ other) / other.norm_squared()
        return other * factor

    def __mod__(self, other):
        """
        Componente perpendicular de self respecto a other.
        """
        return self - (self // other)


    def __mul__(self, other):
        """
        Multiplicación por escalar o producto de Hadamard.

        - Si 'other' es escalar: multiplica cada componente.
        - Si 'other' es Vector: multiplica componente a componente.
        """
        if isinstance(other, (int, float, complex)):
            return Vector([x * other for x in self])
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Los vectores deben tener la misma longitud")
            return Vector([x * y for x, y in zip(self, other)])
        return NotImplemented

    __rmul__ = __mul__


    def __matmul__(self, other):
        """
        Producto escalar entre dos vectores.
        """
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Los vectores deben tener la misma longitud")
            return sum(x * y for x, y in zip(self, other))
        return NotImplemented

    __rmatmul__ = __matmul__


    def __floordiv__(self, other):
        """
        Devuelve la componente paralela de self respecto a other.

        Fórmula:
        v_parallel = ((v1 @ v2) / |v2|^2) * v2
        """
        if not isinstance(other, Vector):
            return NotImplemented

        denom = other @ other
        if denom == 0:
            raise ZeroDivisionError("No se puede proyectar sobre un vector nulo")

        coef = (self @ other) / denom
        return other * coef

    __rfloordiv__ = __floordiv__


    def __mod__(self, other):
        """
        Devuelve la componente perpendicular de self respecto a other.

        Fórmula:
        v_perp = v1 - v1_parallel
        """
        if not isinstance(other, Vector):
            return NotImplemented
        return self - (self // other)

    __rmod__ = __mod__