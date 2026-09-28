# test_checkout.py
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage

URL_SITE = "https://saucedemo.com"

def test_compra_de_mochila_com_sucesso(page: Page):
    """Cenário: Realizar o fluxo completo de compra de ponta a ponta (E2E)"""
    
    # --- 1. ARRANGE (Preparar as páginas e acessar o site) ---
    login_page = LoginPage(page)
    carrinho_page = CarrinhoPage(page)
    
    login_page.acessar_site()
    
    # --- 2. ACT (Executar todo o caminho do cliente) ---
    login_page.realizar_login("standard_user", "secret_sauce")
    
    carrinho_page.adicionar_mochila()
    carrinho_page.ir_para_o_carrinho()
    carrinho_page.iniciar_checkout()
    
    # Preenche os dados fictícios de envio
    carrinho_page.preencher_dados_envio("Seu Nome", "Seu Sobrenome", "12345-678")
    
    carrinho_page.finalizar_compra()
    
    # --- 3. ASSERT (Validar se a mensagem final de sucesso apareceu) ---
    mensagem_sucesso = page.locator(".complete-header")
    expect(mensagem_sucesso).to_have_text("Thank you for your order!")
