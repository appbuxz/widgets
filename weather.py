from PyQt6.QtWidgets import (QApplication, QLabel, QVBoxLayout, QWidget, 
                            QHBoxLayout, QPushButton)
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QPoint
from PyQt6.QtGui import QFont, QMouseEvent, QIcon, QColor
from PyQt6.QtGui import QPainter, QBrush, QPen, QLinearGradient
import requests
import sys
from datetime import datetime

class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_animations()
        self.setup_weather_data()
        
    def setup_ui(self):
        # Основные настройки окна
        self.setWindowTitle("Погодный Виджет")
        self.setFixedSize(300, 180)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | 
                          Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Стиль виджета
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(40, 40, 50, 200);
                border-radius: 15px;
                color: white;
                font-family: 'Segoe UI';
            }
            QLabel {
                padding: 2px;
            }
            QPushButton {
                background-color: transparent;
                border: none;
                color: white;
            }
        """)
        
        # Создаем элементы интерфейса
        self.city_label = QLabel("Загрузка...")
        self.city_label.setFont(QFont('Arial', 12, QFont.Weight.Bold))
        
        self.temp_label = QLabel()
        self.temp_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        
        self.condition_label = QLabel()
        self.condition_label.setFont(QFont('Arial', 10))
        
        self.details_label = QLabel()
        self.details_label.setFont(QFont('Arial', 9))
        
        self.time_label = QLabel()
        self.time_label.setFont(QFont('Arial', 8))
        
        # Кнопка закрытия
        self.close_btn = QPushButton("✕")
        self.close_btn.setFixedSize(20, 20)
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setStyleSheet("""
            QPushButton:hover {
                color: #ff5555;
            }
        """)
        
        # Кнопка обновления
        self.refresh_btn = QPushButton("⟳")
        self.refresh_btn.setFixedSize(20, 20)
        self.refresh_btn.clicked.connect(self.update_weather)
        
        # Размещаем элементы
        header = QHBoxLayout()
        header.addWidget(self.city_label)
        header.addStretch()
        header.addWidget(self.refresh_btn)
        header.addWidget(self.close_btn)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(header)
        main_layout.addWidget(self.temp_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.condition_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.details_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.time_label, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.setSpacing(5)
        
        self.setLayout(main_layout)
        
        # Для перетаскивания окна
        self.drag_pos = QPoint()
        
    def setup_animations(self):
        # Анимация появления
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(500)
        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)
        self.opacity_animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.opacity_animation.start()
        
        # Анимация обновления данных
        self.update_animation = QPropertyAnimation(self, b"geometry")
        self.update_animation.setDuration(300)
        
    def setup_weather_data(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(60000)  # Обновлять каждую минуту
        self.update_weather()
        
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint() - self.pos()
            
    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_pos)
            
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Градиентный фон
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(60, 60, 80, 220))
        gradient.setColorAt(1, QColor(40, 40, 50, 220))
        
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 15, 15)
        
        # Тень
        painter.setPen(QPen(QColor(0, 0, 0, 50), 5))
        painter.drawRoundedRect(self.rect(), 15, 15)
        
    def update_weather(self):
        # Анимация обновления
        self.update_animation.setStartValue(self.geometry())
        self.update_animation.setEndValue(self.geometry().adjusted(0, -5, 0, -5))
        self.update_animation.start()
        
        API_KEY = "78e34157f30c45d095291555250805"
        CITY = "Актобе"
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=ru"
        
        try:
            data = requests.get(url).json()
            
            # Обновляем данные
            self.city_label.setText(f"{data['location']['name']}")
            self.temp_label.setText(f"{data['current']['temp_c']}°C")
            self.condition_label.setText(data['current']['condition']['text'])
            
            # Дополнительная информация
            details = (f"💨 Ветер: {data['current']['wind_kph']} км/ч | "
                      f"💧 Влажность: {data['current']['humidity']}% ")
            self.details_label.setText(details)
            
            # Время последнего обновления
            now = datetime.now().strftime("%H:%M:%S")
            self.time_label.setText(f"Обновлено: {now}")
            
            # Изменяем цвет в зависимости от температуры
            temp = data['current']['temp_c']
            if temp > 25:
                color = "#ff6b6b"  # Жарко
            elif temp > 15:
                color = "#feca57"  # Тепло
            else:
                color = "#54a0ff"  # Холодно
                
            self.temp_label.setStyleSheet(f"color: {color};")
            
        except Exception as e:
            print("Ошибка:", e)
            self.condition_label.setText("Ошибка загрузки данных")
            
        # Возвращаем виджет на место после анимации
        self.update_animation.setStartValue(self.geometry())
        self.update_animation.setEndValue(self.geometry().adjusted(0, 5, 0, 5))
        self.update_animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WeatherWidget()
    widget.show()
    sys.exit(app.exec())