import os
from flask import Flask, request, render_template, send_file, redirect, url_for
import yt_dlp

app = Flask(__name__)

# Pasta onde os arquivos convertidos serão salvos
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format_type = request.form['format']
    ydl_opts = {}

    if format_type == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',  # Qualidade máxima para MP3
            }],
        }
    else:
        return redirect(url_for('index'))  # Redireciona de volta para a página principal em caso de formato inválido

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info_dict).rsplit('.', 1)[0] + '.mp3'
            file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

            # Verificar se o arquivo foi realmente criado
            if not os.path.exists(file_path):
                raise FileNotFoundError("Arquivo não encontrado.")

            return send_file(file_path, as_attachment=True)
    except Exception as e:
        print(f"Erro: {e}")  # Log do erro para depuração
        return redirect(url_for('index'))  # Redireciona para a página principal em caso de erro

if __name__ == '__main__':
    app.run(debug=True)
