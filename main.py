import flet as ft

from mrz.generator.td1 import TD1CodeGenerator
from mrz.generator.td2 import TD2CodeGenerator
from mrz.generator.td3 import TD3CodeGenerator
from mrz.generator.mrva import MRVACodeGenerator
from mrz.generator.mrvb import MRVBCodeGenerator

import utils


def main(page: ft.Page):

    document_type = ft.Text('Document type')
    country_code = ft.Text('Country')
    document_number = ft.Text('Document number')
    birth_date = ft.Text('Birth date')
    sex = ft.Text('Sex')
    expiry_date = ft.Text('Expiry date')
    nationality = ft.Text('Nationality')
    surname = ft.Text('Surname')
    given_names = ft.Text('Given names')
    optional_data1 = ft.Text('Optional data 1')
    optional_data2 = ft.Text('Optional data 2')

    document_type_txt = ft.TextField(
        value='P', text_align=ft.TextAlign.LEFT, width=200, height=50)

    country_code_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    document_number_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    birth_date_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    sex_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    expiry_date_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    nationality_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    surname_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    given_names_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

    optional_data1_txt = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=200, height=50)

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

    def generate_random_data():
        data = utils.random_mrz_data()
        surname_txt.value = data['Surname']
        given_names_txt.value = data['Given Name']
        nationality_txt.value = data['Nationality']
        country_code_txt.value = nationality_txt.value
        sex_txt.value = data['Sex']
        document_number_txt.value = data['Document Number']
        birth_date_txt.value = data['Birth Date']
        expiry_date_txt.value = data['Expiry Date']

    generate_random_data()

    def dropdown_changed(e):
        if dropdown.value == 'ID Card(TD1)':
            document_type_txt.value = 'I'
        elif dropdown.value == 'ID Card(TD2)':
            document_type_txt.value = 'I'
        elif dropdown.value == 'Passport(TD3)':
            document_type_txt.value = 'P'

        elif dropdown.value == 'Visa(A)':
            document_type_txt.value = 'V'

        elif dropdown.value == 'Visa(B)':
            document_type_txt.value = 'V'

        generate_random(e)

    def is_empty(filed_name, filed_text):
        if filed_text.value == None or filed_text.value == '':
            page.snack_bar = ft.SnackBar(
                content=ft.Text(filed_name.value + ' is empty!'),
                action='OK',
            )
            page.snack_bar.open = True
            page.update()
            return True
        return False

    def generate_random(e):
        generate_random_data()
        generate_mrz(e)
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
                    action='OK',
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
                    action='OK',
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
                    action='OK',
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
                    action='OK',
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
                    action='OK',
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
        text='Generate', on_click=generate_mrz)

    button_random = ft.ElevatedButton(
        text='Random', on_click=generate_random)

    mrz_field = ft.TextField(
        value='', text_align=ft.TextAlign.LEFT, width=510, height=100, multiline=True, text_size=14)

    page.add(
        ft.Column(controls=[
            dropdown,
            container_loaded,
            ft.Row([button_random, button_generate]),
            mrz_field], scroll=True)
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
