import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora de gordura corporal"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"

    weight = ft.TextField(width=250, border_radius=20, label='Peso (em kg)')

    chestMeasure = ft.TextField(width=250, border_radius=20, label='Medida do Peitoral (em mm)')
    abdomenMeasure = ft.TextField(width=250, border_radius=20, label='Medida do Abdômen (em mm)')
    thighMeasure = ft.TextField(width=250, border_radius=20, label='Medida da Coxa (em mm)')
    age = ft.TextField(width=100, border_radius=20, label='Idade')
    sex = ft.RadioGroup(content=ft.Row([
        ft.Radio(value='m', label='Homem'),
        ft.Radio(value='w', label='Mulher')
    ]))

    modeIcon = ft.FloatingActionButton()
    modeIcon.icon = ft.icons.LIGHT_MODE

    status = ft.Text('', size=16)
    statusPerc = ft.Text('', size=28)
    statusWeight = ft.Text('', size=16)

    def alternateMode(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            modeIcon.icon = ft.icons.LIGHT_MODE

        elif page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            modeIcon.icon = ft.icons.DARK_MODE

        page.update()

    modeIcon.on_click = alternateMode

    page.floating_action_button = modeIcon

    def calc(e):
        if chestMeasure.value.isdigit() and abdomenMeasure.value.isdigit() and thighMeasure.value.isdigit() and age.value.isdigit() and weight.value.isdigit():
            if sex.value is not None:

                measureSum = int(chestMeasure.value) + int(abdomenMeasure.value) + int(thighMeasure.value)

                if 8 <= measureSum <= 127:
                    yPos = (measureSum - 8) // 3

                if int(age.value) <= 22:
                    xPos = 0

                elif 23 <= int(age.value) <= 27:
                    xPos = 1

                elif 28 <= int(age.value) <= 32:
                    xPos = 2

                elif 33 <= int(age.value) <= 37:
                    xPos = 3

                elif 38 <= int(age.value) <= 42:
                    xPos = 4

                elif 43 <= int(age.value) <= 47:
                    xPos = 5

                elif 48 <= int(age.value) <= 52:
                    xPos = 6

                elif 53 <= int(age.value) <= 57:
                    xPos = 7

                elif int(age.value) > 58:
                    xPos = 8

                if sex.value == 'm':
                    ref = 'measureTable'

                if sex.value == 'w':
                    ref = 'measureTableW'

                f = open(f'assets/{ref}/{yPos}/{xPos}.txt', 'r')
                status.value = f'A porcentagem de gordura corporal é de:'

                percentage = float(f.read())

                statusPerc.value = f'{percentage}%'
                print(percentage)
                print(type(percentage))

                decFat = percentage / 100
                decHealth = 1 - (percentage / 100)

                statusWeight.value = f'{round(decFat * float(weight.value), 2)}kg de gordura e {round(decHealth * float(weight.value), 2)}kg de massa magra'

            else:
                status.value = 'Por favor selecione seu Sexo!'

        else:
            status.value = 'Por favor insira valores Válidos!'

        page.update()

    page.add(

        ft.Row([
            ft.Text('Calculadora de Gordura Corporal', size=20)
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Divider(height=40),

        ft.Row([
            weight
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([
            chestMeasure
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([
            abdomenMeasure
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([
            thighMeasure
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Divider(height=16),

        ft.Row([
            age, sex
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([
            ft.ElevatedButton(text='Calcular', height=50, on_click=calc)
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Divider(height=24),

        ft.Row([
            status
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([
            statusPerc
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([
            statusWeight
        ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Divider(height=40),

    )


ft.app(target=main, assets_dir='assets')
