from aiogram import F, types, Router, Bot
from aiogram.enums import ParseMode, ChatMemberStatus
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession
from filter.chat_types import ChatTypeFilter
from keyboard.inline import *

start_functions_private_router = Router()
start_functions_private_router.message.filter(ChatTypeFilter(['private']))

welcome_text = (
    """👋 Добро пожаловать в Окурмэн Студия!

Мы предлагаем:
🌐 Создание сайтов
📱 Разработку мобильных приложений для Android и iOS
🎓 Обучение IT

📍 Мы находимся в Бишкеке и готовы помочь вам реализовать ваши идеи!

📞 Для связи нажмите на кнопку ниже 👇"""
)


# Обработчик команды /start
@start_functions_private_router.message(CommandStart())
async def start_cmd(message: types.Message, ):
    """Обработчик команды /start"""
    await message.answer_photo(
        photo=types.FSInputFile('media/img/img.png'),
        caption=welcome_text,
        reply_markup=start_functions_keyboard()
    )


# Обработчик нажатия кнопки "Старт"
@start_functions_private_router.callback_query(F.data == "start")
async def start_main_menu(query: types.CallbackQuery, ):
    """Обработчик callback_query для основного меню"""
    await query.message.edit_caption(
        caption=welcome_text,
        reply_markup=start_functions_keyboard())


@start_functions_private_router.callback_query(F.data == "start_")
async def start_main_menu(query: types.CallbackQuery, ):
    """Обработчик callback_query для основного меню"""
    await query.message.delete()
    await query.message.answer_photo(
        photo=types.FSInputFile('media/img/img.png'),
        caption=welcome_text,
        reply_markup=start_functions_keyboard()
    )


@start_functions_private_router.callback_query(F.data == "return")
async def return_main_menu(query: types.CallbackQuery, ):
    """Обработчик callback_query для основного меню"""
    await query.message.answer_photo(
        photo=types.FSInputFile('media/img/img.png'),
        caption=welcome_text,
        reply_markup=start_functions_keyboard()
    )

@start_functions_private_router.callback_query(F.data == 'about_us')
async def about_us_command_callback_query(query: types.CallbackQuery) -> None:
    keyboard_markup = return_functions_keyboard()
    caption_text = (
        "<b>Окурмэн Студия</b> — студия, специализирующаяся на разработке современных сайтов 🌐 и Telegram-ботов 🤖. \n"
        "Мы предлагаем инновационные и интеллектуальные решения для цифрового пространства 💡.\n\n"
        "<b>Наша команда</b> — это специалисты с богатым опытом в области разработки и дизайна. \n"
        "Мы помогаем компаниям и стартапам достигать успеха в цифровом мире 🌟.\n\n"
        "<b>Наши услуги:</b>\n"
        "<b>🌐 Разработка сайтов</b> — создание современных и функциональных сайтов для вашего бизнеса.\n"
        "<b>🤖 Создание Telegram-ботов</b> — разработка удобных и эффективных ботов для различных целей.\n"
        "<b>🔍 SEO-оптимизация</b> — повышение видимости вашего сайта в поисковых системах.\n"
        "<b>⚙️ Индивидуальные решения</b> — разработка решений, которые идеально подходят под ваши задачи.\n"
        "<b>📈 Внедрение CRM-систем</b> — мы помогаем интегрировать CRM для оптимизации работы с клиентами и улучшения бизнес-процессов.\n"
        "<b>Свяжитесь с нами, чтобы узнать больше! 📩</b>"
    )

    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=keyboard_markup
    )


@start_functions_private_router.callback_query(F.data == 'payment_terms')
async def payment_terms_callback_query(query: types.CallbackQuery) -> None:
    keyboard_markup = return_functions_keyboard()

    caption_text = (
        "<b>Условия оплаты:</b>\n\n"
        "<b>💳 Способы оплаты:</b>\n"
        "• Банковские карты (Visa, MasterCard, Мир и Mbank)\n"
        "• Электронные кошельки (Qiwi, WebMoney, Яндекс.Деньги)\n\n"

        "<b>📅 Сроки оплаты:</b>\n"
        "• Оплата должна быть произведена в течение 3 рабочих дней после подтверждения заказа.\n"
        "• В случае задержки оплаты заказ может быть отменен.\n\n"

        "<b>💡 Примечания:</b>\n"
        "• Все оплаты считаются окончательными и не подлежат возврату.\n"
        "• Мы предоставляем все необходимые документы для бухгалтерии по запросу.\n\n"

        "<b>🕒 Время работы:</b>\n"
        "• Понедельник — Пятница: 9:00 — 22:00\n"
        "• Воскресенье: выходной\n\n"

        "<b>Свяжитесь с нами для уточнения деталей! 📩</b>"
    )

    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=keyboard_markup
    )


@start_functions_private_router.callback_query(F.data == 'advantages')
async def advantages_callback_query(query: types.CallbackQuery) -> None:
    keyboard_markup = return_functions_keyboard()

    caption_text = (
        "<b>Наши преимущества:</b>\n\n"
        "<b>🚀 Быстрая разработка:</b> Мы обеспечиваем высокую скорость выполнения проектов, не теряя в качестве.\n"
        "<b>💡 Инновационные решения:</b> Мы используем новейшие технологии и подходы для разработки уникальных решений.\n"
        "<b>🤖 Эксперты в Telegram-ботах:</b> Наша команда имеет большой опыт в создании ботов для любых целей.\n"
        "<b>🌐 Разработка сайтов:</b> Мы создаем современные, функциональные и адаптивные сайты для вашего бизнеса.\n"
        "<b>🔒 Безопасность:</b> Мы гарантируем безопасность ваших данных и защищаем ваши проекты от угроз.\n"
        "<b>🌍 Международный опыт:</b> Мы работаем с клиентами по всему миру, предоставляя качественные решения.\n"
        "<b>💬 Поддержка 24/7:</b> Мы всегда готовы помочь и поддерживать ваши проекты на всех этапах.\n\n"
        "<b>Свяжитесь с нами, чтобы узнать больше! 📩</b>"
    )

    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=keyboard_markup
    )


# Обработчик для отображения FAQ
@start_functions_private_router.callback_query(F.data == 'faq')
async def faq_callback_query(query: types.CallbackQuery) -> None:
    caption_text = (
        "<b>Часто задаваемые вопросы:</b>\n\n"
        "Выберите интересующий вас вопрос из списка ниже:"
    )
    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=generate_faq_keyboard()
    )


# Обработчик для ответа на выбранный вопрос
@start_functions_private_router.callback_query(F.data.startswith('faq_'))
async def faq_answer_callback(query: types.CallbackQuery) -> None:
    # Получаем индекс вопроса из callback_data
    index = int(query.data.split('_')[1])
    question = FAQ[index]["question"]
    answer = FAQ[index]["answer"]

    caption_text = f"<b>{question}</b>\n\n{answer}"
    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=return_functions_keyboard()
    )



@start_functions_private_router.callback_query(F.data == 'contact_us')
async def contact_us_callback_query(query: types.CallbackQuery) -> None:
    # Клавиатура с кнопками для связи
    keyboard_markup = contact_us_functions_keyboard()

    # Текст, который будет отображен при нажатии на кнопку
    caption_text = (
        "<b>📞 Свяжитесь с нами!</b>\n\n"
        "Если у вас есть вопросы или предложения, вы можете связаться с нами через следующие каналы:\n\n"
        "<b>WhatsApp</b> \n"
        "<b>Telegram</b> \n"
        "<b>Instagram</b> \n\n"
        "Нажмите кнопку ниже для связи с администратором."
    )

    # Отправка обновленного сообщения с кнопками
    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=keyboard_markup
    )


@start_functions_private_router.callback_query(F.data == "contact_admin")
async def contact_admin_callback_query(query: types.CallbackQuery, bot: Bot):
    """Обработчик callback_query для записи на contact_admin"""

    # Клавиатура для возврата в главное меню
    keyboard_markup = return_functions_keyboard()

    # Сообщение, которое будет отправлено пользователю
    text = "Ваша заявка отправлена нашему менеджеру, он свяжется с вами в ближайшее время. 💬"

    # Обновляем сообщение с кнопками
    await query.message.edit_caption(
        caption=text,
        reply_markup=keyboard_markup
    )

    # Отправляем уведомление пользователю
    await query.answer(text=text)

    # Информация о пользователе
    user_info = f"📝 {query.from_user.first_name}"

    # Добавляем фамилию, если она есть
    if query.from_user.last_name:
        user_info += f" {query.from_user.last_name}"

    # Добавляем username, если он есть
    if query.from_user.username:
        user_info += f" (@{query.from_user.username})"

    # Отправка сообщения администратору
    await bot.send_message(
        chat_id=1850196205,
        text=(
            f"💬 <b>Новая заявка на связь с администратором</b>:\n\n"
            f"👤 <b>Информация о пользователе:</b>\n"
            f"📛 <b>Имя:</b> {user_info}\n"
            f"📲 <b>Контакт пользователя:</b> @{query.from_user.username or 'Не указан'}\n\n"
            f"🔑 <b>Ваши действия:</b>\n"
            f"1. Свяжитесь с пользователем для дальнейшего общения.\n"
        )
    )


@start_functions_private_router.callback_query(F.data == 'useful_features')
async def useful_features_callback_query(query: types.CallbackQuery) -> None:
    keyboard_markup = useful_features_functions_keyboard()

    caption_text = (
        "<b>✨ Полезные функции от Окурмэн Студия</b>\n\n"
        "Откройте для себя уникальные возможности:\n\n"
        "🎶 <b>Создание музыки с ИИ</b> — создайте уникальные треки.\n"
        "📚 <b>Генерация сказок с ИИ</b> — волшебные истории для всех.\n"
        "🤖 <b>Чат с ИИ</b> — общайтесь с умным ассистентом.\n\n"
        "Наслаждайтесь инновациями с  Окурмэн Студия! 🚀"
    )

    # Отправка обновленного сообщения с кнопками
    await query.message.edit_caption(
        caption=caption_text,
        reply_markup=keyboard_markup
    )


@start_functions_private_router.callback_query(F.data == 'our_services')
async def our_services_callback_query(query: types.CallbackQuery, state: FSMContext) -> None:
        keyboard_markup = return_functions_keyboard()

        caption_text = (
            "💼 **Наши услуги**\n\n"
            "🎨 **Дизайн сайтов и приложений**\n"
            "Создаём стильные и удобные интерфейсы, которые привлекают внимание и обеспечивают комфортное использование.\n\n"
            "🌐 **Сайты под ключ**\n"
            "Полный цикл разработки: от идеи до готового сайта, включая дизайн, верстку и программирование.\n\n"
            "📱 **Мобильные приложения**\n"
            "Разработка функциональных приложений для Android и iOS, которые решают задачи вашего бизнеса.\n\n"
            "📍 Мы находимся в Бишкеке и готовы воплотить ваши идеи в жизнь!"
        )

        await query.message.edit_caption(
            caption=caption_text,
            reply_markup=keyboard_markup,
            parse_mode=ParseMode.MARKDOWN
        )

