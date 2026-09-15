# API ETL — DummyJSON Products

Pipeline de ETL desenvolvido em Python para consumo de dados de uma API REST, processamento, filtragem e armazenamento dos dados em arquivos JSON.

## 🎯 Objetivo

Praticar conceitos fundamentais de Engenharia de Dados, incluindo:

* Consumo de API REST
* Paginação
* Tratamento de erros
* Manipulação de dados JSON
* Transformação e filtragem de dados
* Exportação de dados

## 🛠️ Tecnologias

* Python
* Requests
* JSON
* REST API
* Git

## 🔄 Pipeline

```text
DummyJSON API
      ↓
GET Request
      ↓
Paginação
      ↓
Tratamento de erros
      ↓
Seleção dos campos
      ↓
Filtro dos produtos
      ↓
Exportação para JSON
```

## ⚙️ Funcionalidades

O pipeline:

1. Consome os produtos da API DummyJSON.
2. Realiza paginação automática utilizando `limit` e `skip`.
3. Utiliza timeout para evitar espera indefinida.
4. Trata erros de conexão, timeout, HTTP e JSON.
5. Seleciona os campos relevantes dos produtos.
6. Filtra produtos com:

   * `price > 100`
   * `stock < 50`
7. Salva os dados processados em arquivos JSON.

## 📊 Resultado

Na execução realizada:

* **Total disponível na API:** 194
* **Total recebido:** 194
* **Produtos após o filtro:** 27

## ▶️ Como executar

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta do projeto:

```bash
cd api-etl-dummyjson
```

Instale a dependência:

```bash
pip install requests
```

Antes de executar o script, verifique os caminhos definidos no código para os arquivos de saída. Por padrão, o projeto utiliza caminhos locais do Windows, que devem ser alterados para uma pasta existente na sua máquina:

```python
"C:/Users/SEU_USUARIO/Documents/project/produtos.json"
"C:/Users/SEU_USUARIO/Documents/project/produtos_filtrados.json"
```

Substitua `SEU_USUARIO` pelo seu usuário do Windows e ajuste o caminho, se necessário. A pasta de destino deve existir antes da execução.

Execute o script:

```bash
python seu_codigo.py
```

Após a execução, os arquivos `produtos.json` e `produtos_filtrados.json` serão gerados na pasta de destino definida no código.

## 📚 Aprendizados

Este projeto foi desenvolvido como prática dos fundamentos de Engenharia de Dados, consolidando o fluxo de extração, transformação e carregamento de dados utilizando Python e uma API REST.
