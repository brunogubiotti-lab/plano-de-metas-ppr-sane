# components/sidebar.py
# ============================================================
# Sidebar fixa reutilizável.
# Recebe `active_page` (str) para destacar o item atual.
# Importar em cada página: from components.sidebar import sidebar
# ============================================================

from dash import html

# Itens do menu: (rótulo, href, emoji-ícone)
NAV_ITEMS = [
    ("Visão Geral",    "/",              "📊"),
    ("Indicadores",   "/indicadores",   "📈"),
    ("Relatórios",    "/relatorios",    "📋"),
    ("Análises",      "/analises",      "🔍"),
    ("Metas",         "/metas",         "🎯"),
    ("Exportações",   "/exportacoes",   "📤"),
    ("Configurações", "/configuracoes", "⚙️"),
]


def sidebar(active_page: str = "/") -> html.Div:
    """
    Gera a sidebar com o item ativo destacado.

    Parâmetros
    ----------
    active_page : str
        O href da página atual, ex: "/indicadores".
        O item correspondente recebe a classe CSS 'active'.

    Retorna
    -------
    html.Div
        Elemento Dash com toda a sidebar montada.
    """

    # Monta cada item do menu dinamicamente
    nav_links = []
    for label, href, icon in NAV_ITEMS:
        # Define classe CSS: 'nav-item active' se for a página atual, senão só 'nav-item'
        css_class = "nav-item active" if href == active_page else "nav-item"

        link = html.A(
            children=[
                html.Span(icon, className="nav-icon"),  # ícone emoji
                html.Span(label),                        # rótulo textual
            ],
            href=href,
            className=css_class,
        )
        nav_links.append(link)

    return html.Div(
        id="sidebar",
        children=[
            # ---- Cabeçalho com logo ----
            html.Div(
                id="sidebar-header",
                children=[
                    html.Div(
                        id="sidebar-logo-row",
                        children=[
                            # Quadrado azul com ícone de gráfico
                            html.Div("📊", id="sidebar-logo-icon"),
                            html.Div([
                                html.Div("Plano de Metas", id="sidebar-title"),
                                html.Div("SANESUL", id="sidebar-subtitle"),
                            ])
                        ]
                    )
                ]
            ),

            # ---- Navegação ----
            html.Nav(nav_links, id="sidebar-nav"),

            # ---- Rodapé com avatar do usuário ----
            html.Div(
                id="sidebar-footer",
                children=[
                    html.Div("AD", id="user-avatar"),   # iniciais
                    html.Div([
                        html.Div("Admin", id="user-name"),
                        html.Div("Administrador", id="user-role"),
                    ])
                ]
            ),
        ]
    )
