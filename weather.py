from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QMouseEvent
import requests
import sys

class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Погодный виджет")
        self.setFixedSize(250, 150)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Прозрачность
        self.setStyleSheet("""
            background-color: #2b2b2b;
            color: white;
            border-radius: 10px;
            padding: 10px;
            font-family: Arial;
        """)

        self.city_label = QLabel("Город: ...")
        self.temp_label = QLabel("Температура: ...")
        self.condition_label = QLabel("Состояние: ...")

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.condition_label)
        self.setLayout(layout)

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

    def update_weather(self):
        API_KEY = "78e34157f30c45d095291555250805"
        CITY = "Актобе"
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=ru"
        
        try:
            data = requests.get(url).json()
            self.city_label.setText(f"Город: {data['location']['name']}")
            self.temp_label.setText(f"🌡 Температура: {data['current']['temp_c']}°C")
            self.condition_label.setText(f"☁ {data['current']['condition']['text']}")
        except:
            self.condition_label.setText("Ошибка загрузки")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WeatherWidget()
    widget.show()
    sys.exit(app.exec())