# JSON Tree Viewer

Um visualizador simples de árvore para JSON usando Tkinter em Python.

Este aplicativo permite que você visualize a estrutura de um JSON em formato de árvore.

## Como usar

Cole ou digite o JSON na caixa de texto fornecida.
Clique no botão "Processar JSON".
A estrutura do JSON será exibida como uma árvore na parte inferior da janela.

## Requisitos

Certifique-se de ter o Python instalado em seu sistema. Este aplicativo foi testado em Python 3.x.

## Instalação e execução

Clone este repositório:

```shell
git clone https://github.com/espinhara/JSON-Tree-View.git
```

Navegue até o diretório clonado:

```shell
cd json-tree-viewer
```

Execute o aplicativo:

```shell
python json_tree_viewer.py
```

Como gerar um executável
Você pode gerar um executável usando a biblioteca pyinstaller. Certifique-se de instalá-lo primeiro, se ainda não o fez:

```shell
pip install pyinstaller
```

Em seguida, navegue até o diretório onde está o script json_tree_viewer.py e execute o seguinte comando:

```shell
pyinstaller --onefile main.py
```

Isso criará um executável na pasta dist. Você pode executar o aplicativo diretamente a partir desse executável.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar uma solicitação de recebimento (pull request) para melhorias no código.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE.md).
