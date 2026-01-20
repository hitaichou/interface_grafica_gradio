import gradio as gr

#função que reverte o texto e conta os caracteres
def reverter_texto(texto):
    texto_revertido = texto[::-1] #reverte o texto usando slicing
    return texto_revertido, len(texto_revertido) #retorna o texto revertido e o número de caracteres

# print(reverter_texto("Olá mundo"))
iface = gr.Interface(
    fn=reverter_texto, #chamo a interface do gradio
    inputs="text", #somente tem um input do tipo texto
    outputs=["text", "number"], #dois outputs: um texto e um número
    title="Reversor de Texto",
    description="Insira um texto para revertê-lo e contar os caracteres"
)

iface.launch()