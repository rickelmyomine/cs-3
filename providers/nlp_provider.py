import random

def gerar_resumo_nlp(status, temp, vib, corr):
    """
    Simula uma API de IA (ex: OpenAI/Gemini).
    Gera um texto analítico baseado na severidade e nos dados vitais.
    """
    if status == "🟡 Atenção":
        resumos = [
            f"Análise térmica: A temperatura de {temp:.1f}°C e a corrente de {corr:.1f}A indicam esforço anormal do rotor.",
            f"Padrão vibracional irregular ({vib:.1f} mm/s) compatível com desgaste inicial de rolamento."
        ]
        acoes = [
            "Reduzir a carga da linha em 15% e agendar inspeção visual.",
            "Aumentar fluxo de lubrificação do mancal preventivamente."
        ]
        return random.choice(resumos), random.choice(acoes)
    
    elif status == "🔴 Crítico":
        resumos = [
            f"Risco de falha! Vibração de {vib:.1f} mm/s aponta para possível quebra de mancal.",
            f"Sobrecarga térmica crítica ({temp:.1f}°C). Risco de derretimento do isolamento do estator."
        ]
        acoes = [
            "🚨 PARADA EMERGENCIAL. Isolar equipamento e iniciar manutenção.",
            "🚨 Desligar motor instantaneamente. Risco severo à operação."
        ]
        return random.choice(resumos), random.choice(acoes)
        
    return "Operação estável.", "Manter rotina de monitoramento."