import pytest
import productos
import os
from datetime import datetime
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



@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):

    carpeta_reportes = "reports"
    
    if not os.path.exists(carpeta_reportes):
        os.makedirs(carpeta_reportes)
        
    fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    config.option.htmlpath = os.path.join(carpeta_reportes, f"reporte_{fecha_hora}.html")
    config.option.self_contained_html = True

