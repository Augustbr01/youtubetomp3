# Conversor de YouTube para MP3

Este projeto é um conversor de vídeos do YouTube para MP3 usando Flask e `yt-dlp`. 

## Requisitos

- Python 3.6 ou superior
- `pip` (gerenciador de pacotes do Python)
- FFmpeg instalado

## Configuração do Ambiente

### Clone o Repositório

   `git clone https://github.com/Augustbr01/youtubetomp3`
   `cd youtubetomp3`

### Crie e Ative um Ambiente Virtual (opcional, mas recomendado)

- No Windows:
  `python -m venv youtubetomp3`
  `youtubetomp3\Scripts\activate`

## Instale as Dependências

- Se você estiver usando um ambiente virtual:
  `pip install -r requirements.txt`
- Caso não esteja usando um ambiente virtual, você pode instalar as dependências diretamente:
  `pip install Flask yt-dlp`

## Executando o Projeto

- Execute o Servidor Flask
  `python app.py`
- Acesse a Aplicação
  http://127.0.0.1:5000/

## Como usar

**1. Cole a URL do vídeo do YouTube no campo de entrada.**
**2. Clique no botão "Converter".**
**3. O arquivo MP3 será baixado automaticamente na pasta /downloads.**


## Observações

** - Certifique-se de que o FFmpeg está instalado no seu sistema para a conversão de áudio. [Instruções de instalação do FFmpeg](https://ffmpeg.org/download.html).**
** - Este projeto foi desenvolvido para fins educacionais. Use-o conforme as leis de direitos autorais aplicáveis.**
--------------------------------------------------------

### Explicação dos Seções:

- **Clone o Repositório**: Instruções para clonar o projeto do GitHub (substitua o URL pelo seu).
- **Crie e Ative um Ambiente Virtual**: Instruções para criar e ativar um ambiente virtual.
- **Instale as Dependências**: Instruções para instalar as bibliotecas necessárias.
- **Executando o Projeto**: Como iniciar o servidor Flask.
- **Como Usar**: Passos para usar a aplicação.
- **Observações**: Informações adicionais, como a necessidade do FFmpeg.
- **Licença**: Tipo de licença para o projeto (se aplicável).

