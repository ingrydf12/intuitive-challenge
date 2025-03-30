![logoIntuitive](https://github.com/ingrydf12/intuitive-challenge/blob/master/TesteApi4/front/src/assets/logoIntuitiveWhite.png?raw=true)

# Challenge: IntuitiveCare

Este repositório contém testes relacionados ao processo seletivo do Intuitive Care.

### Objetivos
- Conhecimentos fundamentais de programação.
- Organização e estruturação do código.
- Competências adicionais em boas práticas de programação.

## Tecnologias

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=vuejs,python,fastapi,postman" />
  </a>
</p>

## Estrutura
- `WebScraping` → referente ao Web Scraping e compactação dos anexos
- `TransformData` → referente a extração e transformação de dados em CSV
- `BancoSQL` → referente ao teste de banco de dados
- `TesteApi4` → referente a aplicação em Vue.js e Python com funcionalidade de busca textual

## Descrição dos testes

### Web Scraping
**Objetivo:** Acessar o site da ANS, fazer downloads dos anexos presentes na página em PDF e compactar todos os anexos em um único arquivo (.zip)

**O que ele faz?**
- Cria a pasta de downloads, se esta ainda não existir.
- Verifica a extensão de arquivo .pdf e se começa com 'Anexo'
- Faz download do arquivo e retorna a quantidade de arquivos baixados
- Compacta os arquivos da pasta downloads com ZipFile

#### Estrutura

```
    ├── WebScraping
        └── downloads -> pasta com os anexos baixados
    Anexos.zip -> arquivo de output do processo
    config.py -> dicionário de configuração para o script principal, ex: nome da pasta de output
    main.py -> aplicação principal, contendo a classe de compactPDFFiles
```

### TransformData
**Objetivo:** Extração de dados da tabela presente dentro do Anexo I baixado no teste anterior, salvando em um arquivo csv, que posteriormente é compactado em um arquivo .zip com o nome __"Teste_Ingryd_Cordeiro_Duarte"__

**O que ele faz?**
- Verifica a existência da pasta e o caminho do arquivo Anexo I com sua extensão .pdf
- Verifica a quantidade de páginas e extrai as tabelas por linhas
- Traz a quantidade de tabelas e registros extraídos
- Salva os dados recebidos, zipando como "Teste_Ingryd_Cordeiro_Duarte".zip na pasta transformedData


### BancoSQL
**Objetivo:** Criação de queries de criação de tabelas com base no arquivo csv. e de importação do conteúdo dos arquivos preparados com encoding correto, além de query analítica para responder:
- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

#### Estrutura
```
    ├── BancoSQL
        └── data -> pasta com arquivos de preparação .csv
    consulta.sql -> arquivo com as querys analíticas
    create_tables.sql -> criação das tabelas
    import_data.sql -> importação dos arquivos com encoding para o banco PostgreSQL
```


### TesteAPI4
**Objetivo:** Desenvolvimento de uma interface web usando Vue.js que interage com um servidor em Python para realizar uma busca textual na lista de cadastros de operadoras feito anteriormente.

## O que ele faz?
- No backend, ele carrega o arquivo .csv presente na pasta data, usando Panda `pd.read_csv()`
- A rota da API de pesquisa é definida como `api/search` passando uma string como parâmetro
- A busca é feita com case-insensitive, comparando o input com os campos Razao_Social e Nome_Fantasia, limitando o resultado até 10 registros.

- No frontend, ao usuário fazer uma pesquisar, ele faz requisição HTTP assíncrona a API com Axios.
- Os resultados são exibidos de forma dinâmica com `-v` e o layout é responsivo para mobile.


#### Estrutura
```
    ├── TesteAPI4
        └── api -> pasta do servidor backend
            └── data -> contém os dados necessários, como o arquivo .csv
            main.py -> serviço do backend com FastAPI, Panda e CORS
            requirements.txt -> arquivo com dependências para instalação
        └── front -> aplicação vue.js
            └── assets -> imagens e ícones
            └── components -> componentes em vue
            └── services -> serviço do front em conexão com API
            └── styles -> arquivos de estilização em css
            └── views -> página / área, ex: área de pesquisa
        App.vue
        main.js
```

## Deploy

Veja a aplicação e interaja por meio deste [link](https://intuitive-challenge.vercel.app/)

**Front**: https://intuitive-challenge.vercel.app/

**API**: https://intituivechallenge.onrender.com


## Como rodar localmente

- Clone esse repositório com comando `git clone https://github.com/ingrydf12/intuitive-challenge`
- Abra uma IDE de sua preferência como Visual Studio Code

### Backend
- Ao abrir a pasta de `api` contendo o backend, rode o comando para instalar as dependências necessárias:

```
    $ pip install -r requirements.txt
```

- Rode o backend / api com o comando `uvicorn main:app --reload` 


### Frontend
- Ao abrir a pasta de `front`, rode o comando para instalar as dependências necessárias:

```
    npm install
```

- Rode o frontend com o comando:
`npm run dev` 
