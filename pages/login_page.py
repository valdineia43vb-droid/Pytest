from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Aqui guardamos todos os "endereços" (seletores) dos botões da tela de login
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")

    def acessar_site(self):
        self.page.goto("https://saucedemo.com")

    def realizar_login(self, usuario, senha):
        # Uma única ação que digita o usuário, senha e clica no botão
        self.username_input.fill(usuario)
        self.password_input.fill(senha)
        self.login_button.click()
