import streamlit as st
import time
import random

from pipelines.ml_pipeline import detectar_anomalia 
from providers.nlp_provider import gerar_resumo_nlp
from ui.components import renderizar_card_alerta 
from providers.db_mock import TelemetriaRepository 

def buscar_novos_alertas(simular_falha):
    equipamentos = st.session_state.get('equipamentos', [])
    
    if not equipamentos:
        st.warning("Nenhum equipamento cadastrado para monitorar.")
        return

    pior_status = "🟢 Saudável"

    for motor in equipamentos:
        tag = motor['TAG']
        
        # Puxa os dados reais da sua telemetria
        dados_inst = TelemetriaRepository.obter_dados_atuais(tag)
        temp_atual = float(dados_inst['Temperatura'])
        vib_atual = float(dados_inst['Vibracao'])
        corr_atual = float(dados_inst['Corrente'])

        # O PULO DO GATO: Injeta um erro falso se o modo de teste estiver ligado!
        if simular_falha:
            temp_atual += random.uniform(45.0, 60.0) # Frita o motor de propósito
            vib_atual += random.uniform(6.0, 9.0)    # Causa uma trepidação severa

        # Inteligência Analítica avalia
        status_ml, diagnostico_ml = detectar_anomalia(temp_atual, vib_atual, corr_atual)

        if status_ml != "🟢 Saudável":
            pior_status = status_ml 
            
            resumo_ia, acao_ia = gerar_resumo_nlp(status_ml, temp_atual, vib_atual, corr_atual)
            
            novo_alerta = {
                "status": f"{status_ml} no Ativo: {tag}", 
                "resumo": f"Análise de IA: {resumo_ia}", 
                "acao": acao_ia 
            }
            # Insere no histórico
            st.session_state['alertas_nlp'].insert(0, novo_alerta)
    
    st.session_state['status_global'] = pior_status

def exibir_painel_alertas():
    if 'alertas_nlp' not in st.session_state:
        st.session_state['alertas_nlp'] = []
        st.session_state['status_global'] = "🟢 Saudável"

    st.title("Painel de Inteligência Operacional e Alertas")
    st.subheader(f"Status Global da Planta: {st.session_state['status_global']}")

    # --- NOVO: Checkbox para forçar erro durante a sua apresentação ---
    st.markdown("---")
    modo_falha = st.checkbox("🚨 Modo Apresentação: Forçar anomalia térmica/vibracional nos sensores")

    if st.button("🔄 Executar Varredura e Atualizar Painel"):
        with st.spinner("Analisando telemetria em tempo real de todos os ativos..."):
            time.sleep(1.5) 
            # Passa a informação do checkbox para a função
            buscar_novos_alertas(simular_falha=modo_falha)
            st.rerun()

    st.markdown("---")

    if not st.session_state['alertas_nlp']:
        st.success("Nenhum desvio analítico detectado. A operação de todos os motores está alinhada à baseline.")
    else:
        st.write("### Histórico de Eventos")
        for alerta in st.session_state['alertas_nlp']:
            renderizar_card_alerta(alerta)