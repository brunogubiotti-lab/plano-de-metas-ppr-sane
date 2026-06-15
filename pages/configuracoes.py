# pages/configuracoes.py
from dash import html
from components.sidebar import sidebar

def layout():
    return html.Div([
        sidebar(active_page="/configuracoes"),
        html.Div(id="main-content", children=[
            html.Div(id="page-header", children=[
                html.Div([
                    html.Div("Configurações", id="page-title"),
                    html.Div("Preferências do sistema e gestão de usuários", id="page-subtitle"),
                ]),
            ]),
            html.Div(className="skeleton-page", children=[
                html.Div("⚙️", className="skeleton-icon"),
                html.Div("Configurações", className="skeleton-title"),
                html.Div("Página em construção. Aqui serão gerenciados usuários, permissões e parâmetros do sistema.", className="skeleton-desc"),
            ]),
        ])
    ])
