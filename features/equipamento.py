import re
from providers.db_mock import EquipamentoRepository

def cadastrar_equipamento(tag, modelo, fabricante, potencia, tensao):
    """
    Função responsável por validar a entrada (segurança) e salvar via repositório.
    """
    # 1. Blindagem de Input: Validação de Segurança (Regex)
    # Exige 3 letras maiúsculas, um hífen e 3 números (Ex: MOT-001)
    padrao_tag = r"^[A-Z]{3}-\d{3}$"
    if not re.match(padrao_tag, tag):
        return False, "Formato de TAG inválido. Use o padrão industrial (Ex: MOT-001, BMB-123)."

    # 2. Regra de Negócio: Verifica duplicidade consultando o "banco"
    if EquipamentoRepository.tag_existe(tag):
        return False, f"A TAG {tag} já está cadastrada no sistema."
    
    # 3. Preparação do Objeto
    novo_equipamento = {
        "TAG": tag,
        "Modelo": modelo,
        "Fabricante": fabricante,
        "Potencia": potencia,
        "Tensao": tensao
    }
    
    # 4. Persistência
    EquipamentoRepository.salvar(novo_equipamento)
    
    return True, "Equipamento cadastrado com sucesso!"