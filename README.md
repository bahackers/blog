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

---

## Produção

Pra quem não tem pipenv:

```sh
python3 -m pip install --user --upgrade pipenv
```

Rodar pipenv localmente pra garantir que o ambiente virtual seja criado:

```sh
pipenv install
```

Scripts do pipenv para publicar o site em 
<https://denise.matehackers.org/bahackers/> (requer rodar com o usuário 
**www-data**):  

```sh
pipenv run denise
```

Github Pages:

```sh
pipenv run gh
```

### Automatizando

Assumindo blog clonado em **/var/www/pelican**

```sh
www-data@denise~: git clone -b source https://github.com/bahackers/blog.git ~/pelican
```

Cronjob para sincronizar publicações de hora em hora:

```cron
@hourly pushd ~/pelican && rsync -avvhSP /home/bahackers/blog/ ./ && ~/.local/bin/pipenv run denise
```

