import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage  # Reutilizando o Page Object que você criou!

# 🔄 AQUI ENTRA O PARAMETRIZAR:
# Dizemos ao Pytest para rodar o mesmo teste 3 vezes, mudando apenas o usuário!
@pytest.mark.parametrize("usuario", [
    "standard_user",           # Usuário comum
    "problem_user",            # Usuário que quebra imagens
    "performance_glitch_user"  # Usuário com lentidão de 5 segundos
])
def test_login_multiplos_usuarios_validos(page: Page, usuario):
    """Testa o login com diferentes perfis de usuários usando o padrão AAA"""
    
    # --- 1. ARRANGE (Preparar o ambiente) ---
    login_page = LoginPage(page)
    login_page.acessar_site()
    
    # --- 2. ACT (Executar as ações do teste) ---
    # O robô vai usar a variável 'usuario' que muda a cada rodada automaticamente
    login_page.realizar_login(usuario, "secret_sauce")
    
    # --- 3. ASSERT (Validar se o resultado deu certo) ---
    expect(page.locator(".title")).to_have_text("Products")
