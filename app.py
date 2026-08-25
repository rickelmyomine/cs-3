import streamlit as st
from state.state_manager import init_state
from ui.sidebar import render_sidebar
from ui.view_cadastro import render_cadastro
from ui.view_dados import render_dados

# 1️⃣ NOVA IMPORTAÇÃO: Trazendo a tela de alertas que acabamos de criar
from ui.view_alertas import exibir_painel_alertas 

# 1. Configuração da página (UX)
st.set_page_config(
    page_title="Dashboard de Ativos",
    page_icon="🏭",
    layout="wide"
)

# 2. Inicializa o estado (Data)
init_state()

# 3. Renderiza o menu e captura a escolha
menu_selecionado = render_sidebar()

# 4. Roteamento de Telas
# 2️⃣ NOVO BLOCO IF: Página Inicial de Alertas
# Verifique qual é o nome exato que o seu render_sidebar() retorna para a página inicial.
# Coloquei "Painel Inicial" como exemplo. Pode ser que você precise ir no arquivo sidebar.py e adicionar essa opção!
if menu_selecionado == "Painel Inicial" or menu_selecionado is None:
    exibir_painel_alertas()

elif menu_selecionado == "Consulta de Equipamentos":
    st.title(" Consulta de Equipamentos")
    st.dataframe(st.session_state['equipamentos'], use_container_width=True)
    # Aqui depois você pode adicionar lógica para clicar na linha e abrir detalhes
    
elif menu_selecionado == "Cadastro Técnico":
    st.title("➕ Cadastro Técnico de Equipamento")
    render_cadastro() 
    
elif menu_selecionado == "Dados Brutos (Telemetria)":
    # Aqui removemos o st.title de dentro do App.py pois a view_dados já tem o seu
    render_dados()