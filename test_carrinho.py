from playwright.sync_api import Page, expect
from pages.login_page import LoginPage       # Importa o mapa da tela de Login
from pages.carrinho_page import CarrinhoPage # Importa o mapa da tela de Carrinho

URL_SITE = "https://saucedemo.com"

def test_adicionar_produto_ao_carrinho(page: Page):
    """Cenário 1: Validar que o contador aumenta ao adicionar um item"""
    # 1. Prepara as páginas que o robô vai usar
    login_page = LoginPage(page)
    carrinho_page = CarrinhoPage(page)
    
    # 2. Executa as ações usando as funções limpas das páginas
    login_page.acessar_site()
    login_page.realizar_login("standard_user", "secret_sauce")
    
    carrinho_page.adicionar_mochila()
    
    # 3. Validação (O 'expect' confere o resultado final)
    expect(carrinho_page.icone_contador_carrinho).to_have_text("1")


def test_remover_produto_do_carrinho(page: Page):
    """Cenário 2: Validar que o contador some ao remover o item"""
    login_page = LoginPage(page)
    carrinho_page = CarrinhoPage(page)
    
    login_page.acessar_site()
    login_page.realizar_login("standard_user", "secret_sauce")
    
    carrinho_page.adicionar_mochila()
    carrinho_page.remover_mochila()
    
    # Validação: Confere se o círculo vermelho sumiu/escondeu na tela
    expect(carrinho_page.icone_contador_carrinho).to_be_hidden()
