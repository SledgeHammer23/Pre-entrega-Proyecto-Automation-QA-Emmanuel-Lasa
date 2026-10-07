import pytest
import productos


# decoradores
@pytest.fixture(autouse=True)
def limpiar_productos():
    productos.productos.clear()
    yield # => se ejecuta los test de prueba
    productos.productos.clear()

@pytest.fixture
def datos_base():
    productos.productos.extend([
        {"nombre":"Mouse","precio":1000,"cantidad":3},
        {"nombre":"Teclado","precio":5000,"cantidad":2},
        {"nombre":"Parlante","precio":3000,"cantidad":5}
    ])

    return productos.productos