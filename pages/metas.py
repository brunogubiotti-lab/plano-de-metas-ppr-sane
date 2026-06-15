# pages/metas.py
from dash import html
from components.sidebar import sidebar

def layout():
    return html.Div([
        sidebar(active_page="/metas"),
        html.Div(id="main-content", children=[
            html.Div(id="page-header", children=[
                html.Div([
                    html.Div("Metas", id="page-title"),
                    html.Div("Contratos de Programa — metas por município e horizonte", id="page-subtitle"),
                ]),
            ]),
            html.Div(className="skeleton-page", children=[
                html.Div("🎯", className="skeleton-icon"),
                html.Div("Metas", className="skeleton-title"),
                html.Div("Página em construção. Aqui serão exibidas as metas dos 68 municípios (COB_AGUA, COB_ESG, PERDAS, TRAT_ESG, IQA, DBO5) por horizonte (2029–2041).", className="skeleton-desc"),
            ]),
        ])
    ])
