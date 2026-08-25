🚀 Requisitos Funcionais e Técnicos Implementados
1. Filtro e Navegação Hierárquica (Planta / Área)
Interface dinâmica na barra lateral que permite filtrar ativos com base na sua localização geográfica e operacional (ex: Planta Matriz SP vs Planta Filial MG).

Atualização em tempo real das áreas disponíveis dependendo da planta selecionada.

2. Dashboard de Telemetria e Saúde do Ativo
Exibição de valores instantâneos recolhidos pelos sensores: Temperatura (°C), Vibração (mm/s) e Corrente (A).

Sistema visual de alertas baseado em limites operacionais críticos (Verde 🟢 para Normal, Amarelo 🟡 para Alerta, Vermelho 🔴 para Estado Crítico).

3. Visualização Avançada de Séries Temporais (Plotly)
Integração da biblioteca Plotly Express para fornecer gráficos interativos de linha (RPM ao longo do tempo).

Recursos avançados de UX: ferramentas de zoom, hover unificado para inspeção precisa de pontos e capacidade de exportar gráficos diretamente pela interface.

4. Integração de Cadastro Visual (OCR / Visão Computacional)
Bloco expansível (st.expander) que simula a captura da placa física do motor.

Cruzamento de dados entre os parâmetros extraídos por visão computacional e as informações persistidas no sistema.

💻 Como Instalar e Executar o Projeto
Pré-requisitos
Certifique-se de que tem o Python 3.8+ instalado na sua máquina.

1. Clonar o Repositório e Aceder à Pasta
"cd CS-FRONT-1"

2. Configurar e Ativar o Ambiente Virtual (Recomendado)
No Windows (PowerShell):
"python -m venv venv
.\venv\Scripts\activate"

3. Instalar as Dependências Necessárias
Instale o Streamlit e o Plotly para renderizar os gráficos dinâmicos:
"pip install streamlit plotly"

4. Executar a Aplicação
Se o ambiente virtual estiver ativado corretamente:
"streamlit run app.py"
Caso encontre problemas com as variáveis de ambiente, utilize o comando alternativo:
"python -m streamlit run app.py"
