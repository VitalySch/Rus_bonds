from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from tradetool import OFZ, SUB



OFZ_bond = OFZ()
Sub_bond = SUB()

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Screen_ofz(Screen):
    def load_table(self):
        self.values = OFZ_bond.values
        self.ofz_tables = MDDataTable(size_hint=(1, 0.85),
                                      use_pagination=True,
                                      check=True,
                                      rows_num=10,
                                      background_color_header="#FFD600",
                                      background_color_cell="#FFD600",
                                      background_color_selected_cell="#A68B00",
                                      column_data=[
                                          ('Наименование', dp(40)),
                                          ('Сумма купона', dp(20)),
                                          ('Купонов в год', dp(20)),
                                          ('Дата погашения', dp(25)),
                                          ('Спрос', dp(20)),
                                          ('Предложение', dp(20)),
                                          ('Доходность по оценке пред. дня', dp(20)),
                                          ('Средняя цена предыдущего дня', dp(20)),
                                      ],
                                      row_data=self.values
                                      )

        self.add_widget(self.ofz_tables)
        return self

    def on_enter(self):
        self.load_table()

class Screen_sub(Screen):
    def load_table(self):
        self.values = Sub_bond.values
        self.sub_tables = MDDataTable(size_hint=(1, 0.85),
                                      use_pagination=True,
                                      check=True,
                                      rows_num=10,
                                      background_color_header="#FFD600",
                                      background_color_cell="#FFD600",
                                      background_color_selected_cell="#A68B00",
                                      column_data=[
                                          ('Наименование', dp(40)),
                                          ('Сумма купона', dp(20)),
                                          ('Купонов в год', dp(20)),
                                          ('Дата погашения', dp(25)),
                                          ('Спрос', dp(20)),
                                          ('Предложение', dp(20)),
                                          ('Доходность по оценке пред. дня', dp(20)),
                                          ('Средняя цена предыдущего дня', dp(20)),
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