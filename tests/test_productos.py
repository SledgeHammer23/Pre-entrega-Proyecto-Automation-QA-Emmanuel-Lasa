import pytest
import productos


@pytest.mark.busqueda
@pytest.mark.parametrize("datos_entradas,resultado_esperado",[
    (["Mouse","1500","3"] ,
     {"nombre":"Mouse","precio":1500.0,"cantidad":3}
     ),
    (
        ["Teclado","5000","3"] ,
        {"nombre":"Teclado","precio":5000.0,"cantidad":3}),
    (
        ["Parlante","3000","3"] ,
        {"nombre":"Parlante","precio":3000.0,"cantidad":3})
    ]
)
def test_agregar_producto_exito( monkeypatch, datos_entradas , resultado_esperado ):

    entrada = iter(datos_entradas) # usuario, tester

    monkeypatch.setattr("builtins.input",lambda _: next(entrada))

    productos.agregar_producto()

    assert len(productos.productos) == 1
    assert productos.productos[0] == resultado_esperado


# CASO DE VALIDACIONES 
@pytest.mark.parametrize("entradas_ivalidas",[
    ["","3000","3"] , #nombre vacío
    ["Parlante","-3000","3"] , #precio negativo
    ["Parlante","3000","-3"] , #cantidad negativa
])
def test_agregar_producto_errores(monkeypatch, entradas_ivalidas):
    entrada = iter(entradas_ivalidas) # usuario, tester
    monkeypatch.setattr("builtins.input",lambda _: next(entrada))

    productos.agregar_producto()
    assert len(productos.productos) == 0


def test_agregar_producto_exitos( monkeypatch ):

    entrada = iter(["Mouse","1500","3"]) # usuario, tester

    monkeypatch.setattr("builtins.input",lambda _: next(entrada))

    productos.agregar_producto()

    assert len(productos.productos) > 0

@pytest.mark.eliminar_producto
def test_buscar_productos_existentes( datos_base ):

    resultado = productos.buscar_por_precio( datos_base, precio_maximo=4000)

    assert len(resultado) == 2

def test_agregar_producto_precio_negativo( monkeypatch):
    entrada = iter(["Mouse","-1500","3"])
    monkeypatch.setattr("builtins.input",lambda _: next(entrada))

    productos.agregar_producto()

    assert len(productos.productos) == 0

@pytest.mark.eliminar_producto
def test_eliminar_producto( monkeypatch, datos_base ):

    monkeypatch.setattr("builtins.input",lambda _: "Mouse")

    productos.eliminar_producto()

    
    assert len(productos.productos) == 2
    assert productos.productos[0]["nombre"] == "Teclado"


