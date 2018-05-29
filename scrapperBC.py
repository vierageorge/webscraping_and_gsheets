from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time, datetime

wait_time = 1
path_chromeDriver = "D:\chromedriver.exe"
link = "https://www.grupobancolombia.com/wps/portal/personas/productos-servicios/inversiones/fondos-inversion-colectiva/aplicacion-fondos"

today = datetime.date.today()
today_str = today.strftime('%Y/%m/%d')

driver = webdriver.Chrome(path_chromeDriver)
driver.get(link)

select = Select(driver.find_element_by_name('nmSelectFondo'))
options = select.options
for option in options:
    option.click()
    time.sleep(wait_time)
    nombre_fondo = option.text
    rows = driver.find_elements(By.XPATH, "//div[@id='resultados']/table/tbody/tr/td")
    if len(rows)>=30:
        dias_7 = rows[15].text
        dias_30 = rows[16].text
        dias_180 = rows[17].text
        anos_corrido = rows[23].text
        anos_ultimo = rows[24].text
        anos_ultimos2 = rows[25].text
        anos_ultimos3 = rows[26].text
        valor_unidad = rows[7].text
        valor_pesos = rows[9].text
        fecha_cierre = rows[29].text
        print("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(today_str, nombre_fondo, dias_7, dias_30, dias_180, anos_corrido, anos_ultimo, anos_ultimos2, anos_ultimos3, valor_unidad, valor_pesos, fecha_cierre))
    else:
        print("{} -> No tiene todos los td: Rows: {}".format(nombre_fondo, len(rows)))
driver.quit()
