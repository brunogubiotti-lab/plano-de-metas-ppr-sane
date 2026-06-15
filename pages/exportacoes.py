# pages/exportacoes.py
from dash import html
from components.sidebar import sidebar

def layout():
    return html.Div([
        sidebar(active_page="/exportacoes"),
        html.Div(id="main-content", children=[
            html.Div(id="page-header", children=[
                html.Div([
                    html.Div("Exportações", id="page-title"),
                    html.Div("Download de dados e relatórios em Excel/PDF", id="page-subtitle"),
                ]),
            ]),
            html.Div(className="skeleton-page", children=[
                html.Div("📤", className="skeleton-icon"),
                html.Div("Exportações", className="skeleton-title"),
                html.Div("Página em construção. Aqui será possível exportar dados em .xlsx e relatórios em .pdf.", className="skeleton-desc"),
            ]),
        ])
    ])
