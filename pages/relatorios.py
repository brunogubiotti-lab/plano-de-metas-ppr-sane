# pages/relatorios.py
from dash import html
from components.sidebar import sidebar

def layout():
    return html.Div([
        sidebar(active_page="/relatorios"),
        html.Div(id="main-content", children=[
            html.Div(id="page-header", children=[
                html.Div([
                    html.Div("Relatórios", id="page-title"),
                    html.Div("Geração e exportação de relatórios regulatórios", id="page-subtitle"),
                ]),
            ]),
            html.Div(className="skeleton-page", children=[
                html.Div("📋", className="skeleton-icon"),
                html.Div("Relatórios", className="skeleton-title"),
                html.Div("Página em construção. Aqui serão gerados os relatórios para AGEMS e ANA.", className="skeleton-desc"),
            ]),
        ])
    ])
