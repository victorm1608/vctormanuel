import flet as ft


def calc_suma(txtnum1,txtnum2,txtresultado):
    try:
        num1 = float(txtnum1.value.strip())
        num2 = float(txtnum2.value.strip())
        resultado=num1+num2
        txtresultado.value = f"resultado: {resultado}"
    except ValueError
        txtresultado.value = "Error ingresa valores
correctos"

def calc_suma(txtnum1,txtnum2,txtresultado):
    try:
        num1 = float(txtnum1.value.strip())
        num2 = float(txtnum2.value.strip())
        resultado=num1+num2
        txtresultado.value = f"resultado: {resultado}"
    except ValueError
        txtresultado.value = "Error ingresa valores
correcto"

def calc_suma(txtnum1,txtnum2,txtresultado):
    try:
        num1 = float(txtnum1.value.strip())
        num2 = float(txtnum2.value.strip())
        resultado=num1+num2
        txtresultado.value = f"resultado: {resultado}"
    except ValueError
        txtresultado.value = "Error ingresa valores
correcto"

def calc_suma(txtnum1,txtnum2,txtresultado):
    try:
        num1 = float(txtnum1.value.strip())
        num2 = float(txtnum2.value.strip())
        resultado=num1+num2
        txtresultado.value = f"resultado: {resultado}"
    except ValueError
        txtresultado.value = "Error ingresa valores
correcto"

def on_calc_sum(e):
    calc_suma(txtnum1,txtnum2, lblresultado)
    page.update()
    
def on_calc_resta(e):
    calc_resta(txtnum1,txtnum2, lblresultado)
    page.update()
    
def on_calc_mult(e):
    calc_mult(txtnum1,txtnum2, lblresultado)
    page.update()
    
def on_calc_div(e):
    calc_div(txtnum1,txtnum2, lblresultado)
    page.update()
    
def limpiar(e):
    txtnum1.value = ""
    txtnum2.value = ""
    lblresultado.value = "resultado: "
    page.update()
    
btnsuma=ft.ElevatedButton(text="+",on_click=on_calcsuma)

ft.app(main)
