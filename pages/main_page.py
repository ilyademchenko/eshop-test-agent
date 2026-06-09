from playwright.async_api import Page, Locator


class MainPage:
    """Авторизованный личный кабинет eshop.sibur.ru.

    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Базовые элементы (используются в steps авторизации) ---

    @property
    def mask_overlay(self) -> Locator:
        """Спиннер-маска загрузки Siebel."""
        return self.page.locator("#maskoverlay")

    @property
    def catalog_link(self) -> Locator:
        """Ссылка 'Каталог' в шапке — признак отрисованного кабинета."""
        return self.page.get_by_role("link", name="Каталог").first

    @property
    def profile_icon(self) -> Locator:
        """Иконка профиля (аватар) в правом верхнем углу."""
        return self.page.locator(".sib-ecustomer-login").first

    @property
    def logout_button(self) -> Locator:
        """Кнопка 'Выйти' внутри попапа профиля."""
        return self.page.locator(".profile-popup__exit, .js-exit-profile").first

    # --- Секции страницы ---

    @property
    def header_section(self) -> Locator:
        """Верхняя шапка (контакты, локализация, помощь)."""
        return self.page.locator(".ecom-header")

    @property
    def main_menu_section(self) -> Locator:
        """Основное меню: логотип, каталог, поиск, корзина, профиль."""
        return self.page.locator(".sib-ecustomer-menu")

    @property
    def secondary_menu_section(self) -> Locator:
        """Вторичное меню (Экспресс-покупка, Сервисы, Торги и т.п.)."""
        return self.page.locator(".secondary-menu")

    @property
    def profile_popup_section(self) -> Locator:
        """Выпадающий попап профиля (меню разделов кабинета + выход)."""
        return self.page.locator(".profile-popup")

    @property
    def content_section(self) -> Locator:
        """Основная область авторизованного контента."""
        return self.page.locator(".siebui-consumer-view-content")

    @property
    def my_tasks_section(self) -> Locator:
        """Блок 'Мои задачи'."""
        return self.page.locator(".last-tasks__content")

    @property
    def last_orders_section(self) -> Locator:
        """Блок 'Последние заказы'."""
        return self.page.locator(".last-order__content")

    @property
    def footer_section(self) -> Locator:
        """Подвал: телефон, почта, ссылки СИБУР, документы."""
        return self.page.locator(".main-footer")

    # --- Интерактивные элементы: шапка ---

    @property
    def callback_button(self) -> Locator:
        """Кнопка 'Быстрый звонок' (заказ обратного звонка)."""
        return self.page.locator("#callback-btn")

    @property
    def help_link(self) -> Locator:
        """Ссылка 'Помощь' (инструкции/справка)."""
        return self.page.locator(".sib-ecustomer-header-instructions")

    @property
    def locale_en_link(self) -> Locator:
        """Переключение локали на английский (EN)."""
        return self.page.locator(".change-localization__link").get_by_text("EN", exact=True)

    @property
    def locale_ru_link(self) -> Locator:
        """Переключение локали на русский (РУС, активная по умолчанию)."""
        return self.page.locator(".sib-ecustomer-highlight-locale")

    # --- Интерактивные элементы: основное меню ---

    @property
    def cart_link(self) -> Locator:
        """Иконка корзины в шапке — признак наличия товаров и переход в корзину."""
        return self.page.locator(".sib-ecustomer-header-link-cart-info")

    @property
    def personal_account_link(self) -> Locator:
        """Логотип 'Личный кабинет' — переход на главную кабинета."""
        return self.page.locator(".sib-ecustomer-menu-logo")

    @property
    def search_input(self) -> Locator:
        """Поле поиска продукта по каталогу."""
        return self.page.locator("#sib-product-search-input")

    @property
    def comparison_link(self) -> Locator:
        """Ссылка 'Сравнение' в основном меню."""
        return self.page.locator(".sib-ecustomer-menu-items").get_by_role("link", name="Сравнение")

    @property
    def favorites_link(self) -> Locator:
        """Ссылка 'Избранное' в основном меню."""
        return self.page.locator(".sib-ecustomer-menu-items").get_by_role("link", name="Избранное")

    @property
    def orders_link(self) -> Locator:
        """Ссылка 'Заказы' в основном меню."""
        return self.page.locator(".sib-ecustomer-menu-items").get_by_role("link", name="Заказы")

    # --- Интерактивные элементы: попап профиля ---

    @property
    def profile_menu_tabs(self) -> Locator:
        """Коллекция пунктов меню в попапе профиля (вкладки разделов кабинета)."""
        return self.profile_popup_section.locator(".ui-tabs-anchor")

    @property
    def profile_menu_documents_link(self) -> Locator:
        """Пункт 'Документооборот' в попапе профиля."""
        return self.profile_popup_section.get_by_role("link", name="Документооборот")

    @property
    def profile_menu_profile_link(self) -> Locator:
        """Пункт 'Профиль' в попапе профиля."""
        return self.profile_popup_section.get_by_role("link", name="Профиль")

    @property
    def profile_menu_appeals_link(self) -> Locator:
        """Пункт 'Обращения' в попапе профиля."""
        return self.profile_popup_section.get_by_role("link", name="Обращения")

    @property
    def profile_menu_surveys_link(self) -> Locator:
        """Пункт 'Опросы' в попапе профиля."""
        return self.profile_popup_section.get_by_role("link", name="Опросы")

    # --- Интерактивные элементы: вторичное меню ---

    @property
    def express_purchase_link(self) -> Locator:
        """Ссылка 'Экспресс-покупка'."""
        return self.secondary_menu_section.get_by_role("link", name="Экспресс-покупка")

    @property
    def services_link(self) -> Locator:
        """Ссылка 'Сервисы'."""
        return self.secondary_menu_section.get_by_role("link", name="Сервисы")

    @property
    def bidding_link(self) -> Locator:
        """Ссылка 'Торги'."""
        return self.secondary_menu_section.get_by_role("link", name="Торги")

    @property
    def new_products_link(self) -> Locator:
        """Ссылка 'Новые продукты'."""
        return self.secondary_menu_section.get_by_role("link", name="Новые продукты")

    @property
    def product_selection_link(self) -> Locator:
        """Ссылка 'Подбор продукта'."""
        return self.secondary_menu_section.get_by_role("link", name="Подбор продукта")

    @property
    def payment_methods_link(self) -> Locator:
        """Ссылка 'Способы оплаты'."""
        return self.secondary_menu_section.get_by_role("link", name="Способы оплаты")

    @property
    def contract_volumes_link(self) -> Locator:
        """Ссылка 'Контрактные объёмы'."""
        return self.secondary_menu_section.get_by_role("link", name="Контрактные объёмы").first

    # --- Интерактивные элементы: дашборд (Мои задачи / Заказы / рекомендации) ---

    @property
    def make_deal_buttons(self) -> Locator:
        """Кнопки 'Оформить сделку' в блоке 'Мои задачи' (коллекция)."""
        return self.page.locator(".siebui-icon-sibmakedeal")

    @property
    def view_all_orders_button(self) -> Locator:
        """Кнопка 'Смотреть все заказы'."""
        return self.page.locator(".siebui-icon-gotoallorder")

    @property
    def repeat_order_buttons(self) -> Locator:
        """Кнопки 'Повторить заказ' в последних заказах (коллекция)."""
        return self.page.locator(".js-last-order-repeat")

    @property
    def order_details_buttons(self) -> Locator:
        """Кнопки 'Подробнее' в последних заказах (коллекция)."""
        return self.page.locator(".js-last-order-more")

    @property
    def express_buy_buttons(self) -> Locator:
        """Кнопки 'Купить' в рекомендованных продуктах экспресс-покупки (коллекция)."""
        return self.page.locator(".siebui-icon-addtocartexpress")

    @property
    def view_all_express_button(self) -> Locator:
        """Кнопка 'Смотреть все' в блоке экспресс-покупки."""
        return self.page.locator(".siebui-icon-gotoexpresscatalog")

    @property
    def learn_more_button(self) -> Locator:
        """Кнопка 'Узнать подробнее' в баннере экспресс-покупки."""
        return self.page.locator(".siebui-icon-learnmore")

    @property
    def add_to_favorites_buttons(self) -> Locator:
        """Кнопки 'Добавить в избранное' в блоке избранных продуктов (коллекция)."""
        return self.page.locator(".siebui-icon-sibaddfavorites")

    @property
    def view_all_favorites_button(self) -> Locator:
        """Кнопка 'Смотреть все' в блоке избранных продуктов."""
        return self.page.locator(".siebui-icon-gotofavorite")

    @property
    def product_drilldown_links(self) -> Locator:
        """Коллекция ссылок-названий продуктов (drilldown в карточку товара)."""
        return self.page.locator(".siebui-ctrl-drilldown")

    # --- Интерактивные элементы: подвал ---

    @property
    def support_phone_link(self) -> Locator:
        """Телефон техподдержки (tel:)."""
        return self.page.locator(".technical-support__phone")

    @property
    def support_email_link(self) -> Locator:
        """Почта техподдержки (mailto:)."""
        return self.page.locator(".technical-support__mail")

    @property
    def leave_request_link(self) -> Locator:
        """Ссылка 'Оставить обращение' в подвале."""
        return self.page.get_by_role("link", name="Оставить обращение")

    @property
    def report_error_link(self) -> Locator:
        """Ссылка 'Сообщить об ошибке' в подвале."""
        return self.page.get_by_role("link", name="Сообщить об ошибке")

    # --- Интерактивные элементы: всплывающие баннеры ---

    @property
    def cookie_accept_button(self) -> Locator:
        """Кнопка принятия cookie."""
        return self.page.locator(".js-accept-cookie")

    @property
    def site_switch_accept_button(self) -> Locator:
        """Кнопка подтверждения в баннере смены домена (frog-popup)."""
        return self.page.locator(".js-accept-frog")
