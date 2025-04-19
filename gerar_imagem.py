import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def gerar_imagem_promocional(imagem_url, titulo, chamada, caminho_saida):
    try:
        res = requests.get(imagem_url)
        img = Image.open(BytesIO(res.content)).convert("RGB")
        img = img.resize((1000, 1000))

        nova_img = Image.new("RGB", (1000, 1200), "white")
        nova_img.paste(img, (0, 0))

        draw = ImageDraw.Draw(nova_img)
        try:
            fonte_titulo = ImageFont.truetype("arial.ttf", 32)
            fonte_chamada = ImageFont.truetype("arial.ttf", 28)
        except:
            fonte_titulo = ImageFont.load_default()
            fonte_chamada = ImageFont.load_default()

        draw.text((20, 1020), titulo[:60], font=fonte_titulo, fill="black")
        draw.text((20, 1080), chamada[:60], font=fonte_chamada, fill="red")

        nova_img.save(caminho_saida)

    except Exception as e:
        print("Erro ao gerar imagem:", e)
