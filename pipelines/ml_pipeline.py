def detectar_anomalia(temperatura, vibracao, corrente):
    """
    Recebe os dados de telemetria e passa pelo modelo de ML.
    Retorna o status e um diagnóstico preliminar.
    """
    # Lógica que simula o modelo de Machine Learning
    if vibracao > 8.0 or temperatura > 85.0:
        return "🔴 Crítico", "Padrão anômalo severo detectado nos eixos de vibração/temperatura."
    
    elif corrente > 50.0 or vibracao > 6.0:
        return "🟡 Atenção", "Desvio operacional detectado. Risco de sobrecarga a médio prazo."
    
    else:
        return "🟢 Saudável", "Padrões operacionais alinhados com a baseline histórica."    