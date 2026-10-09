
# 🧪 Pre-entrega-Proyecto-Automation-QA-Emmanuel-Lasa

Este proyecto contiene una suite de pruebas automatizadas utilizando **Python**, **Selenium WebDriver** y **Pytest** para la plataforma de práctica [SauceDemo](https://saucedemo.com). El objetivo es validar los flujos principales de la interfaz de usuario, incluyendo el inicio de sesión, la verificación del inventario y la interacción con el carrito de compras.

---

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.14.7
*   **Framework de Testing:** Pytest
*   **Herramienta de Automatización:** Selenium WebDriver
*   **Administrador de Drivers:** WebDriver Manager (Chrome)
*   **Patrón de Diseño:** Estructura modular basada en Fixtures de Pytest

---

## 📋 Pruebas Automatizadas Incluidas

El archivo `test_saucedemo.py` incluye los siguientes escenarios de prueba encadenados mediante una sesión de navegador compartida (`scope="module"`):

1.  **`test_01_login`**: Valida que un usuario con credenciales pueda iniciar sesión de manera exitosa y sea redirigido a la página de inventario.
2.  **`test_02_verificar_inventario`**: Comprueba que el título de la pestaña del navegador sea correcto y que la sección principal muestre el encabezado `"Products"`.
3.  **`test_03_productos_visibles`**: Asegura que la lista de productos se cargue correctamente en el DOM y contenga elementos visibles.
4.  **`test_04_validar_interfaz`**: Verifica la presencia y visibilidad de componentes clave de la UI, como el menú lateral (*burger menu*) y el filtro de ordenamiento de productos.
5.  **`test_añadir_producto_al_carrito`**: Simula la adición del primer producto al carrito de compras y valida dinámicamente que el texto del botón cambie a `"Remove"`.

---

## 🕒 Timer Aplicado

*   **Esperas Explícitas (`WebDriverWait`):** Se implementaron sincronizaciones dinámicas basadas en condiciones esperadas (`expected_conditions`) para mitigar la latencia de red y evitar la fragilidad en los tests (*flaky tests*).
*   **Manejo del Ciclo de Vida del Driver:** Uso de `@pytest.fixture` con `yield` para garantizar la correcta apertura y el cierre seguro del navegador (`driver.quit()`), evitando dejar procesos colgados en segundo plano.
*   **Estrategia Antifallos (Stale Elements):** Resolución de excepciones de tipo `StaleElementReferenceException` mediante la re-captura de elementos modificados dinámicamente por JavaScript en el DOM.

---

## 🔧 Instalación y Configuración

### 1. Requisitos Previos
Asegurarse de tener instalado Python y el navegador Google Chrome.

### 2. Instalar Dependencias
Instalar las librerías necesarias ejecutando el siguiente comando en tu terminal:
```bash
pip install pytest selenium webdriver-manager
```

---

## 🏃 Ejecución de las Pruebas

Para correr las pruebas de forma correcta, abrir la terminal posicionándote en la **carpeta raíz del proyecto** y ejecuta:

```bash
python -m pytest tests/test_saucedemo.py
```

Para ver un resumen detallado de la ejecución en la consola, se debe agregar el parámetro `-v`:
```bash
python -m pytest tests/test_saucedemo.py -v
```