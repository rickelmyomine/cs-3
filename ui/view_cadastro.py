import streamlit as st
import time
from features.equipamento import cadastrar_equipamento

def render_cadastro():
    st.markdown("### Preencha a ficha técnica do ativo")
    
    # Criando o formulário
    with st.form(key="form_cadastro_equipamento"):
        col1, col2 = st.columns(2)
        
        with col1:
            tag = st.text_input("TAG de Identificação*", placeholder="Ex: MOT-002")
            fabricante = st.selectbox("Fabricante", ["WEG", "Siemens", "ABB", "Outro"])
            tensao = st.selectbox("Tensão de Operação", ["220V", "380V", "440V"])
            
        with col2:
            modelo = st.text_input("Modelo*", placeholder="Ex: W22 Premium")
            potencia = st.text_input("Potência*", placeholder="Ex: 15cv ou 11kW")
            
        st.markdown("*Campos obrigatórios")
        
        # Botão de submissão do formulário
        submit_button = st.form_submit_button(label="💾 Salvar Equipamento")
        
    # Lógica de processamento ao clicar no botão
    if submit_button:
        if not tag or not modelo or not potencia:
            st.warning("⚠️ Por favor, preencha todos os campos obrigatórios.")
        else:
            # Simulando latência/processamento (Design para UX)
            with st.spinner("Validando e registrando ativo no sistema..."):
                time.sleep(1) # Simula 1 segundo de carregamento
                sucesso, mensagem = cadastrar_equipamento(tag, modelo, fabricante, potencia, tensao)
                
            if sucesso:
                st.success(f"✅ {mensagem}")
            else:
                st.error(f"❌ {mensagem}")