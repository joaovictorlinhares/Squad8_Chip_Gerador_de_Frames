from datetime import datetime
from time import sleep
import cv2
import os

cam = cv2.VideoCapture(os.getenv("LINK_CAMERA"))

cam.set(cv2.CAP_PROP_FRAME_WIDTH, int(os.getenv("LARGURA_IMAGEM")))
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, int(os.getenv("ALTURA_IMAGEM")))


def extrair_frame():

    while cam.isOpened():
        ret, frame = cam.read()

        if not ret:
            break

        salvar_frame(frame)

    cam.release()


def salvar_frame(frame):
    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S%f")
    cv2.imwrite(os.path.join("volumeFrame", f"{data_hora}.jpg"), frame)
    sleep(INTERVALO)


def gerar_intervalo(fotos_segundo=1):
    if 1 <= fotos_segundo <= 30:
        return round(1 / fotos_segundo, 6) - 0.025
    else:
        print("A quantidade de fotos por segundo deve estar entre 1 e 30")
        exit()


INTERVALO = gerar_intervalo(int(os.getenv("FOTOS_SEGUNDO")))
extrair_frame()
