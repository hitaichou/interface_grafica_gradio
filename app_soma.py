import gradio as gr #gr é um apelido para gradio

#função com dois parâmetros que retorna a soma deles
def somar(num1, num2):
    return num1 + num2

#criação da interface do gradio
#iface é a variável que guarda a interface
iface = gr.Interface(
    fn=somar, #passo a função que será usada
    inputs=["number", "number"], #dois inputs do tipo número
    outputs="number", #output do tipo número
    title="Calculadora de Soma", #título da interface
    description="Insira dois números para obter a soma", #descrição da interface
    theme="default" #tema padrão do gradio
)

iface.launch() #inicia a interface do gradio