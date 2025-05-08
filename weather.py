from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QFont, QMouseEvent
import sys
from datetime import datetime

class DraggableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |  # Без рамки
            Qt.WindowType.WindowStaysOnTopHint   # Поверх всех окон
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Прозрачность
        self.setGeometry(100, 100, 200, 100)  # x, y, width, height

        # Стиль виджета
        self.setStyleSheet("""
            background-color: rgba(30, 30, 30, 180);
            border-radius: 10px;
            color: white;
        """)

        # Текст (часы)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 20))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Таймер для обновления времени
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Обновлять каждую секунду

        # Для перетаскивания
        self.drag_pos = QPoint()

    def update_time(self):
        """Обновляет время на виджете."""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time)

    def mousePressEvent(self, event: QMouseEvent):
        """Захватывает позицию при клике."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        """Перемещает виджет при зажатой ЛКМ."""
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_pos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = DraggableWidget()
    widget.show()
    sys.exit(app.exec())