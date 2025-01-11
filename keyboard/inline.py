from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_functions_keyboard():
    """Функция для создания клавиатуры."""
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="📖 О нас", callback_data="about_us"))

    keyboard.add(InlineKeyboardButton(text="🛠️ Наши услуги", callback_data="our_services"))

    keyboard.add(InlineKeyboardButton(text="💳 Оплата и условия", callback_data="payment_terms"))

    keyboard.add(InlineKeyboardButton(text="💬 Часто задаваемые вопросы (FAQ)", callback_data="faq"))

    keyboard.add(InlineKeyboardButton(text="📈 Наши преимущества", callback_data="advantages"))

    keyboard.add(InlineKeyboardButton(text="📅 Связаться с нами", callback_data="contact_us"))

    keyboard.add(InlineKeyboardButton(text="✨ Полезные функции от нас", callback_data="useful_features"))
    return keyboard.adjust(1, 2, 1, 1, 1, 1, ).as_markup()


def return_functions_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="📅 Связаться с нами", callback_data="contact_us"))
    keyboard.add(InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start"))
    return keyboard.adjust(1, ).as_markup()


def our_projects_functions_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🔗 Перейти к проекту Sengoku", url="https://t.me/sengokukg_bot"))
    keyboard.add(InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start"))
    return keyboard.adjust(1, ).as_markup()


def get_cancel_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="❌ Отменить", callback_data="cancel"))
    return keyboard.adjust(1).as_markup()


def return_menu_functions_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start_"))
    return keyboard.adjust(1, ).as_markup()


def contact_us_functions_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="Напишите нам в WhatsApp", url="https://api.whatsapp.com/send/?phone=%2B996503556500"),
        InlineKeyboardButton(text="Напишите нам в Telegram", url="https://t.me/t0kt0bek0vv"),
        InlineKeyboardButton(text="Напишите нам в Instagram", url="https://www.instagram.com/okurmen_studio/"),
        InlineKeyboardButton(text="📩 Связаться с администратором", callback_data="contact_admin"),
        # Кнопка для связи с администратором
        InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start")
    )
    return keyboard.adjust(1, ).as_markup()


def useful_features_functions_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="🤖 Чат с ИИ", callback_data="chat_ai"),
        InlineKeyboardButton(text="🎵 Создать музыку", callback_data="create_music"),
        InlineKeyboardButton(text="📖 Создать сказку", callback_data="create_story"),
        InlineKeyboardButton(text="🔙 Вернуться в главное меню", callback_data="start")
    )
    return keyboard.adjust(1, 1, 1, 1).as_markup()

# Массив вопросов и ответов
FAQ = [
    {"question": "❓ Как заказать?", "answer": "Свяжитесь с нами через кнопку '📅 Связаться с нами'. Мы обсудим детали вашего проекта и приступим к работе!"},
    {"question": "❓ Время разработки?", "answer": "Сроки зависят от сложности проекта. Обычно разработка занимает от 1 до 4 недель."},
    {"question": "❓ Как оплатить?", "answer": "Мы принимаем оплату через банковский перевод или карту. Уточните детали у нашего менеджера."},
    {"question": "❓ Какие услуги предоставляет студия?", "answer": "Наша студия предоставляет услуги по разработке сайтов, мобильных приложений, а также дизайну и маркетингу."},
    {"question": "❓ Могу ли я внести изменения в проект после начала работы?", "answer": "Да, изменения возможны, но они могут повлиять на сроки и стоимость разработки."},
    {"question": "❓ Какие технологии вы используете?", "answer": "Мы используем современные технологии, включая Python, Django, React, и другие популярные фреймворки."},
    {"question": "❓ Предоставляете ли вы поддержку после завершения проекта?", "answer": "Да, мы предлагаем техническую поддержку и обслуживание после завершения проекта."}
]

def generate_faq_keyboard():
    builder = InlineKeyboardBuilder()
    for index, item in enumerate(FAQ):
        builder.button(text=item["question"], callback_data=f"faq_{index}")
    builder.button(text="⬅️ Назад", callback_data="return")
    return builder.adjust(1, ).as_markup()
