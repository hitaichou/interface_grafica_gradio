import gradio as gr
import math

def fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos"
    return math.factorial(num) #uso a função factorial do módulo math

# print(fatorial(5))
iface = gr.Interface(
    fn=fatorial, #chamo a função do fatorial para criar a interface
    inputs="number",
    outputs="text", #o retorno é em texto para lidar com mensagens de erro
    title="Calculadora de Fatorial",
    description="Insira um número para obter o fatorial"
)

iface.launch()