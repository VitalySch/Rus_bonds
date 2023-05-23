from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from tradetool import Bonds



bonds = Bonds()
ofz = bonds.df.loc[(bonds.df['Тип ценной бумаги'] == "3")]
sub = bonds.df.loc[(bonds.df['Тип ценной бумаги'] == "4")]

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Screen_ofz(Screen):
    def load_table(self):
        self.values = ofz.values
        self.ofz_tables = MDDataTable(size_hint=(1, 0.85),
                                      use_pagination=True,
                                      check=True,
                                      rows_num=10,
                                      background_color_header="#FFFF00",
                                      background_color_cell="#FFFF00",
                                      background_color_selected_cell="#A68B00",
                                      column_data=[
                                          ('Наименование', dp(40)),
                                          ('Дата погашения', dp(20)),
                                          ('Год погашения', dp(20), self.sort_col),
                                          ('Номинал', dp(15)),
                                          ('Валюта', dp(15)),
                                          ('Спрос', dp(15), self.sort_col),
                                          ('Предложение', dp(25)),
                                          ('Сумма купона', dp(20)),
                                          ('Купонов в год', dp(20)),
                                          ('Доходность по оценке пред. дня', dp(20)),
                                          ('Средняя цена предыдущего дня', dp(20)),
                                          ('Тип ценной бумаги', dp(20)),

                                      ],
                                      row_data=self.values
                                      )

        self.add_widget(self.ofz_tables)
        return self

    def on_enter(self):
        self.load_table()

    def sort_col(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))

class Screen_sub(Screen):
    def load_table(self):
        self.values = sub.values
        self.sub_tables = MDDataTable(size_hint=(1, 0.85),
                                      use_pagination=True,
                                      check=True,
                                      rows_num=10,
                                      background_color_header="#FFFF00",
                                      background_color_cell="#FFFF00",
                                      background_color_selected_cell="#A68B00",
                                      column_data=[
                                          ('Наименование', dp(40)),
                                          ('Дата погашения', dp(20)),
                                          ('Год погашения', dp(20)),
                                          ('Номинал', dp(15)),
                                          ('Валюта', dp(15)),
                                          ('Спрос', dp(15)),
                                          ('Предложение', dp(25)),
                                          ('Сумма купона', dp(20)),
                                          ('Купонов в год', dp(20)),
                                          ('Доходность по оценке пред. дня', dp(20)),
                                          ('Средняя цена предыдущего дня', dp(20)),
                                          ('Тип ценной бумаги', dp(20)),
                                      ],
                                      row_data=self.values
                                      )

        self.add_widget(self.sub_tables)
        return self

    def on_enter(self):
        self.load_table()

class Bonds(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        # self.theme_cls.primary_hue = "A100"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.material_style = "M3"
        return Builder.load_file('moex.kv')


Bonds().run()