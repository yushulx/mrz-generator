import flet as ft
import sys

from mrz.generator.td1 import TD1CodeGenerator
from mrz.generator.td2 import TD2CodeGenerator
from mrz.generator.td3 import TD3CodeGenerator
from mrz.generator.mrva import MRVACodeGenerator
from mrz.generator.mrvb import MRVBCodeGenerator


def main(page: ft.Page):

    document_type = ft.Text('Document type')
    country_code = ft.Text('Country')
    document_number = ft.Text('Document number')
    birth_date = ft.Text('Birth date')
    sex = ft.Text('sex')
    expiry_date = ft.Text('Expiry date')
    nationality = ft.Text('Nationality')
    surname = ft.Text('Surname')
    given_names = ft.Text('Given names')
    optional_data1 = ft.Text('Optional data 1')
    optional_data2 = ft.Text('Optional data 2')

    document_type_txt = ft.TextField(
        value='P', text_align=ft.TextAlign.LEFT, width=200, height=50)

    country_code_txt = ft.TextField(
        value='UTO', text_align=ft.TextAlign.LEFT, width=200, height=50)

    document_number_txt = ft.TextField(
        value='L898902C3', text_align=ft.TextAlign.LEFT, width=200, height=50)

    birth_date_txt = ft.TextField(
        value='740812', text_align=ft.TextAlign.LEFT, width=200, height=50)

    sex_txt = ft.TextField(
        value='F', text_align=ft.TextAlign.LEFT, width=200, height=50)

    expiry_date_txt = ft.TextField(
        value='120415', text_align=ft.TextAlign.LEFT, width=200, height=50)

    nationality_txt = ft.TextField(
        value='UTO', text_align=ft.TextAlign.LEFT, width=200, height=50)

    surname_txt = ft.TextField(
        value='Eriksson', text_align=ft.TextAlign.LEFT, width=200, height=50)

    given_names_txt = ft.TextField(
        value='Anna María', text_align=ft.TextAlign.LEFT, width=200, height=50)

    optional_data1_txt = ft.TextField(
        value='ZE184226B', text_align=ft.TextAlign.LEFT, width=200, height=50)

    optional_data2_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    container_loaded = ft.ResponsiveRow([
        ft.Column(col=2, controls=[document_type, document_type_txt,
                                   country_code, country_code_txt,
                                   document_number, document_number_txt,]),
        ft.Column(col=2, controls=[birth_date, birth_date_txt,
                                   sex, sex_txt,
                                   expiry_date, expiry_date_txt,]),
        ft.Column(col=2, controls=[nationality, nationality_txt,
                                   surname, surname_txt,
                                   given_names, given_names_txt,]),
        ft.Column(col=2, controls=[optional_data1, optional_data1_txt,
                                   optional_data2, optional_data2_txt])
    ])

    def dropdown_changed(e):
        if dropdown.value == 'ID Card(TD1)':
            document_type_txt.value = 'I'
            country_code_txt.value = 'ESP'
            document_number_txt.value = 'BAA000589'
            birth_date_txt.value = '800101'
            sex_txt.value = 'F'
            expiry_date_txt.value = '250101'
            nationality_txt.value = 'ESP'
            surname_txt.value = 'ESPAÑOLA ESPAÑOLA'
            given_names_txt.value = 'CARMEN'
            optional_data1_txt.value = '99999999R'
            optional_data2_txt.value = ''
        elif dropdown.value == 'ID Card(TD2)':
            document_type_txt.value = 'I'
            country_code_txt.value = 'Utopia'
            surname_txt.value = 'ERIKSSON'
            given_names_txt.value = 'ANNA MARIA'
            document_number_txt.value = 'D23145890'
            nationality_txt.value = 'UTO'
            birth_date_txt.value = '740812'
            sex_txt.value = 'F'
            expiry_date_txt.value = '120415'
            optional_data1_txt.value = ''
            optional_data2_txt.value = ''
        elif dropdown.value == 'Passport(TD3)':
            document_type_txt.value = 'P'
            country_code_txt.value = 'UTO'
            document_number_txt.value = 'L898902C3'
            birth_date_txt.value = '740812'
            sex_txt.value = 'F'
            expiry_date_txt.value = '120415'
            nationality_txt.value = 'UTO'
            surname_txt.value = 'Eriksson'
            given_names_txt.value = 'Anna María'
            optional_data1_txt.value = 'ZE184226B'
            optional_data2_txt.value = ''

        elif dropdown.value == 'Visa(A)':
            document_type_txt.value = 'V'
            country_code_txt.value = 'USA'
            surname_txt.value = 'TRAVELER'
            given_names_txt.value = 'HAPPY'
            document_number_txt.value = '123456789'
            nationality_txt.value = 'CAN'
            birth_date_txt.value = '661212'
            sex_txt.value = 'M'
            expiry_date_txt.value = '140728'
            optional_data1_txt.value = 'B3XLC000FD142955'
            optional_data2_txt.value = ''

        elif dropdown.value == 'Visa(B)':
            document_type_txt.value = 'V'
            country_code_txt.value = 'GBR'
            surname_txt.value = 'MUNIR'
            given_names_txt.value = 'FAISAL'
            document_number_txt.value = 'AD0725981'
            nationality_txt.value = 'PAK'
            birth_date_txt.value = '760815'
            sex_txt.value = 'M'
            expiry_date_txt.value = '061116'
            optional_data1_txt.value = ''
            optional_data2_txt.value = ''

        page.update()

    def is_empty(filed_name, filed_text):
        if filed_text.value == None or filed_text.value == '':
            page.snack_bar = ft.SnackBar(
                content=ft.Text(filed_name.value + " is empty!"),
                action="OK",
            )
            page.snack_bar.open = True
            page.update()
            return True
        return False

    def generate_random(e):
        page.update()

    def generate_mrz(e):

        if dropdown.value == 'ID Card(TD1)':

            if is_empty(country_code, country_code_txt):
                return
            if is_empty(document_number, document_number_txt):
                return
            if is_empty(birth_date, birth_date_txt):
                return
            if is_empty(sex, sex_txt):
                return
            if is_empty(expiry_date, expiry_date_txt):
                return
            if is_empty(nationality, nationality_txt):
                return
            if is_empty(surname, surname_txt):
                return
            if is_empty(given_names, given_names_txt):
                return

            try:
                mrz_field.value = TD1CodeGenerator(
                    document_type_txt.value, country_code_txt.value, document_number_txt.value, birth_date_txt.value, sex_txt.value, expiry_date_txt.value, nationality_txt.value, surname_txt.value, given_names_txt.value, optional_data1_txt.value, optional_data2_txt.value)
            except Exception as e:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(str(e)),
                    action="OK",
                )
                page.snack_bar.open = True

        elif dropdown.value == 'ID Card(TD2)':

            if is_empty(country_code, country_code_txt):
                return
            if is_empty(surname, surname_txt):
                return
            if is_empty(given_names, given_names_txt):
                return
            if is_empty(document_number, document_number_txt):
                return
            if is_empty(nationality, nationality_txt):
                return
            if is_empty(birth_date, birth_date_txt):
                return
            if is_empty(sex, sex_txt):
                return
            if is_empty(expiry_date, expiry_date_txt):
                return

            try:
                mrz_field.value = TD2CodeGenerator(
                    document_type_txt.value, country_code_txt.value, surname_txt.value, given_names_txt.value, document_number_txt.value, nationality_txt.value, birth_date_txt.value, sex_txt.value, expiry_date_txt.value, optional_data1_txt.value)
            except Exception as e:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(str(e)),
                    action="OK",
                )
                page.snack_bar.open = True

        elif dropdown.value == 'Passport(TD3)':

            if is_empty(country_code, country_code_txt):
                return
            if is_empty(surname, surname_txt):
                return
            if is_empty(given_names, given_names_txt):
                return
            if is_empty(document_number, document_number_txt):
                return
            if is_empty(nationality, nationality_txt):
                return
            if is_empty(birth_date, birth_date_txt):
                return
            if is_empty(sex, sex_txt):
                return
            if is_empty(expiry_date, expiry_date_txt):
                return

            try:
                mrz_field.value = TD3CodeGenerator(
                    document_type_txt.value, country_code_txt.value, surname_txt.value, given_names_txt.value, document_number_txt.value, nationality_txt.value, birth_date_txt.value, sex_txt.value, expiry_date_txt.value, optional_data1_txt.value)
            except Exception as e:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(str(e)),
                    action="OK",
                )
                page.snack_bar.open = True
        elif dropdown.value == 'Visa(A)':

            if is_empty(country_code, country_code_txt):
                return
            if is_empty(surname, surname_txt):
                return
            if is_empty(given_names, given_names_txt):
                return
            if is_empty(document_number, document_number_txt):
                return
            if is_empty(nationality, nationality_txt):
                return
            if is_empty(birth_date, birth_date_txt):
                return
            if is_empty(sex, sex_txt):
                return
            if is_empty(expiry_date, expiry_date_txt):
                return

            try:
                mrz_field.value = MRVACodeGenerator(
                    document_type_txt.value, country_code_txt.value, surname_txt.value, given_names_txt.value, document_number_txt.value, nationality_txt.value, birth_date_txt.value, sex_txt.value, expiry_date_txt.value, optional_data1_txt.value)
            except Exception as e:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(str(e)),
                    action="OK",
                )
                page.snack_bar.open = True

        elif dropdown.value == 'Visa(B)':

            if is_empty(country_code, country_code_txt):
                return
            if is_empty(surname, surname_txt):
                return
            if is_empty(given_names, given_names_txt):
                return
            if is_empty(document_number, document_number_txt):
                return
            if is_empty(nationality, nationality_txt):
                return
            if is_empty(birth_date, birth_date_txt):
                return
            if is_empty(sex, sex_txt):
                return
            if is_empty(expiry_date, expiry_date_txt):
                return
            try:
                mrz_field.value = MRVBCodeGenerator(
                    document_type_txt.value, country_code_txt.value, surname_txt.value, given_names_txt.value, document_number_txt.value, nationality_txt.value, birth_date_txt.value, sex_txt.value, expiry_date_txt.value, optional_data1_txt.value)
            except Exception as e:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(str(e)),
                    action="OK",
                )
                page.snack_bar.open = True

        page.update()

    page.title = 'Flet MRZ example'
    page.vertical_alignment = ft.MainAxisAlignment.START

    dropdown = ft.Dropdown(on_change=dropdown_changed, width=200, options=[
        ft.dropdown.Option('Passport(TD3)'),
        ft.dropdown.Option('ID Card(TD1)'),
        ft.dropdown.Option('ID Card(TD2)'),
        ft.dropdown.Option('Visa(A)'),
        ft.dropdown.Option('Visa(B)'),
    ],)
    dropdown.value = 'Passport(TD3)'

    button_generate = ft.ElevatedButton(
        text="Generate", on_click=generate_mrz)

    button_random = ft.ElevatedButton(
        text="Random", on_click=generate_random)

    mrz_field = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=510, height=100, multiline=True)

    page.add(
        ft.Column(controls=[
            dropdown,
            container_loaded,
            ft.Row([button_generate]),
            mrz_field], scroll=True)
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
