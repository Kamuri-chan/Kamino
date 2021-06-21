# Kamino

# Português
## Outro bot? Qual o proposito?
SIm, esse é outro bot, mas diferente dos outros, este bot tem uma função de preprocessamento de text. Vou explicar mais nas próximas linhas:
- Este bot usa algumas técnicas chamadas de preprocessamento de texto, resumindo, texto puro entra, texto pronto para o processamento sai. Os métidos usados neste trabalho são explicados abaixo.
- Este bot não usa Aprendizado de Máquina, IA ou outros métodos complicados para encontrar e pegar a resposta, apenas preprocessamento de texto e uma métrica baseada em palavra-chave/precisão.
- As palavras chaves, assim como as respostas, estão em um arquivo JSON que pode ser atualizado usando uma API com POST requests, deixando muito mais fácil adicionar novas funções.

## Os métodos
Quando lidamos com texto informal e texto não-padronizado (ou não-estruturado), geralmente é bem mais dificil encontrar algum significado nele. É nesse comento que o prepeocessamento de texto é usado.
Os métodos explorados por este bot são:
- Tokenization:
  - Este processo transforma a mensagem em palavras menores, deixando mais fácil para trabalhar.
- Remoção de stop-words:
  - Esse método remove as palavras não necessárias, que apenas deixam o texto longo.
    - "Stop words são divisões da linguagem natural. O motivo pelo qual stop-words devem ser removidas do texto é que elas apenas fazem o texto parecer mais pesado e menos importante para analistas. Removendo stop words reduz a dimensionalidade no termo de espaço. As palavras mais comus em documentos de texto são artigos, preposições, pronomes, etc. que não dão o significado do documento. Essas palavras são tratadas como stop words. Exemplos de stop words: o, a, em, com, de, que, etc. Stop words também são removidas de documentos porquê essas palavras não consideras palavras-chave em aplicações de mineração de texto"[[1]](#1).
- Eu também criei uma função para remover pontuação, já que, na maior parte do tempo, são desnecessárias para este projeto.
- Stemming e Lemmatization ainda não foram incluidos, mas tenho planos de adicionar alguns algoritmos em breve.
Por enquanto é só.

## O futuro
Eu não tenho certeza sobre o futuro deste projeto, estou fazendo apenas por diversão. Mas se você se interessar, me deixe saber, me envie um email e vamos tomar um café ;D

# English
## Another bot? What's the purpose?
Yes, this is another bot, but unlike the others, this bot has a text preprocessing feature. I'll explain more on the following lines:
- This bot uses some techniques called text preprocessing, TLDR: raw text, like any message, goes in, ready-for-processing text goes out. The explanation of the methods used on this work are bellow.
- This bot don't use ML, AI or any other fancy methods to find and retrieve the response, just uses text preprocessing and a keyword/precision metric.
- The keywords, as well the responses, are in a JSON file that can be updated by using an API with POST requests, making it much easier to add new features.

## The methods
When dealing with informal text and text that is not in standardized (or structured), usually it's a lot hardier to get some meaning out of it. That's when text preprocessing comes in.
The methods explored by this bot are:
- Tokenization:
  - This breakes down the message into several smaller words, making it easier to work with.
- Removing stop-words:
  - This processing removes the uneeded words, that only makes the text longer and full of garbage:
    - "Stop words are a division of natural language. The motive that stop-words should be removed from a text is that they make the text look heavier and less important for analysts. Removing stop words reduces the dimensionality of term space. The most common words in text documents are articles, prepositions, and pro-nouns, etc. that does not give the meaning of the documents. These words are treated as stop words. Example for stop words: the, in, a, an, with, etc. Stop words   are removed from documents because those words are not measured as keywords in text mining applications" [[1]](#1).
- Also, I built a function to remove punctuation, as they are, most of the time, unecessary for the needs of this project.
- Stemming and Lemmatization are not included yet, but I do have some plans to include some algorithms soon.
For now, that's it.

## The future
I don't know for certain the future of this project, I am doing it just for fun. But if you're interested, let me know, email me and let's drink a coffe ;D


## References
<a id="1">[1]</a> 
Dr.S.Vijayarani et al.
International Journal of Computer Science & Communication NetworksVol 5(1), 7-16.
ISSN:2249-5789
(Tradução para português: tradução nossa)
