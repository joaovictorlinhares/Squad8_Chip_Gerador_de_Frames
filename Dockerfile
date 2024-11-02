# Escolha a imagem base
FROM python:3.13

# Instale o OpenCV
RUN pip install opencv-python-headless



# Define variáveis de ambiente para geração de frames

    # LINK_CAMERA: URL para acessar a câmera
    # - Protocolos suportados: 
    # --- HTTP
    # --- RTSP
    ENV LINK_CAMERA=http://host.docker.internal:8080

    # LARGURA_IMAGEM: largura da imagem em pixels
    ENV LARGURA_IMAGEM=1280

    # ALTURA_IMAGEM: altura da imagem em pixels
    ENV ALTURA_IMAGEM=720

    # FOTOS_SEGUNDO: quantidade de fotos que devem ser salvas em 1 segundo
    # Valor mínimo: 1
    # Valor máximo: 30
    ENV FOTOS_SEGUNDO=5



# Diretório para salvar os frames
RUN mkdir -p /app/volumeFrame

# Copie o código para o container
COPY /app /app

# Defina o diretório de trabalho
WORKDIR /app

# Execute o código ao iniciar o container
CMD ["python", "geracaoFrame_v2.py"]
