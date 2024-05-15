# Análise de Ações com Python

Este projeto realiza análises de ações do mercado financeiro usando Python. Utilizamos as bibliotecas `yfinance` para obter dados financeiros, `matplotlib` para visualização dos dados e `pandas` para manipulação de dados. O projeto foca especificamente na ação BBAS3 (Banco do Brasil S.A.), analisando indicadores como Bandas de Bollinger, Índice de Força Relativa (RSI) e Oscilador Estocástico.

## Funcionalidades

- **Coleta de Dados**: Obtenha dados históricos de ações diretamente do Yahoo Finance.
- **Análise Técnica**: Realize análise técnica com:
  - Bandas de Bollinger
  - RSI (Índice de Força Relativa)
  - Oscilador Estocástico
- **Visualização de Dados**: Gere gráficos para visualizar os indicadores mencionados.
- **Recomendação de Compra**: Fornece uma recomendação baseada em condições estatísticas se hoje é um bom dia para comprar ações.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido utilizando Python 3.8. Além disso, você precisará de um ambiente virtual para instalar e executar as bibliotecas necessárias.

## Configuração

Para configurar este projeto, siga as instruções abaixo:

1. Clone o repositório para sua máquina local:
git clone https://github.com/seu-usuario/seu-repositorio.git
2. Navegue até o diretório do projeto:
cd analise_BBAS3
3. Crie um ambiente virtual:
python -m venv venv
4. Ative o ambiente virtual:
- Windows:
  ```
  .\venv\Scripts\activate
  ```
- macOS/Linux:
  ```
  source venv/bin/activate
  ```
5. Instale as dependências do projeto:
pip install -r requirements.txt

## Uso

Para executar o script de análise, utilize o comando:
python src/analysis.py

Os gráficos gerados e a recomendação de compra serão exibidos conforme definido no script.

## Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para forkar o projeto, fazer melhorias e criar um pull request. Se você encontrar algum problema, por favor, abra uma issue no repositório do GitHub.

## Contato

Gabriel Vezono – gvezono@gmail.com

Link do Projeto: https://github.com/gvezono/analise_BBAS3.git