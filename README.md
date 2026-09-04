
# 🐾 Pokédex

Projeto de uma **Pokédex Web** desenvolvida com **Django**, integrada à **PokéAPI**, com o objetivo de consumir e apresentar informações dos Pokémon de forma dinâmica e organizada.

O projeto está sendo desenvolvido de forma incremental, utilizando boas práticas de organização de templates, componentes reutilizáveis, arquivos estáticos e separação das funcionalidades.

---

## 🚀 Tecnologias utilizadas

* 🐍 Python
* 🌐 Django
* 🎨 HTML5
* 🎨 CSS3
* ⚡ JavaScript
* 🅱️ Bootstrap
* 🔌 PokéAPI
* 🗂️ Git
* 🐙 GitHub

---

## 📌 Funcionalidades atuais

### 🏠 Página Inicial

* Página de boas-vindas ao projeto.
* Apresentação visual da Pokédex.
* Imagens dos Pokémon.
* Cards estilizados.
* Efeito `hover` nos cards.
* Integração com Bootstrap.
* Estilização própria com CSS.

### 🐾 Página de Pokémon

* Consumo da PokéAPI.
* Carregamento dinâmico dos Pokémon.
* Exibição de **20 Pokémon**.
* Organização dos Pokémon em cards.
* Informações recebidas diretamente da API.

### ℹ️ Página Sobre

* Página dedicada à apresentação do projeto.
* Navegação integrada com as demais páginas.

---

## 🔌 Integração com a PokéAPI

O projeto utiliza a **PokéAPI** para obter os dados dos Pokémon.

Atualmente, a aplicação realiza o consumo da API e apresenta **20 Pokémon dinamicamente** na interface.

Essa integração será ampliada conforme novas funcionalidades forem implementadas.

---

## 🧩 Estrutura de Templates

O projeto utiliza uma estrutura organizada de templates para facilitar a manutenção e expansão da aplicação.

```text
templates/
├── base.html
├── index.html
└── include/
    ├── header.html
    ├── footer.html
    └── cards.html
```

Também existe uma organização específica para as páginas relacionadas à Pokédex.

A utilização de templates reutilizáveis permite compartilhar estruturas como:

* Header
* Footer
* Cards
* Estrutura base das páginas

---

## 🎨 Arquivos Estáticos

Os arquivos estáticos estão organizados separadamente para facilitar a manutenção:

```text
static/
├── css/
├── js/
└── img/
```

Os estilos das páginas também estão sendo organizados de forma independente conforme o projeto cresce.

---

## 🔗 Navegação

O projeto possui rotas configuradas para as páginas principais da aplicação, permitindo a navegação entre:

* 🏠 Home
* 🐾 Pokémon
* ℹ️ Sobre

---

## 🌿 Desenvolvimento

O projeto está sendo desenvolvido de forma incremental.

Novas funcionalidades serão adicionadas conforme a Pokédex evolui, incluindo melhorias na interface, novos dados provenientes da API e novos recursos de interação.

---

## 📋 Próximas funcionalidades

> Esta seção será atualizada conforme novas funcionalidades forem implementadas.

* [ ] Melhorar a apresentação dos dados dos Pokémon
* [ ] Adicionar página de detalhes do Pokémon
* [ ] Adicionar busca por Pokémon
* [ ] Adicionar filtros
* [ ] Adicionar paginação
* [ ] Exibir mais informações fornecidas pela API
* [ ] Criar modal com detalhes do Pokémon
* [ ] Melhorar responsividade
* [ ] Adicionar novas interações com JavaScript
* [ ] Evoluir o design da Pokédex

---

## 📂 Organização do projeto

A estrutura será ampliada conforme novas funcionalidades forem desenvolvidas.

```text
pokedex_01/
│
├── pokedex/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── pokemon/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Status do projeto

🟢 **Em desenvolvimento**

A aplicação já possui integração funcional com a PokéAPI e apresenta Pokémon dinamicamente no navegador.

O projeto continuará sendo desenvolvido e receberá novas funcionalidades ao longo do processo.

---

## 👨‍💻 Desenvolvimento

Projeto desenvolvido como parte do processo de aprendizado e prática de desenvolvimento **Full Stack com Python e Django**, com foco em consumo de APIs, organização de projetos, desenvolvimento de interfaces e boas práticas de programação.
