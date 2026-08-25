import streamlit as st

def renderizar_card_alerta(alerta):
    """
    Componente reutilizável para exibir um card de alerta padronizado.
    """
    with st.container():
        st.markdown(f"**{alerta['status']}**")
        st.write(f"**Diagnóstico NLP:** {alerta['resumo']}")
        st.info(f"💡 **Recomendação de Ação:** {alerta['acao']}")
        st.markdown("---")