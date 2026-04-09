import os
import shutil

caminho = r"C:\Users\SeuUsuario\Downloads" #Coloque o caminho que desejar

def organizar_arquivos(caminho):
    arquivos = os.listdir(caminho)

    # Criar pastas
    pastas = {
        "PDF": ["pdf"],
        "Imagens": ["jpg", "jpeg", "png"],
        "Videos": ["mp4", "mp3", "mov", "avi"],
        "Outros": []
    }

    for pasta in pastas:
        os.makedirs(os.path.join(caminho, pasta), exist_ok=True)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)

        if os.path.isfile(caminho_arquivo) and "." in arquivo:
            extensao = arquivo.split(".")[-1].lower()

            movido = False

            for pasta, extensoes in pastas.items():
                if extensao in extensoes:
                    destino = os.path.join(caminho, pasta)
                    shutil.move(caminho_arquivo, os.path.join(destino, arquivo))
                    movido = True
                    break

            if not movido:
                destino = os.path.join(caminho, "Outros")
                shutil.move(caminho_arquivo, os.path.join(destino, arquivo))

    print("Arquivos organizados com sucesso!")

organizar_arquivos(caminho)