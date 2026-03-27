import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Automação Truck Monitor (via requests)")

if st.button("Iniciar programa"):
    usuario_input = st.text_input("Digite seu usuário")
    senha_input = st.text_input("Digite sua senha", type="password")

    if st.button("Login"):
        # URL base
        url_login = "http://truckmonitor/login"   # ajuste conforme o endpoint real
        url_monitor = "http://truckmonitor/MonitoracaoGC/Index?planta=SP&GC_TW=GC&tipoPesquisa=PL"

        # Cria sessão para manter cookies
        session = requests.Session()

        # Payload de login (ajuste os nomes dos campos conforme o form HTML)
        payload = {
            "Login": usuario_input,
            "Password": senha_input,
            "Planta": "1"   # equivalente ao select
        }

        # Faz POST para logar
        resp = session.post(url_login, data=payload)

        if resp.status_code == 200:
            # Agora acessa a página de monitoramento
            resp_monitor = session.get(url_monitor)
            if resp_monitor.status_code == 200:
                soup = BeautifulSoup(resp_monitor.text, "html.parser")

                # Exemplo: pegar título da página
                titulo = soup.title.string if soup.title else "Sem título"
                st.success(f"Login realizado! Página acessada: {titulo}")
            else:
                st.error("Não consegui acessar a página de monitoramento.")
        else:
            st.error("Falha no login. Verifique usuário/senha.")
