# 🧪 Automação de Testes E2E - Sauce Demo

Projeto desenvolvido para praticar e consolidar conceitos de **Automação de Testes de Software** utilizando a biblioteca **Playwright com Python** e o framework **Pytest**. O projeto aplica as melhores práticas de mercado, como o padrão de arquitetura **Page Object Model (POM)** e a estruturação de testes **AAA (Arrange, Act, Assert)**.

---

## 🎯 Cenários Automatizados

O escopo dos testes cobre a aplicação fictícia de e-commerce **Sauce Demo**, englobando:
- **Feature de Autenticação:** Login com sucesso, validação de bloqueio de usuário e testes simultâneos com múltiplos perfis válidos usando `@pytest.mark.parametrize`.
- **Feature de Carrinho de Compras:** Adição e remoção de produtos, com verificação dinâmica do contador do carrinho.
- **Feature de Checkout:** Fluxo completo de ponta a ponta (*End-to-End*) realizando a compra de itens com sucesso.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework de Testes:** Pytest
- **Ferramenta de Automação:** Playwright (Python)
- **Design Pattern:** Page Object Model (POM)
- **Relatórios:** Pytest-HTML

---

## 🚀 Como Executar o Projeto Localmente

Se você deseja baixar e rodar este projeto na sua máquina, siga os passos abaixo no terminal:

### 1. Clonar o repositório
```bash
git clone https://github.com
cd automacao-saucedemo-playwright
```

### 2. Instalar as dependências
```bash
pip install pytest-playwright pytest-html
playwright install
```

### 3. Executar os testes

- **Modo Interativo (Visível):**
  ```bash
  pytest --headed
  ```

- **Gerando Relatório Visual HTML:**
  ```bash
  pytest --html=relatorio_final.html --headed
  ```

---
💡 *Projeto desenvolvido por uma estudante de Análise e Desenvolvimento de Sistemas (ADS) na Universidade Anhanguera com foco em Engenharia de Qualidade de Software (QA).*
