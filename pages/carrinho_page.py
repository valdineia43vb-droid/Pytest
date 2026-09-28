# pages/carrinho_page.py
from playwright.sync_api import Page

class CarrinhoPage:
    def __init__(self, page: Page):
        self.page = page
        # Botões do fluxo do carrinho e checkout
        self.botao_adicionar_mochila = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.botao_remover_mochila = page.locator("[data-test='remove-sauce-labs-backpack']")
        self.icone_contador_carrinho = page.locator(".shopping_cart_badge")
        self.link_carrinho = page.locator(".shopping_cart_link")
        
        # Elementos da tela de Checkout (Formulário)
        self.botao_checkout = page.locator("[data-test='checkout']")
        self.input_nome = page.locator("[data-test='firstName']")
        self.input_sobrenome = page.locator("[data-test='lastName']")
        self.input_cep = page.locator("[data-test='postalCode']")
        self.botao_continuar = page.locator("[data-test='continue']")
        
        # Elemento da tela de Finalização
        self.botao_finalizar = page.locator("[data-test='finish']")

    def adicionar_mochila(self):
        self.botao_adicionar_mochila.click()

    def ir_para_o_carrinho(self):
        self.link_carrinho.click()

    def iniciar_checkout(self):
        self.botao_checkout.click()

    def preencher_dados_envio(self, nome, sobrenome, cep):
        self.input_nome.fill(nome)
        self.input_sobrenome.fill(sobrenome)
        self.input_cep.fill(cep)
        self.botao_continuar.click()

    def finalizar_compra(self):
        self.botao_finalizar.click()

    def remover_mochila(self):
        self.botao_remover_mochila.click()
