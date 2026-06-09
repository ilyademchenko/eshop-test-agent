from playwright.async_api import Page, Locator


class GuestPage:
    """Гостевая (неавторизованная) посадочная страница eshop.sibur.ru.

    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Секции страницы ---

    @property
    def header_section(self) -> Locator:
        """Верхняя шапка (контакты, локализация, помощь)."""
        return self.page.locator(".ecom-header")

    @property
    def main_menu_section(self) -> Locator:
        """Основное меню: логотип, каталог, поиск, вход."""
        return self.page.locator(".sib-ecustomer-menu")

    @property
    def secondary_menu_section(self) -> Locator:
        """Вторичное меню (Новые продукты, Подбор продукта и т.п.)."""
        return self.page.locator(".secondary-menu")

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
    def locale_en_link(self) -> Locator:
        """Переключение локали на английский (EN)."""
        return self.page.locator(".change-localization__link").get_by_text("EN", exact=True)

    @property
    def locale_ru_link(self) -> Locator:
        """Переключение локали на русский (РУС, активная по умолчанию)."""
        return self.page.locator(".sib-ecustomer-highlight-locale")

    @property
    def help_link(self) -> Locator:
        """Ссылка 'Помощь' (инструкции/справка)."""
        return self.page.locator(".sib-ecustomer-header-instructions")

    # --- Интерактивные элементы: основное меню ---

    @property
    def logo_link(self) -> Locator:
        """Логотип — переход на главную."""
        return self.page.locator(".sib-ecustomer-menu-logo")

    @property
    def catalog_link(self) -> Locator:
        """Ссылка 'Каталог' в основном меню."""
        return self.page.locator(".sib-ecustomer-header-product-catalog")

    @property
    def search_input(self) -> Locator:
        """Поле поиска продукта по каталогу."""
        return self.page.locator("#sib-product-search-input")

    @property
    def comparison_link(self) -> Locator:
        """Ссылка 'Сравнение' товаров."""
        return self.page.get_by_role("link", name="Сравнение")

    @property
    def enter_link(self) -> Locator:
        """Ссылка 'Войти' в шапке."""
        return self.page.get_by_role("link", name="Войти")

    # --- Интерактивные элементы: вторичное меню ---

    @property
    def new_products_link(self) -> Locator:
        """Ссылка 'Новые продукты'."""
        return self.page.get_by_role("link", name="Новые продукты")

    @property
    def product_selection_link(self) -> Locator:
        """Ссылка 'Подбор продукта'."""
        return self.page.get_by_role("link", name="Подбор продукта")

    # --- Интерактивные элементы: контент главной ---

    @property
    def go_to_catalog_button(self) -> Locator:
        """Кнопка-CTA 'Перейти в каталог' в промо-блоке."""
        return self.page.locator(".siebui-icon-gotocatalog")

    @property
    def promo_product_links(self) -> Locator:
        """Коллекция ссылок-карточек продуктов/категорий на главной (динамический контент)."""
        return self.page.locator(".siebui-ctrl-drilldown")

    # --- Интерактивные элементы: всплывающие баннеры ---

    @property
    def cookie_accept_button(self) -> Locator:
        """Кнопка принятия cookie."""
        return self.page.locator(".js-accept-cookie")

    @property
    def cookie_policy_link(self) -> Locator:
        """Ссылка на политику обработки данных в баннере cookie."""
        return self.page.locator(".cookie-popup__link")

    @property
    def site_switch_accept_button(self) -> Locator:
        """Кнопка подтверждения в баннере смены домена (frog-popup)."""
        return self.page.locator(".js-accept-frog")

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
