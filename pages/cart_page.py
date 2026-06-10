from playwright.async_api import Page, Locator


class CartPage:
    """Страница оформления заказа (корзина) eshop.sibur.ru.

    Открывается по клику на иконку корзины (.sib-ecustomer-header-link-cart-info).
    Siebel рендерит содержимое корзины поверх текущего view (overlay).
    Содержит только локаторы. Действия и ожидания — в steps/.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Секции страницы ---

    @property
    def content_section(self) -> Locator:
        """Основной контейнер страницы оформления заказа."""
        return self.page.locator(".checkout")

    @property
    def header(self) -> Locator:
        """Заголовок страницы 'Оформление заказа'."""
        return self.page.locator(".checkout__header")

    @property
    def cart_step(self) -> Locator:
        """Первый шаг оформления — список товаров в корзине."""
        return self.page.locator(".checkout-step").first

    @property
    def cart_step_title(self) -> Locator:
        """Заголовок шага ('Товары в корзине')."""
        return self.page.locator(".checkout-step__title").first

    @property
    def cart_step_content(self) -> Locator:
        """Содержимое шага — список позиций заказа."""
        return self.page.locator(".checkout-step__content").first

    @property
    def aside_summary(self) -> Locator:
        """Боковая панель с итоговой информацией по заказу."""
        return self.page.locator(".checkout__aside")

    # --- Строки товаров ---

    @property
    def cart_items(self) -> Locator:
        """Коллекция строк товаров в корзине."""
        return self.page.locator(".checkout-element")

    @property
    def cart_item_titles(self) -> Locator:
        """Коллекция названий товаров в корзине."""
        return self.page.locator(".checkout-product__title")

    @property
    def cart_item_prices(self) -> Locator:
        """Коллекция цен товаров (числовые значения)."""
        return self.page.locator(".checkout-product__price-value")

    # --- Кнопки управления ---

    @property
    def delete_all_button(self) -> Locator:
        """Кнопка 'Удалить все' — очистить корзину."""
        return self.page.locator(".siebui-icon-sibcartdeleteall")

    @property
    def next_step_button(self) -> Locator:
        """Кнопка 'Далее' — перейти к следующему шагу оформления."""
        return self.page.locator(".checkout-step__next")

    # --- Структура шага ---

    @property
    def checkout_content(self) -> Locator:
        """Обёртка активного шага (внутри .checkout)."""
        return self.page.locator(".checkout__content")

    @property
    def step_header(self) -> Locator:
        """Шапка шага: нумерованный бейдж + заголовок."""
        return self.page.locator(".checkout-step__header").first

    @property
    def step_counter(self) -> Locator:
        """Числовой бейдж номера шага."""
        return self.page.locator(".checkout-step__counter").first

    @property
    def step_footer(self) -> Locator:
        """Подвал шага с кнопкой 'Далее'."""
        return self.page.locator(".checkout-step__footer").first

    # --- Шаг 1: Объёмы и доставка — управление позицией ---

    @property
    def cart_item_delete_buttons(self) -> Locator:
        """Коллекция кнопок удаления отдельных позиций в списке товаров."""
        return self.page.locator(".checkout-step__content button.siebui-icon-sibdeleterecord_dummy")

    @property
    def qty_tons_input(self) -> Locator:
        """Поле ввода объёма в тоннах для позиции."""
        return self.page.locator(".checkout-element__tons input.siebui-ctrl-calc").first

    @property
    def round_qty_button(self) -> Locator:
        """Кнопка 'Округлить' — скруглить объём до кратного вагону."""
        return self.page.locator("button.siebui-icon-sibround").first

    @property
    def special_price_button(self) -> Locator:
        """Кнопка 'Специальная цена' — запросить спецусловия."""
        return self.page.locator("button.checkout-element__special-button").first

    # --- Шаг 1: Условия доставки ---

    @property
    def delivery_section(self) -> Locator:
        """Блок 'Условия доставки' внутри позиции."""
        return self.page.locator(".checkout-element__delivery").first

    @property
    def delivery_supplier_radio(self) -> Locator:
        """Метка 'Доставка поставщиком' (радио)."""
        return self.page.locator(".checkout-element__delivery-type label").filter(has_text="Доставка поставщиком")

    @property
    def delivery_self_pickup_radio(self) -> Locator:
        """Метка 'Самовывоз' (радио)."""
        return self.page.locator(".checkout-element__delivery-type label").filter(has_text="Самовывоз")

    @property
    def transport_type_select(self) -> Locator:
        """Выпадающий список 'Тип транспорта'."""
        return self.page.locator(".checkout-element__address-type input.siebui-ctrl-select").first

    @property
    def delivery_address_section(self) -> Locator:
        """Секция 'Адрес грузополучателя' (контейнер с полем и подсказкой)."""
        return self.page.locator(".checkout-element__address-wrap").first

    # --- Aside: боковая панель прогресса и итогов ---

    @property
    def stepper_section(self) -> Locator:
        """Степпер в aside — навигация по шагам оформления (1–4)."""
        return self.page.locator(".stepper.stepper_checkout")

    @property
    def aside_product_title(self) -> Locator:
        """Название продукта в сводке aside."""
        return self.page.locator(".info-product__title").first

    @property
    def aside_product_delete_button(self) -> Locator:
        """Кнопка удаления продукта из сводки aside."""
        return self.page.locator(".info-product__button .siebui-icon-sibdeleterecord_dummy").first

    @property
    def aside_weight(self) -> Locator:
        """Суммарный вес заказа в aside."""
        return self.page.locator(".values-info__weight").first

    @property
    def aside_total_price(self) -> Locator:
        """Суммарная стоимость заказа в aside."""
        return self.page.locator(".values-info__price").first

    @property
    def add_product_link(self) -> Locator:
        """Ссылка '+ Добавить продукт' в aside."""
        return self.page.locator(".goto-catalog").first

    # --- Шаг 2: Отгрузка — выбор месяца ---

    @property
    def shipment_month_section(self) -> Locator:
        """Блок 'Месяц отгрузки' с описанием и радио-табами."""
        return self.page.locator(".checkout-step__month")

    @property
    def shipment_month_controls(self) -> Locator:
        """Контейнер радио-кнопок выбора месяца (Июнь / Июль / Август...)."""
        return self.page.locator(".checkout-month__controls")

    @property
    def shipment_month_radio_labels(self) -> Locator:
        """Коллекция меток-кнопок выбора месяца отгрузки."""
        return self.page.locator(".checkout-month__controls label.sib-field__label")

    # --- Шаг 2: Отгрузка — календарь распределения ---

    @property
    def shipment_calendar_section(self) -> Locator:
        """Блок с инлайн-календарём распределения объёма по датам."""
        return self.page.locator(".checkout-element__calendar").first

    @property
    def shipment_quantity_remaining(self) -> Locator:
        """Счётчик 'Осталось распределить — N тонн' над календарём."""
        return self.page.locator(".checkout-element__quantity").first

    @property
    def datepicker_section(self) -> Locator:
        """Встроенный датапикер (air-datepicker) для выбора дат отгрузки."""
        return self.page.locator(".air-datepicker_checkout").first

    @property
    def datepicker_nav_title(self) -> Locator:
        """Заголовок месяца/года в навигации датапикера ('Июнь 2026')."""
        return self.page.locator(".air-datepicker-nav--title").first

    @property
    def datepicker_nav_actions(self) -> Locator:
        """Коллекция стрелок навигации по месяцам в датапикере."""
        return self.page.locator(".air-datepicker-nav--action")

    @property
    def datepicker_day_cells(self) -> Locator:
        """Коллекция ячеек-дней в календаре (все, включая disabled)."""
        return self.page.locator(".air-datepicker-cell.-day-")

    @property
    def datepicker_day_ton_inputs(self) -> Locator:
        """Коллекция полей ввода тонн в каждой ячейке дня."""
        return self.page.locator("input.cell-date__ton")

    @property
    def datepicker_day_kg_inputs(self) -> Locator:
        """Коллекция полей ввода килограммов в каждой ячейке дня."""
        return self.page.locator("input.cell-date__kilogram")

    @property
    def product_toggle_button(self) -> Locator:
        """Кнопка сворачивания/разворачивания карточки продукта в календаре."""
        return self.page.locator("button.checkout-product__toggle").first

    # --- Навигация по шагам ---

    @property
    def back_step_button(self) -> Locator:
        """Кнопка 'Назад' — вернуться к предыдущему шагу."""
        return self.page.locator(".checkout-step__cancel").first
