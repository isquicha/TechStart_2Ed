# Trabalho no olist
Olist é uma empresa que oferece uma plataforma de integração para vendedores e marketplaces, permitindo-lhes vender seus produtos em vários canais.

A equipe de desenvolvimento Olist consiste em desenvolvedores que amam o que fazem. Nossos processos de desenvolvimento ágil e nossa busca pelas melhores práticas de desenvolvimento proporcionam um ótimo ambiente para profissionais que gostam de criar softwares de qualidade em boa companhia.

Estamos sempre à procura de bons programadores que adorem melhorar seu trabalho. 

Este repositório contém um problema usado para avaliar as habilidades do candidato. É importante notar que resolver satisfatoriamente o problema é apenas uma parte do que será avaliado. Também consideramos outras disciplinas de programação como documentação, teste, cronograma de commit, design e melhores práticas de codificação.


# Dicas:
* Leia atentamente a especificação para entender todos os requisitos do problema e do artefato antes de começar, se você não entender algo, diga-nos;
* Verifique as recomendações e o material de referência no final desta especificação;
* Apreciamos a simplicidade, portanto, crie uma boa configuração de projeto que nos ajudará na sua avaliação;

# Como participar
* Faça um fork deste repositório no Github. Se você não pode criar um fork público deste projeto, faça um repositório privado e adicione permissão de leitura para o usuário abaixo:
  + mgranemann
* Siga as instruções do README.md (este arquivo);
* Candidate-se ao cargo na nossa página de carreiras com o link para o fork no Github.
  + caso ja tenha realizado a candidatura na pagina de carreiras sem o envio do desafio, responda ao e-mail que lhe foi enviado pela equipe do seleção com o link do seu repositório.



# Especificação
Você deve implementar um aplicativo para armazenar dados de vendedores, produtos ,marketplaces e categorias.

1. CRUD (criar, ler, atualizar e excluir) de vendedores:
2. CRUD (criar, ler, atualizar e excluir) de produtos:
3. CRUD (criar, ler, atualizar e excluir) de marketplaces:
4. CRUD (criar, ler, atualizar e excluir) de categorias:

Ao final o sistema deve permitir as ações a seguir:
* Cadastrar vendedores, produtos, marketplaces e categorias
* Ler os dados de vendedores, produtos, marketplaces e categorias
* Atualizar os dados de vendedores, produtos, marketplaces e categorias
* Excluir os dados de vendedores, produtos, marketplaces e categorias

Cada registro de vendedor deve conter as seguintes informações:
* id (autogerado)
* nome fantasia
* razão social
* cnpj
* email de contato
* telefone de contato
* endereco completo

Cada registro de produto deve conter as seguintes informações:
* id (autogerado)
* nome
* descrição
* valor
* categorias (um produto pode estar em mais de uma categoria)

Cada registro de categoria deve conter as seguintes informações:
* id (autogerado)
* nome
* descrição

Cada registro de marketplace deve conter as seguintes informações:
* id (autogerado)
* nome
* descrição
* site
* telefone de contato
* email de contato
* contato responsável técnico

Para recuperar um produto, podemos filtrar por 4 campos (ou uma composição desses quatro):
* nome
* descrição
* valor
* categorias
Deve ser possível navegar pelos dados de todos os produtos sem nenhum filtro.


# Requisitos do projeto:
1. Pode ser feita em qualquer linguagem de programação que suporte o paradigma de orientação a objetos
2. Utilizar padrões de projeto
3. Boas práticas de desenvolvimento de software
4. Utilizar paradigma de orientação a objetos
5. Utilizar GitHub
6. Camada visual pode ser console, desktop ou web
7. Variáveis, código e strings devem estar todos em inglês.
8. Escreva a documentação do projeto contendo:

>  * Descrição;
>  * Instruções de instalação (configuração);
>  * Breve descrição do ambiente de trabalho utilizado para executar este projeto (Computador / sistema operacional, editor de texto / IDE, bibliotecas, etc).
  
# Recomendações
  * Use boas práticas de programação;
  * Use as melhores práticas do git, com mensagens claras;
  * Esteja ciente ao modelar o banco de dados;

# Divirta-se!
