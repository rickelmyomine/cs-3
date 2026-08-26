import streamlit as st

def render_sidebar():
    # Título da barra lateral
    st.sidebar.title("Gestão de Ativos")
    
    # 1. Menu Principal
    menu_selecionado = st.sidebar.radio(
        "Selecione a visão desejada:",
        [
            "Painel Inicial", 
            "Consulta de Equipamentos",
            "Cadastro Técnico",
            "Dados Brutos (Telemetria)"
        ]
    )
    
    st.sidebar.markdown("---")
    
    # 2. Filtros Hierárquicos (Atualização em tempo real das áreas[cite: 1])
    st.sidebar.subheader("📍 Filtros de Localização")
    
    planta = st.sidebar.selectbox("Selecione a Planta:", ["Matriz SP", "Filial MG"])
    
    # Devolvendo as áreas! Se quiser adicionar mais, é só colocar entre aspas na lista abaixo:
    if planta == "Matriz SP":
        area = st.sidebar.selectbox("Selecione a Área:", [
            "Linha de Produção A", 
            "Linha de Produção B",
            "Montagem",
            "Expedição"
        ])
    else: # Filial MG
        area = st.sidebar.selectbox("Selecione a Área:", [
            "Linha de Montagem A", # <-- De volta ao seu devido lugar!
            "Usinagem", 
            "Embalagem",
            "Controle de Qualidade"
        ])
        
    # CORREÇÃO CHAVE: Usando exatamente as chaves que a view_dados.py está procurando
    st.session_state['planta_selecionada'] = planta
    st.session_state['area_selecionada'] = area
    
    return menu_selecionado