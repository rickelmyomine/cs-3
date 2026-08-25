import streamlit as st

def init_state():
    # Inicializa um "banco de dados" em memória se não existir
    if 'equipamentos' not in st.session_state:
        st.session_state['equipamentos'] = [
            {"TAG": "MOT-001", "Modelo": "W22", "Fabricante": "WEG", "Potencia": "10cv", "Tensao": "380V"}
        ]
        
    # --- NOVO: Inicializa os estados da Sprint de Visualização ---
    if 'planta_selecionada' not in st.session_state:
        st.session_state['planta_selecionada'] = None
    if 'area_selecionada' not in st.session_state:
        st.session_state['area_selecionada'] = None
