import tkinter

tela = tkinter.Tk()
tela.title("CALCULADORA IMC")

def calcular_imc():
    kg = float(kg_input.get())
    altura = float(altura_input.get())
    imc = round((kg / (altura ** 2)), 2)
    if imc < 18.5:
        imc_text = 'baixo'
    elif imc <= 24.9:
        imc_text = 'normal'
    elif imc <= 29.9:
        imc_text = 'sobrepeso'
    elif imc <= 34.9:
        imc_text = 'Obesidade'
    elif imc <= 39.9:
        imc_text = 'Obesidade Severa'
    elif imc >= 40.0:
        imc_text = 'Obedidade Mórbida'
    resultado['text'] = f'IMC: {imc}, {imc_text}'

kg_texto = tkinter.Label(tela, text='KG: ')
kg_texto.grid(column=0, row=0)

kg_input = tkinter.Entry(tela)
kg_input.grid(column=1, row=0)

altura_texto = tkinter.Label(tela, text='Altura: ')
altura_texto.grid(column=0, row=1)

altura_input = tkinter.Entry(tela)
altura_input.grid(column=1, row=1)

cal_button = tkinter.Button(tela, text='Calcular', command=calcular_imc)
cal_button.grid(column=0, row=2)

resultado = tkinter.Label(tela, text='IMC: ')
resultado.grid(column=1, row=2)

tela.mainloop()