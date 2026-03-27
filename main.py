import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

st.title("Automação Truck Monitor")

if st.button("Iniciar programa"):
    usuario_input = st.text_input("Digite seu usuário")
    senha_input = st.text_input("Digite sua senha", type="password")

    if st.button("Login"):
        # Configura Chrome headless (sem abrir janela)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        driver.get("http://truckmonitor/")

        # Localiza campos
        usuario = driver.find_element(By.ID, "Login")
        senha = driver.find_element(By.ID, "inputPassword")
        campo_select = driver.find_element(By.ID, "inputPlanta")

        # Seleciona planta
        select = Select(campo_select)
        select.select_by_value("1")

        # Digita usuário e senha
        usuario.send_keys(usuario_input)
        senha.send_keys(senha_input)

        time.sleep(20)

        # Clica no botão de login
        botao_login = driver.find_element(By.XPATH, "//button")
        botao_login.click()

        st.success("Login realizado com sucesso!")

