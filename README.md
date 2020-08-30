# blog

Blog do Bah Hackers. Python 3.6 e Pelican.

## Desenvolvimento:

Clonar o repositório e entrar na pasta clonada.

Criar ambiente virtual.
```
python3 -m venv venv
```

Ou

```
virtualenv --python=python3.6 venv
```

Ativar o ambiente virtual.

```
source venv/bin/activate
```

Instalar as dependências:

```
pip install -r requirements.txt
```

Gerar os arquivos estáticos:

```
pelican CAMINHO_DA_PASTA_CONTENT
```

Ver no navegador:

```
firefox output/index.html
```


Adicionar imagens no artigo:
- Coloque a imagem dentro de `content/images`
- Use a seguinte sintaxe: `![Alt-text para a imagem]({static}/images/ARQUIVO.EXTENSÃO)`
