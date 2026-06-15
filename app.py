# app.py
# ============================================================
# Ponto de entrada do sistema Plano de Metas — SANESUL.
#
# Responsabilidades:
#   1. Inicializar o app Dash com tema Bootstrap
#   2. Definir o layout raiz (container de URL + conteúdo dinâmico)
#   3. Callback de roteamento: URL → página correta
#   4. Rodar o servidor
#
# Para executar:
#   python app.py
# Para produção (Render.com):
#   gunicorn app:server
# ============================================================

import dash
from dash import html, dcc, Input, Output

# dash-bootstrap-components fornece grid responsivo e utilitários de estilo
import dash_bootstrap_components as dbc

# Importa o layout de cada página
from pages import (
    visao_geral,
    indicadores,
    relatorios,
    analises,
    metas,
    exportacoes,
    configuracoes,
)

# ── Inicialização do app ────────────────────────────────────
# suppress_callback_exceptions=True é necessário quando os componentes
# referenciados nos callbacks só existem depois do roteamento (páginas dinâmicas)
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    # BOOTSTRAP garante o grid de 12 colunas e utilitários CSS
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        # Google Fonts: Inter (fonte do layout original)
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
    ],
    # Meta tag para responsividade mobile
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

# Expõe o servidor WSGI para o gunicorn (deploy em produção)
server = app.server

# Título da aba do navegador
app.title = "Plano de Metas — SANESUL"


# ── Layout raiz ─────────────────────────────────────────────
# dcc.Location monitora a URL atual e dispara o callback de roteamento.
# O div #page-content é o contêiner onde cada página é renderizada.
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  # não recarrega a página ao mudar URL
    html.Div(id="page-content"),             # conteúdo dinâmico injetado pelo callback
])


# ── Callback de roteamento ───────────────────────────────────
# Sempre que o pathname da URL muda, este callback é chamado
# e retorna o layout da página correspondente.
@app.callback(
    Output("page-content", "children"),   # onde o layout será inserido
    Input("url", "pathname"),             # o que aciona: mudança de URL
)
def render_page(pathname: str):
    """
    Mapeia pathname → layout da página.

    Exemplo: usuário acessa /indicadores
    → pathname = "/indicadores"
    → retorna indicadores.layout()
    """
    rota_para_pagina = {
        "/":               visao_geral.layout,
        "/indicadores":    indicadores.layout,
        "/relatorios":     relatorios.layout,
        "/analises":       analises.layout,
        "/metas":          metas.layout,
        "/exportacoes":    exportacoes.layout,
        "/configuracoes":  configuracoes.layout,
    }

    # Busca a função de layout; default: Visão Geral se rota não encontrada
    pagina_fn = rota_para_pagina.get(pathname, visao_geral.layout)
    return pagina_fn()


# ── Ponto de entrada ─────────────────────────────────────────
if __name__ == "__main__":
    # debug=True → recarrega automaticamente ao salvar arquivos (desenvolvimento)
    # host="0.0.0.0" → aceita conexões de outros dispositivos na rede local
    app.run(debug=True, host="0.0.0.0", port=8050)
