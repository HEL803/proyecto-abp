import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("Hello Flet")))
    page.title="cuetionario quizziz"
    page.bgcolor="black"

    
    txtR1=ft.TextField(label="ingresa el indice de tu respuesta")

    lblp1=ft.Text("¿Que es la tecnologia?",color="white")
    lblia=ft.Text("a",color="white"),
    lblib=ft.Text("B",color="white"),
    lblic=ft.Text("c",color="white"),

    txtR2=ft.TextField(label="ingresa el indice de tu respuesta")

    lblp2=ft.Text("¿Que son las STEM?",color="white")
    lblia=ft.Text("a",color="white"),
    lblib=ft.Text("B",color="white"),
    lblic=ft.Text("c",color="white"),

    

    txtR3=ft.TextField(label="ingresa el indice de tu respuesta")

    lblp3=ft.Text("¿Como puedes usar la tecnologia para expresarte?",color="white")
    lblia=ft.Text("a",color="white"),
    lblib=ft.Text("B",color="white"),
    lblic=ft.Text("c",color="white"),

    txtR4=ft.TextField(label="ingresa el indice de tu respuesta")

    lblp4=ft.Text("Cual es la importancia de usar la tecnoligia como medio de expresion?",color="white")
    lblia=ft.Text("a",color="white"),
    lblib=ft.Text("B",color="white"),
    lblic=ft.Text("c",color="white"),

    

    txtR5=ft.TextField(label="ingresa el indice de tu respuesta")

    lblp5=ft.Text("¿Que son las STEM?",color="white")
    lblia=ft.Text("a",color="white"),
    lblib=ft.Text("B",color="white"),
    lblic=ft.Text("c",color="white"),

    

    txtR6=ft.TextField(label="ingresa el indice de tu respuesta")

    lblp6=ft.Text("¿Cual es son las ventajas de usar la tecnologia como medio de expresion?",color="white")
    lblia=ft.Text("a",color="white"),
    lblib=ft.Text("B",color="white"),
    lblic=ft.Text("c",color="white"),

    








    page.add(
        ft.Column(
            controls=[
                ft.Row(controls=[lblp1], alignment="CENTER"),
                ft.Row(controls=[lblia,lblib,lblic],alignment="CENTER"),
                ft.Row(controls=[txtR1],alignmnet="CENTER")
            ],alignment="CENTER"
        )
    )



    


ft.app(main)
