# data/mock_data.py
# ============================================================
# Dados fictícios para desenvolvimento inicial.
# Quando os Excels da SANESUL estiverem prontos,
# substituir estas constantes por funções que leem o arquivo.
# ============================================================

import pandas as pd

# ----------------------------------------------------------
# Grupo 1 – Indicadores Institucionais
# Cada dict vira um card com donut chart
# ----------------------------------------------------------
INDICADORES_INSTITUCIONAIS = [
    {
        "id": "IA",
        "nome": "IA",
        "descricao": "Índice de Abastecimento",
        "valor": 84.7,
        "meta": 80.0,
        "icone": "🧠",
        "cor_icone": "#1E6FD9",
    },
    {
        "id": "IPL",
        "nome": "IPL",
        "descricao": "Índice de Perdas Lineares",
        "valor": 76.3,
        "meta": 75.0,
        "icone": "👥",
        "cor_icone": "#6366F1",
    },
    {
        "id": "IE",
        "nome": "IE",
        "descricao": "Índice de Esgotamento",
        "valor": 88.1,
        "meta": 85.0,
        "icone": "📊",
        "cor_icone": "#0891B2",
    },
    {
        "id": "IQA",
        "nome": "IQA",
        "descricao": "Índice de Qualidade da Água",
        "valor": 91.2,
        "meta": 90.0,
        "icone": "💧",
        "cor_icone": "#0D9488",
    },
    {
        "id": "Mdex",
        "nome": "Mdex",
        "descricao": "Índice Multidimensional",
        "valor": 73.5,
        "meta": 70.0,
        "icone": "⭐",
        "cor_icone": "#7C3AED",
    },
]

# ----------------------------------------------------------
# Grupo 2 – Indicadores de Gestão
# Três cards com gauge (velocímetro) + variação vs. mês anterior
# ----------------------------------------------------------
INDICADORES_GESTAO = [
    {
        "id": "proprio",
        "nome": "Indicador Próprio",
        "valor": 68.9,
        "meta": 100,
        "variacao": 5.4,       # % vs. mês anterior
        "icone": "🎯",
        "prefixo": "",
        "sufixo": "",
        "max_gauge": 100,
    },
    {
        "id": "ponderado",
        "nome": "Indicador Ponderado",
        "valor": 74.6,
        "meta": 100,
        "variacao": 6.7,
        "icone": "⚖️",
        "prefixo": "",
        "sufixo": "",
        "max_gauge": 100,
    },
    {
        "id": "gratificacao",
        "nome": "Gratificação",
        "valor": 125430,
        "meta": 150000,
        "variacao": 8.2,
        "icone": "🎁",
        "prefixo": "R$ ",
        "sufixo": "",
        "max_gauge": 200000,
    },
]

# ----------------------------------------------------------
# Histórico mensal — aparece na tabela à direita
# Lista de dicts; cada linha é um mês
# ----------------------------------------------------------
HISTORICO = [
    {"data": "01/05/2024", "proprio": 68.9, "ponderado": 74.6, "gratificacao": 125430},
    {"data": "01/04/2024", "proprio": 65.4, "ponderado": 70.1, "gratificacao": 115920},
    {"data": "01/03/2024", "proprio": 63.1, "ponderado": 68.5, "gratificacao": 112340},
    {"data": "01/02/2024", "proprio": 60.2, "ponderado": 66.2, "gratificacao": 107850},
    {"data": "01/01/2024", "proprio": 56.8, "ponderado": 63.4, "gratificacao": 102110},
    {"data": "01/12/2023", "proprio": 55.1, "ponderado": 61.0, "gratificacao": 98560},
    {"data": "01/11/2023", "proprio": 53.0, "ponderado": 59.2, "gratificacao": 96120},
    {"data": "01/10/2023", "proprio": 51.3, "ponderado": 57.8, "gratificacao": 93870},
    {"data": "01/09/2023", "proprio": 50.2, "ponderado": 56.4, "gratificacao": 91430},
    {"data": "01/08/2023", "proprio": 48.7, "ponderado": 54.9, "gratificacao": 89210},
    {"data": "01/07/2023", "proprio": 47.1, "ponderado": 53.2, "gratificacao": 87150},
    {"data": "01/06/2023", "proprio": 45.6, "ponderado": 51.7, "gratificacao": 85230},
]

def get_historico_df() -> pd.DataFrame:
    """
    Retorna o histórico como DataFrame pandas.
    Quando houver Excel real, esta função fará:
        df = pd.read_excel('data/dados.xlsx', sheet_name='Historico')
        return df
    """
    return pd.DataFrame(HISTORICO)
