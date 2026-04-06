# Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

## Nom i cognoms

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Javier Eduardo Basurto Chamorro

## Aviso Importante

> [!Caution]
>
> 
> El objetivo de esta tarea es programar en Python usando el pardigma de la programación
> orientada a objeto. Es el alumno quien debe realizar esta programación. Existen bibliotecas
> que, si lugar a dudas, lo harán mejor que él, pero su uso está prohibido.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Fecha de entrega: 6 de abril a medianoche

## Clase Vector e implementación de la multiplicación de vectores

El fichero `algebra/vectores.py` incluye la definición de la clase `Vector` con los
métodos desarrollados en clase, que incluyen la construcción, representación y
adición de vectores, entre otros.

Añada a este fichero los métodos siguientes, junto con sus correspondientes
tests unitarios.

### Multiplicación de los elementos de dos vectores (Hadamard) o de un vector por un escalar

- Sobrecargue el operador asterisco (`*`, correspondiente a los métodos `__mul__()`,
  `__rmul__()`, etc.) para implementar el producto de Hadamard (vector formado por
  la multiplicación elemento a elemento de dos vectores) o la multiplicación de un
  vector por un escalar.

  - La prueba unitaria consistirá en comprobar que, dados `v1 = Vector([1, 2, 3])` y
    `v2 = Vector([4, 5, 6])`, la multiplicación de `v1` por `2` es `Vector([2, 4, 6])`,
    y el producto de Hadamard de `v1` por `v2` es `Vector([4, 10, 18])`.

- Sobrecargue el operador arroba (`@`, multiplicación matricial, correspondiente a los
  métodos `__matmul__()`, `__rmatmul__()`, etc.) para implementar el producto escalar
  de dos vectores.

  - La prueba unitaria consistirá en comprobar que el producto escalar de los dos
    vectores `v1` y `v2` del apartado anterior es igual a `32`.

### Obtención de las componentes normal y paralela de un vector respecto a otro

Dados dos vectores $v_1$ y $v_2$, es posible descomponer $v_1$ en dos componentes,
$v_1 = v_1^\parallel + v_1^\perp$ tales que $v_1^\parallel$ es tangencial (paralela) a
$v_2$, y $v_1^\perp$ es normal (perpendicular) a $v_2$.

> Se puede demostrar:
>
> - $v_1^\parallel = \frac{v_1\cdot v_2}{\left|v_2\right|^2} v_2$
> - $v_1^\perp = v_1 - v_1^\parallel$

- Sobrecargue el operador doble barra inclinada (`//`, métodos `__floordiv__()`,
  `__rfloordiv__()`, etc.) para que devuelva la componente tangencial $v_1^\parallel$.

- Sobrecargue el operador tanto por ciento (`%`, métodos `__mod__()`, `__rmod__()`, etc.)
  para que devuelva la componente normal $v_1^\perp$.

> Es discutible esta elección de las sobrecargas, dado que extraer la componente
> tangencial no es equivalente a ningún tipo de división. Sin embargo, está
> justificado en el hecho de que su representación matemática es dos barras
> paralelas ($\parallel$), similares a las usadas para la división entera (`//`).
>
> Por otro lado, y de manera *parecida* (aunque no idéntica) al caso de la división
> entera, las dos componentes cumplen: `v1 = v1 // v2 + v1 % v2`, lo cual justifica
> el empleo del tanto por ciento para la componente normal.

- En este caso, las pruebas unitarias consistirán en comprobar que, dados los vectores
  `v1 = Vector([2, 1, 2])` y `v2 = Vector([0.5, 1, 0.5])`, la componente de `v1` paralela
  a `v2` es `Vector([1.0, 2.0, 1.0])`, y la componente perpendicular es `Vector([1.0, -1.0, 1.0])`.

### Entrega

#### Fichero `algebra/vectores.py`

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno
  y los tests unitarios de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido
  de la función, los argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el
  uso de los estándares marcados por PEP-ocho.

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el
fichero `algebra/vectores.py` con la opción *verbosa*, de manera que se muestre el
resultado de la ejecución de los tests unitarios.
![Tests](tests.png)
#### Código desarrollado

Inserte a continuación el código de los métodos desarrollados en esta tarea, usando los
comandos necesarios para que se realice el realce sintáctico en Python del mismo (no
vale insertar una imagen o una captura de pantalla, debe hacerse en formato *markdown*).
```python
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
```
#### Subida del resultado al repositorio GitHub y *pull-request*

La entrega se formalizará mediante *pull request* al repositorio de la tarea.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y
visualizarse correctamente en el repositorio, incluyendo la imagen con la ejecución de
los tests unitarios y el realce sintáctico del código fuente insertado.
