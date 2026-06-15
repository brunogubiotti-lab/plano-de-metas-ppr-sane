# pages/indicadores.py
from dash import html
from components.sidebar import sidebar

def layout():
    return html.Div([
        sidebar(active_page="/indicadores"),
        html.Div(id="main-content", children=[
            html.Div(id="page-header", children=[
                html.Div([
                    html.Div("Indicadores", id="page-title"),
                    html.Div("Detalhamento por indicador e município", id="page-subtitle"),
                ]),
            ]),
            html.Div(className="skeleton-page", children=[
                html.Div("📈", className="skeleton-icon"),
                html.Div("Indicadores", className="skeleton-title"),
                html.Div("Página em construção. Aqui serão exibidos os gráficos detalhados de cada indicador regulatório.", className="skeleton-desc"),
            ]),
        ])
    ])
