import PySimpleGUI as sg

athema = {'BACKGROUND': 'DARKBLUE',
                'TEXT': 'BLACK',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#WHITE',
                'BUTTON': ('white', 'DARKGREEN'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0 }

sg.theme_add_new('Athema', athema)
