from selenium import webdriver

navegador = webdriver.e()

navegador.get('https://sistema.ssw.inf.br/bin/ssw0194')
navegador.find_element_by_id('lnk_atualizar').click()
