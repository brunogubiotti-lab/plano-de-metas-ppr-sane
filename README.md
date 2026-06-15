# Plano de Metas — SANESUL

Dashboard de KPIs regulatórios construído com **Dash + Plotly + Pandas**.

## Estrutura do projeto

```
plano-metas-sanesul/
│
├── app.py                  ← Ponto de entrada; roteamento de URLs
├── requirements.txt        ← Dependências Python
│
├── assets/
│   └── style.css           ← CSS global (cores, sidebar, cards, tabelas)
│
├── components/
│   └── sidebar.py          ← Sidebar reutilizável (importada em cada página)
│
├── data/
│   └── mock_data.py        ← Dados fictícios (substituir por leitura de Excel)
│
└── pages/
    ├── visao_geral.py      ← Página completa (Grupo 1 + Grupo 2)
    ├── indicadores.py      ← Esqueleto
    ├── relatorios.py       ← Esqueleto
    ├── analises.py         ← Esqueleto
    ├── metas.py            ← Esqueleto
    ├── exportacoes.py      ← Esqueleto
    └── configuracoes.py    ← Esqueleto
```

## Instalação

```bash
# 1. Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar em desenvolvimento
python app.py
# Acesse: http://localhost:8050
```

## Deploy gratuito no Render.com

1. Faça push do projeto para um repositório GitHub privado
2. Acesse https://render.com → New Web Service
3. Conecte o repositório
4. Configure:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:server`
5. Deploy automático a cada `git push`

## Trocar dados mock por Excel real

Em `data/mock_data.py`, substitua as constantes pela leitura do arquivo:

```python
import pandas as pd

def get_historico_df():
    return pd.read_excel(
        "data/SISPLAN_BD.xlsx",
        sheet_name="METAS",
        dtype=str
    )
```

## Paleta de cores

| Token        | Hex       | Uso                          |
|--------------|-----------|------------------------------|
| Navy         | `#0D1B3E` | Sidebar, títulos, cabeçalho  |
| Azul         | `#1E6FD9` | Itens ativos, gráficos       |
| Verde        | `#22C55E` | Atingimento, variação +      |
| Cinza claro  | `#E5E7EB` | Bordas, fundos neutros       |
