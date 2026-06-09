from playwright.async_api import Page, expect

from config import settings
from pages import GuestPage, LoginPage, MainPage
from test_data import DEFAULT_USER_ALIAS, get_user

# expect-проверки используют собственный дефолтный таймаут (5с),
# не зависящий от page.set_default_timeout — поднимаем под медленный Siebel.
expect.set_options(timeout=settings.NAVIGATION_TIMEOUT)


class AuthSteps:
    """Шаги сценария авторизации: обращения к локаторам, ожидания и проверки.

    Siebel шлёт фоновые XHR непрерывно — networkidle недостижим,
    поэтому ждём конкретные элементы DOM и исчезновение спиннера-маски.
    """

    def __init__(self, page: Page) -> None:
        self.page = page
        self.guest_page = GuestPage(page)
        self.login_page = LoginPage(page)
        self.main_page = MainPage(page)
        self.page.set_default_timeout(settings.NAVIGATION_TIMEOUT)

    # --- Вспомогательные ожидания ---

    async def wait_spinner_gone(self) -> None:
        """Ждёт исчезновения спиннера-маски Siebel (если он есть)."""
        try:
            await self.main_page.mask_overlay.wait_for(
                state="hidden", timeout=settings.NAVIGATION_TIMEOUT
            )
        except Exception:
            pass  # маска могла уже исчезнуть или отсутствовать

    # --- Шаги ---

    async def open_site(self) -> None:
        """Открыть стартовую страницу и проверить наличие ссылки 'Войти'."""
        await self.page.goto(
            settings.BASE_URL, wait_until="load", timeout=settings.NAVIGATION_TIMEOUT
        )
        await expect(self.guest_page.enter_link).to_be_visible()

    async def go_to_login_form(self) -> None:
        """Перейти к форме логина и дождаться её появления."""
        # Клик инициирует медленную навигацию Siebel — не ждём её авто-завершения
        await self.guest_page.enter_link.click(no_wait_after=True)
        await expect(self.login_page.login_input).to_be_visible()

    async def fill_credentials(self, login: str, password: str) -> None:
        """Заполнить поля логина и пароля."""
        await self.login_page.login_input.fill(login)
        await self.login_page.password_input.fill(password)
        await expect(self.login_page.login_input).to_have_value(login)

    async def fill_credentials_from_settings(self, alias: str = DEFAULT_USER_ALIAS) -> None:
        """Заполнить поля логина и пароля данными пользователя по алиасу из test_data."""
        user = get_user(alias)
        await self.fill_credentials(user.login, user.password)

    async def accept_checkboxes_if_present(self) -> None:
        """Отметить чекбоксы капчи и согласия, если они отображаются."""
        if await self.login_page.captcha_checkbox.is_visible():
            await self.login_page.captcha_checkbox.check()
        if await self.login_page.consent_checkbox.is_visible():
            await self.login_page.consent_checkbox.check()

    async def submit_login(self) -> None:
        """Нажать кнопку 'Вход'."""
        await self.login_page.submit_button.click(no_wait_after=True)

    async def assert_logged_in(self) -> None:
        """Проверить успешный вход: форма исчезла, спиннер ушёл, шапка отрисована."""
        await self.login_page.login_input.wait_for(
            state="hidden", timeout=settings.NAVIGATION_TIMEOUT
        )
        await self.wait_spinner_gone()
        await expect(self.main_page.catalog_link).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )

    async def logout(self) -> None:
        """Выйти по клику: иконка профиля -> кнопка 'Выйти' в попапе."""
        await self.wait_spinner_gone()
        await expect(self.main_page.profile_icon).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )
        await self.main_page.profile_icon.click()

        await expect(self.main_page.logout_button).to_be_visible(
            timeout=settings.NAVIGATION_TIMEOUT
        )
        await self.main_page.logout_button.click(no_wait_after=True)

    async def assert_logged_out(self) -> None:
        """Проверить успешный выход: иконка профиля пропала."""
        await expect(self.main_page.profile_icon).to_be_hidden(
            timeout=settings.NAVIGATION_TIMEOUT
        )

    # --- Композитный шаг ---

    async def login(self, alias: str = DEFAULT_USER_ALIAS) -> None:
        """Полный сценарий входа пользователем по алиасу до проверки кабинета."""
        await self.open_site()
        await self.go_to_login_form()
        await self.fill_credentials_from_settings(alias)
        await self.accept_checkboxes_if_present()
        await self.submit_login()
        await self.assert_logged_in()
