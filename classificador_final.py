from pathlib import Path

import pandas as pd

regras = {
        "rede": ["internet", "wifi", "rede", "roteador","site", "ping", "conexão", "servidor", "dns", "ip", "velocidade", "vpn" ],
        "software": ["excel", "fecha", "programa", "windows", "vírus", "e-mail", "erro", "instalação", "atualização", "driver", "antivírus", "firewall", "navegador", "aplicativo", "sistema operacional", "configuração", "backup", "restauração", "licença", "registro", "script", "plugin", "extensão", "word", "powerpoint", "outlook", "office", "linux", "mac", "android", "ios", "chrome", "firefox", "edge", "opera", "safari", "tela azul", "lento"],
        "hardware": ["tela", "teclado", "mouse", "ruído", "barulho", "placa", "memória", "processador", "hd", "ssd", "placa de vídeo", "bateria", "carregador", "fonte", "ventoinha", "cooler", "placa-mãe", "ventilador", "impresora", "impressora", "usb", "hdmi", "vga", "display", "monitor", "placa de som", "placa de rede", "placa de captura", "placa de vídeo dedicada", "placa de vídeo integrada", "quente", "reinicia", "liga", "imprimir"],
 
    }


def classificar(texto):
    texto = texto.lower()
    for categoria, palavras in regras.items():
        for palavra in palavras:
            if palavra in texto:
                return categoria
    return "outro"


def avaliar(nome, arquivo):
    df = pd.read_csv(arquivo)
    df["categoria_regras"] = df["ticket"].apply(classificar)
    df["acertou"] = df["categoria_regras"] == df["categoria_correta"]

    print(f"\n=== {nome} ({len(df)} chamados) ===")
    print(f"Acerto das regras: {df['acertou'].mean():.0%}")

    print("\nAcerto por categoria:")
    print(df.groupby("categoria_correta")["acertou"].mean())

    erros = df[~df["acertou"]]
    print(f"\nErros ({len(erros)}):")
    if erros.empty:
        print("Nenhum erro.")
    else:
        print(erros[["ticket", "categoria_correta", "categoria_regras"]].to_string())


pasta = Path(__file__).parent

avaliar("Desenvolvimento", pasta / "tickets.csv")
avaliar("Teste", pasta / "tickets_teste.csv")
