from playwright.async_api import Page, Locator


class ProductListPage:
    """Страница списка продуктов (Экспресс-покупка) eshop.sibur.ru.
    Siebel view: SIB ECOM Express Buying Product Search Catalog View.

    Содержит только локаторы. Действия и ожидания — в steps/.
    Шапка, меню и подвал не дублируются — они описаны в MainPage.
    """

    def __init__(self, page: Page) -> None:
        self.page = page

    # --- Секции страницы ---

    @property
    def page_title(self) -> Locator:
        """Заголовок страницы ('Экспресс-покупка')."""
        return self.page.locator(".catalog-header")

    @property
    def content_section(self) -> Locator:
        """Основной контейнер представления списка продуктов."""
        return self.page.locator(".sib-ecom-product-search-view")

    @property
    def filters_sidebar(self) -> Locator:
        """Левый сайдбар с фильтрами (категория, кнопки применить/сбросить)."""
        return self.page.locator(".sib-ecom-product-search-view-content__filter")

    @property
    def results_section(self) -> Locator:
        """Правая область с результатами: переключатели вида и сетка карточек."""
        return self.page.locator(".sib-ecom-product-search-view-content__result")

    @property
    def product_grid(self) -> Locator:
        """Сетка карточек продуктов."""
        return self.page.locator(".sib-ecom-product-grid")

    @property
    def pagination_section(self) -> Locator:
        """Блок пагинации (счётчик и стрелки навигации по страницам)."""
        return self.page.locator(".sib-tile-nav")

    # --- Фильтры ---

    @property
    def category_filter_input(self) -> Locator:
        """Поле-комбобокс выбора категории в сайдбаре фильтров."""
        return self.filters_sidebar.locator(".sib-field__control[role='combobox']")

    @property
    def apply_filter_button(self) -> Locator:
        """Кнопка 'Применить' — применить выбранный фильтр категории."""
        return self.page.locator(".siebui-icon-sibfind")

    @property
    def reset_filter_button(self) -> Locator:
        """Кнопка 'Сбросить фильтры'."""
        return self.page.locator(".siebui-icon-sibreset")

    # --- Переключатели вида ---

    @property
    def view_table_button(self) -> Locator:
        """Кнопка 'Таблицей' — переключить отображение в режим плиток."""
        return self.page.get_by_role("button", name="Таблицей")

    @property
    def view_list_button(self) -> Locator:
        """Кнопка 'Списком' — переключить отображение в режим списка."""
        return self.page.get_by_role("button", name="Списком")

    # --- Карточки продуктов ---

    @property
    def product_cards(self) -> Locator:
        """Коллекция карточек продуктов в сетке."""
        return self.page.locator(".sib-ecom-product-card")

    @property
    def product_name_links(self) -> Locator:
        """Коллекция ссылок-названий продуктов (drilldown в карточку товара)."""
        return self.page.locator(".siebui-ctrl-drilldown.siebui-anchor-readonly")

    @property
    def add_to_cart_buttons(self) -> Locator:
        """Коллекция кнопок 'Купить' (добавить в корзину из экспресс-покупки)."""
        return self.page.locator(".siebui-icon-addtocartexpress")

    @property
    def product_favorites_buttons(self) -> Locator:
        """Коллекция иконок 'Избранное' на карточках продуктов."""
        return self.page.locator(".sib-ecom-product-card-favorites")

    @property
    def product_card_footers(self) -> Locator:
        """Коллекция подвалов карточек (цена + кнопка 'Купить')."""
        return self.page.locator(".sib-ecom-product-card-footer")

    # --- Пагинация ---

    @property
    def pagination_prev_button(self) -> Locator:
        """Кнопка 'Предыдущая страница' в пагинации."""
        return self.page.locator(".sib-tile-nav__prev")

    @property
    def pagination_next_button(self) -> Locator:
        """Кнопка 'Следующая страница' в пагинации."""
        return self.page.locator(".sib-tile-nav__next")
