Title: Try Hack Me - Terça Sem Fim - 01-set-2020
Date: 2020-09-01 18:00
Modified: 2020-09-01 00:42
Category: blog, hacking
Tags: tryhackme, hacking, nmap
Slug: try-hack-me-setup
Authors: Mate Hackers
Summary: README da live Terça Sem Fim de 01/setembro/2020. Entre no nosso Github para contribuir, atualizar ou complementar essas informações, se for necessário.

## 1. Configuração<a name="config"></a>

A configuração da máquina em que os desafios estão sendo realizados, para demonstrar que você não precisa de uma máquina top de linha simplesmente para começar a aprender - se tiver um computador que seja ao menos de arquitetura 64-bits já está de bom tamanho para a maioria das coisas (apesar de alguns processos serem mais demorados se a máquina não for muito potente).  

**Netbook Acer Aspire 1410**  

```
Intel Celeron 1.2 GHz, 800 MHz (64-bits)
2GB memória
240 GB SDD
Sistema operacional: Kali Linux 64-bit (2020.3) https://www.kali.org
```

![Papel de parede do Kali Linux]({static}/images/tryhackme/kali-strips-4x3.png)

### 1.1 Alternativas

Também é possível utilizar:  

- Kali Live (inicializar um computador que possui outro sistema operacional a partir de um pendrive com Kali)  
- Kali em algum dispositivo com arquitetura arm64, como Raspberry Pi  
- Máquinas virtuais com Kali Linux (usando VirtualBox ou derivados)  

### 1.2 Algumas dificuldades que podem ser encontradas utilizando essas alternativas

#### VirtualBox

- Dificuldade de configuração de hardware (usar interfaces do computador host, mapeá-las para a máquina virtual, etc).  

#### Sistema live

- Persistência de configurações ou de informações.  

#### Raspberry Pi

Nem todos os pacotes ou programas disponíveis na versão "full" do Kali foram portados para a imagem do Raspberry Pi e você poderá ter que ficar garimpando na mão algumas coisas.  

Ex.:  

- listas de senhas que vem por padrão no `/usr/share/wordlists/`  
- Burp Suite (não tem distribuição)  
- Gobuster (tem que instalar Go e gerar o binário para poder instalar/usar)  

---

## 2. Try Hack Me (Tente Me Hackear)<a name="try-hack-me"></a>

![Logo Try Hack Me, uma nuvem vermelha chovendo números binários]({static}/images/tryhackme/tryhackme-logo.png)

Try Hack Me é uma plataforma para aprendizado de questões relacionadas à segurança de sistemas e de aplicações. Apesar de ser toda em inglês e não ter localização para português brasileiro, ela é bastante intuitiva e oferece ferramentas para que se comece rapidamente a explorar essas questões de segurança e aprender. Se você tem dificuldades com o idioma, vá utilizando alguma ferramenta de tradução, mas aproveite e vá anotando palavras que você não conhece - para se familiarizar com elas -; o inglês é a língua franca da informática e essa é mais uma oportunidade de ter contato com o idioma, praticar e aprender.  

### 2.1 Configurando<a name="try-hack-me-setup"></a>

- Criar conta em [https://tryhackme.com](https://tryhackme.com)  
- Verificar o e-mail da conta (para ativar as funcionalidades e em caso de precisar recuperar a senha)  
- Baixar o arquivo de configuração OpenVPN (Access Machines / botão "Download My Configuration File")  
- Instalar Openvpn no seu sistema operacional, se ainda não estiver instalado  
- Conectar usando o arquivo de configuração baixado: `sudo openvpn ENDEREÇO_DO_ARQUIVO_DE_CONFIGURAÇÃO`  
- Inicializar um servidor (botão "Deploy" no "room" de boas vindas - Welcome)  
- Aguardar o servidor carregar e fornecer um endereço de IP  
- Abrir o endereço de IP no navegador  
- Copiar a flag que aparece e colar na resposta da tarefa "Access your first machine"  

Se você conseguiu: Parabéns! Agora você consegue implantar uma máquina no Try Hack Me e acessá-la. Nem sempre vai ser somente pelo navegador, algumas vezes pelo terminal ou usando outros programas, mas o processo de conectar o OpenVPN e fazer Deploy é basicamente esse.  

Se não conseguiu: Não desiste! Busca na internet o erro que está dando, compartilha lá no Telegram ou na lista do Mate Hackers onde você travou e quem sabe alguém consiga te ajudar.  

### 2.2 Room Nmap<a name="room-nmap"></a>
![Logo da sala Nmap com a legenda: parte da série Red Primer, introdução ao escaneamento]({static}/images/tryhackme/room-nmap.png)

O primeiro "room" (sala) que vamos explorar (depois do de Boas Vindas) é o room do Nmap, por esta ser uma sala introdutória a uma ferramenta que é importante e útil na investigação de máquinas. Como vamos interagir com uma das máquinas da TryHackMe, é preciso que a conexão via OpenVPN tenha sido estabelecida (ou precisa pagar a assinatura para utilizar uma das máquinas via navegador).  

Para completar os desafios da sala, é sempre necessário entrar nela, clicando em "Join Room". Após, enquanto usar a conta gratuita sempre haverá o aviso que precisa assinar para assistir os vídeos, mas de modo geral não é necessário pagar para realizar as atividades (existem algumas salas que são fechadas só para assinantes, nenhumas das quais estaremos completando aqui).  

#### Tarefa 1: Deploy

Na primeira tarefa, só é necessário inicializar a máquina (clicando no botão "Deploy") e confirmar no botão verde ("Question Done"). Aguarde até o endereço IP da máquina aparecer.  

#### Tarefa 2: Nmap Quiz (Leia o manual)

A segunda tarefa busca ajudar você a se familiarizar com alguns parâmetros muito utilizados com o Nmap. Todas as respostas para as questões estão no manual da ferramenta (no Linux, você pode acessar através do comando `man NOME_DA_FERRAMENTA`, no caso: `man nmap`). Nessas questões estão a resposta para alguns comandos que serão utilizados na tarefa seguinte.  

#### Tarefa 3: Nmap Scanning (Nmap na prática, usando para escanear uma máquina)

Através dessa tarefa, você vai executar alguns escaneamentos básicos e aprender a interpretar os resultados. Como temos alguns processos que são mais demoradas para serem realizadas (por exemplo, escanamento agressivo), pode ser interessante utilizar o parâmetro "verboso" para ter certeza que o programa está avançando e o computador não travou, rede não caiu, etc.  

Entre as questões do desafio, a mais complicada é certamente a última, em que é necessário executar todos os scripts da categoria de vulnerabilidades (`vuln`) para obter a resposta. Entretanto, se você tiver dificuldade com as outras questões, persista! Procure informações no manual. Peça ajuda! Visite o [site do Mate Hackers](https://matehackers.org) e encontre formas de contatar o grupo.  

![Captura de tela do Try Hack Me mostrando todas tarefas em verde, completas]({static}/images/tryhackme/tryhackme-sala-nmap-completa.png)
