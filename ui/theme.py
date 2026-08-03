STYLE = """
/* ==========================
   GENEL
   ========================== */

QWidget{
    font-family: "Segoe UI";
    font-size: 10pt;
    color: palette(window-text);
    background: palette(window);
}

/* ==========================
   MENÜ
   ========================== */

QMenuBar{
    background: palette(window);
    color: palette(window-text);
    border-bottom: 1px solid palette(mid);
}

QMenuBar::item{
    padding: 6px 10px;
    background: transparent;
}

QMenuBar::item:selected{
    background: #1976D2;
    color: white;
}

QMenu{
    background: palette(base);
    color: palette(text);
    border: 1px solid palette(mid);
}

QMenu::item{
    padding: 6px 24px;
}

QMenu::item:selected{
    background: #1976D2;
    color: white;
}

/* ==========================
   TAB
   ========================== */

QTabWidget::pane{
    border: 1px solid palette(mid);
}

QTabBar::tab{
    background: palette(button);
    color: palette(button-text);
    padding: 10px 18px;
    border: 1px solid palette(mid);
}

QTabBar::tab:selected{
    background: #1976D2;
    color: white;
}

/* ==========================
   BUTON
   ========================== */

QPushButton{
    background: #1976D2;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 14px;
}

QPushButton:hover{
    background: #1565C0;
}

QPushButton:pressed{
    background: #0D47A1;
}

QPushButton:disabled{
    background: #9E9E9E;
    color: white;
}

/* ==========================
   INPUT
   ========================== */

QLineEdit{
    background: palette(base);
    color: palette(text);
    border: 1px solid palette(mid);
    border-radius: 6px;
    padding: 6px;
    selection-background-color: #1976D2;
    selection-color: white;
}

/* ==========================
   TABLE
   ========================== */

QTableWidget{
    background: palette(base);
    alternate-background-color: palette(alternate-base);
    color: palette(text);
    border: 1px solid palette(mid);
    gridline-color: palette(mid);
    selection-background-color: #1976D2;
    selection-color: white;
}

QHeaderView::section{
    background: #1976D2;
    color: white;
    border: none;
    padding: 6px;
    font-weight: bold;
}

QTableCornerButton::section{
    background: #1976D2;
    border: none;
}

/* ==========================
   LABEL
   ========================== */

QLabel{
    color: palette(window-text);
    background: transparent;
}

/* ==========================
   STATUS BAR
   ========================== */

QStatusBar{
    background: palette(window);
    color: palette(window-text);
    border-top: 1px solid palette(mid);
}

/* ==========================
   PROGRESS BAR
   ========================== */

QProgressBar{
    background: palette(base);
    color: palette(text);
    border: 1px solid palette(mid);
    border-radius: 6px;
    text-align: center;
}

QProgressBar::chunk{
    background: #1976D2;
}

/* ==========================
   MESSAGE BOX
   ========================== */

QMessageBox{
    background: palette(window);
}

QMessageBox QLabel{
    color: palette(window-text);
    background: transparent;
}

QMessageBox QPushButton{
    min-width: 90px;
}

/* ==========================
   SCROLL BAR
   ========================== */

QScrollBar:vertical{
    background: palette(window);
    width: 12px;
    margin: 0px;
}

QScrollBar::handle:vertical{
    background: #1976D2;
    border-radius: 5px;
    min-height: 25px;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{
    height: 0px;
}

QScrollBar:horizontal{
    background: palette(window);
    height: 12px;
}

QScrollBar::handle:horizontal{
    background: #1976D2;
    border-radius: 5px;
    min-width: 25px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal{
    width: 0px;
}
"""
