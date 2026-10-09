import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_01_login(driver):
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)
        user_input = wait.until(EC.visibility_of_element_by_id if hasattr(EC, 'visibility_of_element_by_id') else EC.visibility_of_element_located((By.ID, "user-name")))

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "/inventory.html" in driver.current_url , "ERROR: No se redirige a /inventory.html"

def test_02_verificar_inventario(driver):   
        wait = WebDriverWait(driver, 10)
        section_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))) 
       # driver.get("https://www.saucedemo.com/")
        
        #driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #driver.find_element(By.ID, "login-button").click()

        page_title = driver.title
        section_title = driver.find_element(By.CLASS_NAME, "title").text    

        assert page_title  == "Swag Labs", f"ERROR: Titulo de ventana esperado 'swag labs', Obtenido {page_title}"



        assert section_title == "Products" , f"ERROR: Titulo de seccion esperado 'products', Obtenido {section_title}"

def test_03_productos_visibles(driver):
       wait = WebDriverWait(driver, 10)
       wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
       inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')  
       #[] len() ver el largo de una lista
       assert len(inventory_item) > 0 , f"ERROR: No se encontraron productos visibles"   

def test_04_validar_interfaz(driver):
       menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')  
       filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')  

       assert menu_button.is_displayed(), f"ERROR: El menu no esta visible"
       assert filtro.is_displayed(), f"ERROR: El filtro no esta visible"    

def test_05_añadir_producto_al_carrito(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))
    
    boton_agregar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_inventory')))
    boton_agregar.click()
    boton_actualizado = driver.find_element(By.CLASS_NAME, 'btn_inventory')
    
    assert boton_actualizado.text.capitalize() == 'Remove', "ERROR: El boton no cambio a Remove"


def test_06_verificar_contador_carrito(driver):
     contador_carrito = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
     contador_carrito == "1" , f"ERROR: Se esperaba 1, se obtuvo {contador_carrito}"   



def test_07_navegar_carrito(driver):
      driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
      assert "/cart.html" in driver.current_url , "ERROR: No se redirige a /cart.html" 


def test_08_comprobar_producto_en_el_carrito(driver):
    producto_nombre_en_carrito = driver.find_element(By.CLASS_NAME,'inventory_item_name').text
    assert producto_nombre_en_carrito == 'Sauce Labs Backpack' , f'ERROR: No es el mismo nombre'