# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt, QDate, QSize
from PySide6.QtWidgets import (
    QWidget, QTabWidget, QSplitter, QTableWidget, QHeaderView,
    QGroupBox, QFormLayout, QDateEdit, QDoubleSpinBox, QComboBox, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QSize(480, 320))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --------- Tab widget ---------
        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")

        # Главная
        self.tab_home = QWidget()
        self.tab_home.setObjectName("tab_home")
        self._setup_home_tab(self.tab_home)
        self.tabs.addTab(self.tab_home, "Главная")

        # Аналитика
        self.tab_analytics = QWidget()
        self.tab_analytics.setObjectName("tab_analytics")
        self._setup_analytics_tab(self.tab_analytics)
        self.tabs.addTab(self.tab_analytics, "Аналитика")

        # Инструменты
        self.tab_tools = QWidget()
        self.tab_tools.setObjectName("tab_tools")
        self._setup_tools_tab(self.tab_tools)
        self.tabs.addTab(self.tab_tools, "Инструменты")

        # Настройки
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self._setup_settings_tab(self.tab_settings)
        self.tabs.addTab(self.tab_settings, "Настройки")

        # Main layout
        layout = QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralwidget)

    # ---------------- Home tab ----------------
    def _setup_home_tab(self, tab):
        layout = QHBoxLayout(tab)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # Table with transactions
        self.table = QTableWidget(0, 4)
        self.table.setObjectName("table")
        self.table.setHorizontalHeaderLabels(["Дата", "Категория", "Описание", "Сумма"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        splitter.addWidget(self.table)

        # Right side form
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        form = QGroupBox("Новая транзакция")
        form_layout = QFormLayout(form)

        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(QDate.currentDate())
        self.sumEdit = QDoubleSpinBox(); self.sumEdit.setMaximum(1e9)
        self.catEdit = QComboBox(); self.catEdit.addItems(["Еда", "Транспорт", "Доход"])
        self.descEdit = QLineEdit()

        form_layout.addRow("Дата:", self.dateEdit)
        form_layout.addRow("Сумма:", self.sumEdit)
        form_layout.addRow("Категория:", self.catEdit)
        form_layout.addRow("Описание:", self.descEdit)

        self.add_btn = QPushButton("Добавить")
        self.del_btn = QPushButton("Удалить выбранное")

        right_layout.addWidget(form)
        right_layout.addWidget(self.add_btn)
        right_layout.addWidget(self.del_btn)
        right_layout.addStretch()

        splitter.addWidget(right_panel)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 1)

    # ---------------- Analytics tab ----------------
    def _setup_analytics_tab(self, tab):
        vbox = QVBoxLayout(tab)
        self.period_box = QComboBox()
        self.period_box.addItems(["Последние 7 дней", "Месяц", "Год", "Весь период"])
        vbox.addWidget(self.period_box)

        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        board = QWidget(); board_layout = QVBoxLayout(board)
        board_layout.addWidget(QLabel("⏳ Графики появятся позже…", alignment=Qt.AlignCenter))
        scroll.setWidget(board)
        vbox.addWidget(scroll)

    # ---------------- Tools tab ----------------
    def _setup_tools_tab(self, tab):
        vbox = QVBoxLayout(tab)

        conv = QGroupBox("Конвертер валют"); conv_layout = QFormLayout(conv)
        self.amountSpin = QDoubleSpinBox(); self.amountSpin.setMaximum(1e9)
        self.fromCur = QComboBox(); self.fromCur.addItems(["RUB", "USD", "EUR"])
        self.toCur = QComboBox(); self.toCur.addItems(["RUB", "USD", "EUR"])
        self.resultLabel = QLabel("—")
        self.convert_btn = QPushButton("Конвертировать")

        conv_layout.addRow("Сумма:", self.amountSpin)
        conv_layout.addRow("Из:", self.fromCur)
        conv_layout.addRow("В:", self.toCur)
        conv_layout.addRow(self.convert_btn, self.resultLabel)

        io_box = QGroupBox("Импорт / Экспорт"); io_layout = QVBoxLayout(io_box)
        self.import_btn = QPushButton("Импорт CSV")
        self.export_btn = QPushButton("Экспорт CSV")
        io_layout.addWidget(self.import_btn)
        io_layout.addWidget(self.export_btn)

        vbox.addWidget(conv)
        vbox.addWidget(io_box)
        vbox.addStretch()

    # ---------------- Settings tab ----------------
    def _setup_settings_tab(self, tab):
        outer = QVBoxLayout(tab)
        scroll = QScrollArea(); scroll.setWidgetResizable(True)
        inner = QWidget(); form = QFormLayout(inner)

        self.theme_box = QComboBox(); self.theme_box.addItems(["Светлая", "Тёмная (default)"])
        self.lang_box = QComboBox(); self.lang_box.addItems(["Русский", "English"])
        self.cur_box = QComboBox(); self.cur_box.addItems(["RUB", "USD", "EUR"])
        self.save_btn = QPushButton("Сохранить")

        form.addRow("Тема:", self.theme_box)
        form.addRow("Язык:", self.lang_box)
        form.addRow("Валюта по-умолчанию:", self.cur_box)
        form.addRow(self.save_btn)

        scroll.setWidget(inner)
        outer.addWidget(scroll)