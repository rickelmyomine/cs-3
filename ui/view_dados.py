import streamlit as st
import time # NOVO: Necessário para a pausa do spinner
from pipelines.conversor_sinais import obter_dados_telemetria
from providers.db_mock import TelemetriaRepository
import plotly.express as px

def render_dados():
    st.markdown("### 📊 Monitoramento de Sensores e Telemetria")
    
    # --- Exibir a localização selecionada na barra lateral ---
    planta = st.session_state.get('planta_selecionada', 'Não definida')
    area = st.session_state.get('area_selecionada', 'Não definida')
    st.caption(f"📍 Localização Atual: **{planta}** > **{area}**")
    st.markdown("---")

    # Verifica se existe algum equipamento cadastrado
    if not st.session_state.get('equipamentos'):
        st.info("Nenhum equipamento cadastrado. Vá até 'Cadastro Técnico' para adicionar um ativo primeiro.")
        return

    # Extrai as TAGs dos equipamentos para o selectbox
    tags_disponiveis = [eq['TAG'] for eq in st.session_state['equipamentos']]

    col_header1, col_header2 = st.columns([2, 1])
    with col_header1:
        ativo_selecionado = st.selectbox("Selecione o Ativo para Monitoramento", tags_disponiveis)
    with col_header2:
        st.markdown("<br>", unsafe_allow_html=True) # Espaçamento
        st.status("Conexão com Sensor: OK", state="complete")
        
    st.markdown("---")

    # --- Indicadores de Alerta e Status ---
    # Puxa os dados instantâneos para o ativo selecionado
    dados_inst = TelemetriaRepository.obter_dados_atuais(ativo_selecionado)
    
    st.markdown(f"#### Estado de Saúde do Ativo: {dados_inst['Indicador']} {dados_inst['Status']}")
    
    metrica1, metrica2, metrica3 = st.columns(3)
    with metrica1:
        st.metric(label="Temperatura (Atual)", value=f"{dados_inst['Temperatura']} °C")
    with metrica2:
        st.metric(label="Vibração (Atual)", value=f"{dados_inst['Vibracao']} mm/s")
    with metrica3:
        st.metric(label="Corrente (Atual)", value=f"{dados_inst['Corrente']} A")

    # --- Integração de Cadastro Visual ---
    with st.expander("📷 Visualizar Placa do Ativo (Extração via Visão Computacional)"):
        col_img, col_info = st.columns([1, 1])
        
        with col_img:
            # Usando uma imagem simulada da internet (placeholder). 
            url_placa_mock = "https://dummyimage.com/600x300/2c3e50/ecf0f1&text=PLACA+MOTOR+-+WEG+W22"
            st.image(url_placa_mock, caption=f"Imagem de Referência: {ativo_selecionado}", use_container_width=True)
            st.info("Imagem real ainda vai ser disponibilizada...")
            
        with col_info:
            st.markdown("##### Dados Extraídos (OCR/Visão Computacional)")
            equipamento_info = next((eq for eq in st.session_state['equipamentos'] if eq['TAG'] == ativo_selecionado), None)
            
            if equipamento_info:
                st.write(f"**Fabricante:** {equipamento_info.get('Fabricante', 'N/A')}")
                st.write(f"**Modelo:** {equipamento_info.get('Modelo', 'N/A')}")
                st.write(f"**Potência:** {equipamento_info.get('Potencia', 'N/A')}")
                st.write(f"**Tensão:** {equipamento_info.get('Tensao', 'N/A')}")
                st.success("Dados validados com o sistema de cadastro e telemetria.")
    
    st.markdown("---")

    col_lateral, col_principal = st.columns([1, 3])
    
    # Área de Controle (Human-in-the-loop)
    with col_lateral:
        st.markdown("#### Parâmetros de Leitura")
        qtd_amostras = st.slider("Janela de Tempo (segundos)", min_value=10, max_value=100, value=30)
        
        if st.button("🔄 Iniciar Nova Coleta", use_container_width=True):
            # 1. Dispara o balão flutuante imediatamente ao clicar
            st.toast('Iniciando coleta de dados dos sensores...', icon='📡')
            
            with st.spinner("Lendo barramento de sensores..."):
                time.sleep(1.5) # Dá um tempinho para o usuário ler o balão e ver o loading
                st.session_state['df_telemetria'] = obter_dados_telemetria(qtd_amostras)
            
            # 2. Dispara o balão de sucesso após terminar de carregar os dados
            st.toast('Coleta finalizada com sucesso e gráfico atualizado!', icon='✅')
                
    # Inicializa os dados na primeira vez que abre a tela
    if 'df_telemetria' not in st.session_state:
        st.session_state['df_telemetria'] = obter_dados_telemetria(30)
        
    df_atual = st.session_state['df_telemetria']
    
    # Área de Exibição
    with col_principal:
        tab_grafico, tab_tabela = st.tabs(["📈 Gráfico Interativo (Plotly)", "🗄️ Histórico de Conversão (Bruto vs Real)"])
        
        with tab_grafico:
            st.markdown(f"**Análise de Comportamento do Motor: {ativo_selecionado}**")
            
            # Gráfico Plotly com UX avançada
            fig = px.line(
                df_atual, 
                x='Tempo (s)', 
                y='RPM_Convertido', 
                markers=True, 
                title="Evolução do RPM ao Longo do Tempo (Histórico da Sprint 1)",
                labels={'RPM_Convertido': 'RPM', 'Tempo (s)': 'Tempo em Segundos'}
            )
            
            # Ajuste de UI/UX
            fig.update_layout(
                hovermode="x unified", 
                xaxis_title="Janela de Tempo (s)",
                yaxis_title="Rotação por Minuto (RPM)",
                template="plotly_dark" 
            )
            
            # Exibe o gráfico do Plotly no Streamlit
            st.plotly_chart(fig, use_container_width=True)
            
        with tab_tabela:
            st.markdown("**Comparativo de Sinais Históricos**")
            st.dataframe(
                df_atual,
                use_container_width=True,
                hide_index=True
            )