# pages/visao_geral.py
# ============================================================
# Página "Visão Geral" — idêntica ao layout da imagem.
# Contém:
#   - Grupo 1: 5 cards com donut chart (indicadores institucionais)
#   - Grupo 2: 3 cards com gauge (indicadores de gestão) + tabela histórica
# ============================================================

from dash import html, dcc
import plotly.graph_objects as go

# Importa os dados mock centralizados
from data.mock_data import (
    INDICADORES_INSTITUCIONAIS,
    INDICADORES_GESTAO,
    get_historico_df,
)
from components.sidebar import sidebar

# ── Paleta de cores ────────────────────────────────────────
COR_NAVY   = "#0D1B3E"
COR_AZUL   = "#1E6FD9"
COR_VERDE  = "#22C55E"
COR_CINZA  = "#E5E7EB"
COR_TRACK  = "#EFF6FF"   # fundo do arco não preenchido do donut


# ══════════════════════════════════════════════════════════
#  FUNÇÕES DE GRÁFICO
# ══════════════════════════════════════════════════════════

def make_donut(valor: float, meta: float) -> go.Figure:
    """
    Cria um gráfico de rosca (donut) mostrando valor vs. meta.

    Plotly representa o donut como um gráfico de pizza com buraco (hole).
    Usamos dois segmentos:
      1. Preenchido  → proporção do valor dentro de 120% da meta (teto visual)
      2. Vazio       → restante (cor cinza clara)

    Parâmetros
    ----------
    valor : float   — valor real do indicador
    meta  : float   — meta a atingir
    """
    # Teto visual = 120% da meta, para não ultrapassar o círculo
    teto = meta * 1.2
    preenchido = min(valor, teto)
    vazio = max(teto - preenchido, 0)

    fig = go.Figure(go.Pie(
        values=[preenchido, vazio],
        hole=0.65,          # tamanho do buraco central (65% = rosca)
        showlegend=False,
        textinfo="none",    # sem rótulos sobre os segmentos
        marker=dict(
            colors=[COR_AZUL, COR_TRACK],   # preenchido azul | vazio azul-claro
            line=dict(width=0),              # sem borda entre segmentos
        ),
        sort=False,         # mantém a ordem: preenchido primeiro (horário)
        direction="clockwise",
    ))

    # Anotação central com o valor numérico grande
    fig.add_annotation(
        text=f"<b>{valor}</b>",
        x=0.5, y=0.55,
        font=dict(size=20, color=COR_NAVY, family="Inter"),
        showarrow=False,
        xanchor="center",
    )
    # Linha menor com "de X.X" (a meta)
    fig.add_annotation(
        text=f"de {meta}",
        x=0.5, y=0.38,
        font=dict(size=11, color="#6B7280", family="Inter"),
        showarrow=False,
        xanchor="center",
    )

    fig.update_layout(
        margin=dict(t=4, b=4, l=4, r=4),
        paper_bgcolor="rgba(0,0,0,0)",  # transparente (herda o card branco)
        plot_bgcolor="rgba(0,0,0,0)",
        height=140,
    )
    return fig


def make_gauge(valor: float, meta: float, max_val: float) -> go.Figure:
    """
    Cria um velocímetro (gauge) semicircular.

    Plotly oferece go.Indicator com mode="gauge+number".
    Aqui usamos apenas mode="gauge" para ter controle total
    sobre a anotação central.

    Parâmetros
    ----------
    valor   : float — valor atual
    meta    : float — meta (exibida como marcação no gauge)
    max_val : float — valor máximo do eixo do gauge
    """
    fig = go.Figure(go.Indicator(
        mode="gauge",
        value=valor,
        gauge=dict(
            axis=dict(
                range=[0, max_val],
                tickwidth=1,
                tickcolor="#D1D5DB",
                tickfont=dict(size=9, color="#9CA3AF"),
                nticks=5,
            ),
            bar=dict(color=COR_AZUL, thickness=0.25),   # ponteiro azul
            bgcolor="white",
            borderwidth=0,
            steps=[
                # Faixas coloridas de fundo do gauge
                dict(range=[0, meta * 0.6],  color="#FEE2E2"),  # vermelho-claro
                dict(range=[meta * 0.6, meta], color="#FEF9C3"),  # amarelo-claro
                dict(range=[meta, max_val], color="#DCFCE7"),   # verde-claro
            ],
            threshold=dict(
                line=dict(color=COR_VERDE, width=3),
                thickness=0.75,
                value=meta,   # marca a meta com linha verde
            ),
        ),
    ))

    # Anotação com valor formatado no centro do gauge
    if valor >= 1000:
        # Formata milhares com ponto: 125430 → 125.430
        valor_fmt = f"{valor:,.0f}".replace(",", ".")
    else:
        valor_fmt = str(valor)

    fig.add_annotation(
        text=f"<b>{valor_fmt}</b>",
        x=0.5, y=0.18,
        font=dict(size=16, color=COR_NAVY, family="Inter"),
        showarrow=False,
        xanchor="center",
    )

    meta_fmt = f"{meta:,.0f}".replace(",", ".") if meta >= 1000 else str(int(meta))
    fig.add_annotation(
        text=f"Meta {meta_fmt}",
        x=0.5, y=0.02,
        font=dict(size=10, color="#6B7280", family="Inter"),
        showarrow=False,
        xanchor="center",
    )

    fig.update_layout(
        margin=dict(t=0, b=0, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        height=150,
    )
    return fig


# ══════════════════════════════════════════════════════════
#  FUNÇÕES DE COMPONENTES HTML
# ══════════════════════════════════════════════════════════

def card_institucional(ind: dict) -> html.Div:
    """
    Monta um card do Grupo 1 (indicador institucional).

    Estrutura:
      ┌─────────────────┐
      │ [ícone] Nome    │
      │   [donut chart] │
      │   Meta: X.X     │
      │   Atingimento % │
      └─────────────────┘
    """
    atingimento = (ind["valor"] / ind["meta"]) * 100

    return html.Div(
        className="kpi-card",
        children=[
            # Linha superior: ícone colorido + nome
            html.Div(
                className="kpi-card-icon-row",
                children=[
                    html.Div(
                        ind["icone"],
                        className="kpi-card-icon",
                        style={"backgroundColor": ind["cor_icone"] + "22"}  # 22 = 13% opacidade
                    ),
                    html.Span(ind["nome"], className="kpi-card-name"),
                ]
            ),
            # Gráfico de rosca (donut)
            dcc.Graph(
                figure=make_donut(ind["valor"], ind["meta"]),
                config={"displayModeBar": False},  # esconde a barra de ferramentas do plotly
                style={"margin": "0 auto"},
            ),
            # Linha "Meta: X.X"
            html.Div([
                html.Span("🎯 Meta:  ", style={"color": "#9CA3AF", "fontSize": "12px"}),
                html.Span(str(ind["meta"]), className="kpi-meta-value", style={"fontSize": "12px"}),
            ], className="kpi-meta-row"),
            # Percentual de atingimento em verde
            html.Div(
                f"Atingimento:  {atingimento:.1f}%",
                className="kpi-atingimento",
            ),
        ]
    )


def card_gestao(ind: dict) -> html.Div:
    """
    Monta um card do Grupo 2 (indicador de gestão) com gauge lateral.

    Estrutura horizontal:
      ┌──────────────────────────────────────┐
      │ [ícone]                              │
      │ Nome         [  gauge chart  ]       │
      │ Valor grande                         │
      │ ↑ variação%                          │
      │ vs. mês anterior                     │
      └──────────────────────────────────────┘
    """
    # Formata o valor conforme o tipo (ex: gratificação é monetário)
    if ind["valor"] >= 1000:
        valor_fmt = f"R$ {ind['valor']:,.0f}".replace(",", ".")
    else:
        valor_fmt = f"{ind['valor']}"

    return html.Div(
        className="gauge-card",
        children=[
            # Lado esquerdo: ícone, rótulo, valor, variação
            html.Div(
                className="gauge-card-left",
                children=[
                    html.Div(ind["icone"], className="gauge-card-icon"),
                    html.Div(ind["nome"], className="gauge-card-label"),
                    html.Div(valor_fmt, className="gauge-card-value"),
                    html.Div(f"↑ {ind['variacao']}%", className="gauge-card-variation"),
                    html.Div("vs. mês anterior", className="gauge-card-variation-label"),
                ]
            ),
            # Lado direito: gráfico gauge
            html.Div(
                className="gauge-card-chart",
                children=[
                    dcc.Graph(
                        figure=make_gauge(ind["valor"], ind["meta"], ind["max_gauge"]),
                        config={"displayModeBar": False},
                    )
                ]
            ),
        ]
    )


def tabela_historico() -> html.Div:
    """
    Monta a tabela histórica com cabeçalho navy e linhas alternadas.
    Usa HTML puro (sem dash_table) para controle visual total.
    """
    df = get_historico_df()

    # Cabeçalho
    header = html.Div(
        className="table-header-row",
        children=[
            html.Span("Data",               className="table-header-cell"),
            html.Span("Indicador Próprio",  className="table-header-cell"),
            html.Span("Indicador Ponderado",className="table-header-cell"),
            html.Span("Gratificação",       className="table-header-cell"),
        ]
    )

    # Linhas de dados
    rows = []
    for _, row in df.iterrows():
        grat_fmt = f"R$ {row['gratificacao']:,.0f}".replace(",", ".")
        rows.append(
            html.Div(
                className="table-data-row",
                children=[
                    html.Span(row["data"]),
                    html.Span(str(row["proprio"])),
                    html.Span(str(row["ponderado"])),
                    html.Span(grat_fmt),
                ]
            )
        )

    return html.Div(
        className="historico-card",
        children=[
            html.Div("Histórico dos Indicadores", className="historico-title"),
            header,
            html.Div(rows),
        ]
    )


# ══════════════════════════════════════════════════════════
#  LAYOUT PRINCIPAL DA PÁGINA
# ══════════════════════════════════════════════════════════

def layout() -> html.Div:
    """
    Retorna o layout completo da página Visão Geral.
    Chamada pelo app.py via roteamento de URL.
    """
    return html.Div([

        # ── Sidebar fixa (componente reutilizável) ──────────
        sidebar(active_page="/"),

        # ── Conteúdo principal ──────────────────────────────
        html.Div(
            id="main-content",
            children=[

                # ── Header: título + filtro de data ──────────
                html.Div(
                    id="page-header",
                    children=[
                        html.Div([
                            html.Div("Painel de Desempenho", id="page-title"),
                            html.Div("Indicadores institucionais e de gestão", id="page-subtitle"),
                        ]),
                        html.Div(
                            ["📅 01/05/2024 — 31/05/2024"],
                            id="date-filter",
                        ),
                    ]
                ),

                # ══ GRUPO 1 — Indicadores Institucionais ═════
                html.Div(
                    className="section-title mb-16",
                    children=[
                        "Grupo 1 — Indicadores Institucionais",
                        html.Span("ℹ", className="section-info-icon"),
                    ]
                ),

                # 5 cards em linha usando CSS grid via style inline
                html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "repeat(5, 1fr)",
                        "gap": "16px",
                        "marginBottom": "32px",
                    },
                    children=[
                        card_institucional(ind) for ind in INDICADORES_INSTITUCIONAIS
                    ]
                ),

                # ══ GRUPO 2 — Indicadores de Gestão ══════════
                html.Div(
                    className="section-title mb-16",
                    children=[
                        "Grupo 2 — Indicadores de Gestão",
                        html.Span("ℹ", className="section-info-icon"),
                    ]
                ),

                # Grid: 3 colunas à esquerda (gauges) + 4 colunas à direita (tabela)
                html.Div(
                    style={
                        "display": "grid",
                        "gridTemplateColumns": "5fr 6fr",  # proporção similar ao layout
                        "gap": "20px",
                        "alignItems": "start",
                    },
                    children=[
                        # Coluna esquerda: 3 cards de gauge empilhados
                        html.Div([
                            card_gestao(ind) for ind in INDICADORES_GESTAO
                        ]),
                        # Coluna direita: tabela histórica
                        tabela_historico(),
                    ]
                ),

            ]
        )
    ])
