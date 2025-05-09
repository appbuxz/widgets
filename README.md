rus:
Погодный Виджет на PyQt6 🌤

Минималистичный и стильный погодный виджет, созданный с использованием библиотеки PyQt6, отображает текущую погоду в выбранном городе, обновляется в реальном времени и красиво анимирован. Работает поверх всех окон и не имеет рамки.

🚀 Особенности

    Анимированное появление и обновление данных

    Автоматическое обновление каждые 60 секунд

    Поддержка градиентного фона и закругленных углов

    Перетаскиваемое окно без рамки

    Отображение:

        текущей температуры,

        погодного состояния,

        влажности, ветра, ощущаемой температуры

        времени последнего обновления

🌐 Используемый сервис

Для получения актуальных погодных данных используется WeatherAPI.
Почему именно WeatherAPI?

    ✅ Бесплатный тариф — идеально подходит для личных и учебных проектов

    ✅ Простота в использовании — удобная и понятная документация

    ✅ Поддержка разных языков — возможность отображения информации на русском языке

📦 Зависимости

Перед запуском убедитесь, что у вас установлены необходимые библиотеки:
pip install PyQt6 requests

🛠 Запуск
python weather.py

(файл weather.py — это ваш файл с кодом)
🏙 Город по умолчанию

По умолчанию отображается погода для города Актобе. Чтобы изменить его, замените строку:
CITY = "Актобе"
на нужный вам город в коде.

🔐 Ключ API
Убедитесь, что у вас есть свой API-ключ от WeatherAPI, и подставьте его в переменную:
API_KEY = "ваш_ключ"






eng:
  Weather Widget with PyQt6 🌦

A stylish, frameless and minimalistic PyQt6 weather widget that displays current weather conditions in real-time. It stays on top of all windows, auto-refreshes, and includes smooth animations.

🚀 Features

    Animated appearance and data refresh

    Auto-updates every 60 seconds

    Frameless, translucent window with gradient background

    Draggable interface

    Displays:

        current temperature

        weather condition description

        humidity, wind speed, feels-like temperature

        last updated time

🌐 Weather Data Provider

This project uses WeatherAPI to fetch live weather information.
Why WeatherAPI?

    ✅ Free plan available — ideal for personal and educational use

    ✅ Simple and clear API — easy to integrate

    ✅ Supports multiple languages — including Russian for localized display

📦 Dependencies

Make sure you have the required libraries installed:
pip install PyQt6 requests

🛠 How to Run
python weather.py
(weather.py is the name of your Python file)

🏙 Default City
The default city is set to Aktobe. You can change it in the code:
CITY = "Aktobe"

🔐 API Key
To run the widget, you’ll need a free API key from WeatherAPI. Replace this line:
API_KEY = "your_key_here"
with your actual API key.
