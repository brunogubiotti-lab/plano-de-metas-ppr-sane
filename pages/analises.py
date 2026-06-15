# pages/analises.py
from dash import html
from components.sidebar import sidebar

def layout():
    return html.Div([
        sidebar(active_page="/analises"),
        html.Div(id="main-content", children=[
            html.Div(id="page-header", children=[
                html.Div([
                    html.Div("Análises", id="page-title"),
                    html.Div("Análises comparativas e tendências", id="page-subtitle"),
                ]),
            ]),
            html.Div(className="skeleton-page", children=[
                html.Div("🔍", className="skeleton-icon"),
                html.Div("Análises", className="skeleton-title"),
                html.Div("Página em construção. Aqui serão apresentadas análises de tendência e comparativos entre municípios.", className="skeleton-desc"),
            ]),
        ])
    ])
