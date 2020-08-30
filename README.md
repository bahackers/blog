# blog

Blog do Bah Hackers. Python 3.6 e Pelican.

## Desenvolvimento:

Clonar o repositório.

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

Entrar na pasta do blog e instalar as dependências:

```
cd blog
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
