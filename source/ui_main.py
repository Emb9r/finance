# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt, QSize, QCoreApplication
from PySide6.QtWidgets import (
    QApplication, QComboBox, QDateEdit, QDoubleSpinBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QHeaderView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 700)
        MainWindow.setMinimumSize(QSize(480, 320))

        self.centralwidget = QWidget(MainWindow)
        self.gridLayout = QGridLayout(self.centralwidget)

        # ───────── Tabs ─────────
        self.tabs = QTabWidget(self.centralwidget)
        self._init_home_tab()
        self._init_analytics_tab()
        self._init_tools_tab()
        self._init_settings_tab()

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    # ===== helpers =====
    def _init_home_tab(self):
        self.tab_home = QWidget(); layout = QHBoxLayout(self.tab_home)
        # ── Левая часть: таблица
        v_left = QVBoxLayout()
        self.table = QTableWidget(columnCount=4)
        headers = ["Дата", "Сумма", "Категория", "Описание"]
        for idx, h in enumerate(headers):
            self.table.setHorizontalHeaderItem(idx, QTableWidgetItem(h))
        # растягиваем колонки
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        v_left.addWidget(self.table)
        # индикаторы баланса
        h_bal = QHBoxLayout()
        for txt in ("Текущий баланс", "100", "Траты", "50", "Доходы", "150"):
            h_bal.addWidget(QLabel(txt))
        v_left.addLayout(h_bal)
        layout.addLayout(v_left)
        # ── Правая часть: форма + кнопки
        v_right = QVBoxLayout()
        group = QGroupBox("Новая транзакция"); form = QFormLayout(group)
        form.addRow("Дата:", QDateEdit())
        sumSpin = QDoubleSpinBox(minimum=-1e8, maximum=1e9); form.addRow("Сумма:", sumSpin)
        catBox = QComboBox(); catBox.addItems(["Еда", "Транспорт", "Доход"])
        form.addRow("Категория:", catBox)
        form.addRow("Описание:", QLineEdit())
        v_right.addWidget(group)
        v_right.addWidget(QPushButton("Добавить"))
        v_right.addWidget(QPushButton("Удалить выбранное"))
        v_right.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addLayout(v_right)
        self.tabs.addTab(self.tab_home, "Главная")

    def _init_analytics_tab(self):
        self.tab_analytics = QWidget(); v_main = QVBoxLayout(self.tab_analytics)
        self.period_box = QComboBox(); self.period_box.addItems(["Последние 7 дней", "Месяц", "Год", "Весь период"])
        v_main.addWidget(self.period_box)
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); scroll.setWidget(content)
        grid = QGridLayout(content)
        titles = [
            "Расходы по категориям (Pie)",
            "Доход / Расход по месяцам (Bar)",
            "Баланс со временем (Line)",
            "Траты по счётам (Donut)"
        ]
        for i, t in enumerate(titles):
            grp = QGroupBox(t)
            QVBoxLayout(grp).addWidget(QLabel("📊 …", alignment=Qt.AlignCenter))
            grid.addWidget(grp, i // 2, i % 2)
        v_main.addWidget(scroll)
        self.tabs.addTab(self.tab_analytics, "Аналитика")

    def _init_tools_tab(self):
        from functools import partial
        self.tab_tools = QWidget(); v = QVBoxLayout(self.tab_tools)
        # конвертер
        g = QGroupBox("Конвертер валют"); f = QFormLayout(g)
        amount = QDoubleSpinBox(maximum=1e9); f.addRow("Сумма:", amount)
        cur_from = QComboBox(); cur_from.addItems(["RUB", "USD", "EUR"])
        cur_to = QComboBox(); cur_to.addItems(["RUB", "USD", "EUR"])
        f.addRow("Из:", cur_from); f.addRow("В:", cur_to)
        btn_conv, lbl_res = QPushButton("Конвертировать"), QLabel("—")
        f.addRow(btn_conv, lbl_res)
        v.addWidget(g)
        # кредит
        g2 = QGroupBox("Калькулятор кредита"); f2 = QFormLayout(g2)
        p = QDoubleSpinBox(maximum=1e9); r = QDoubleSpinBox(suffix=" %", maximum=100.0, decimals=2)
        t = QSpinBox(suffix=" мес", maximum=480)
        btn_c = QPushButton("Рассчитать платёж"); lbl_c = QLabel("—")
        for lab, w in (("Сумма кредита:", p), ("Ставка (% год):", r), ("Срок:", t)):
            f2.addRow(lab, w)
        f2.addRow(btn_c, lbl_c)
        v.addWidget(g2)
        # вклад
        g3 = QGroupBox("Калькулятор вклада"); f3 = QFormLayout(g3)
        init = QDoubleSpinBox(maximum=1e9); rate = QDoubleSpinBox(suffix=" %", maximum=100.0, decimals=2)
        term = QSpinBox(suffix=" мес", maximum=480); month = QDoubleSpinBox(prefix="+ ", maximum=1e9)
        btn_d = QPushButton("Рассчитать итог"); lbl_d = QLabel("—")
        for lab, w in (("Начальная сумма:", init), ("Ставка (% год):", rate), ("Срок:", term), ("Ежемесячный взнос:", month)):
            f3.addRow(lab, w)
        f3.addRow(btn_d, lbl_d)
        v.addWidget(g3)
        v.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.tabs.addTab(self.tab_tools, "Инструменты")

    def _init_settings_tab(self):
        self.tab_settings = QWidget(); v = QVBoxLayout(self.tab_settings)
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        content = QWidget(); scroll.setWidget(content)
        form = QFormLayout(content)
        lang = QComboBox(); lang.addItems(["Русский", "English"])
        theme = QComboBox(); theme.addItems(["Светлая", "Тёмная"])
        cur = QComboBox(); cur.addItems(["RUB", "USD", "EUR"])
        form.addRow("Язык:", lang)
        form.addRow("Тема:", theme)
        form.addRow("Валюта по умолчанию:", cur)
        form.addRow("", QPushButton("Сохранить"))
        v.addWidget(scroll)
        self.tabs.addTab(self.tab_settings, "Настройки")

    # ── translate ──
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Управление финансами"))