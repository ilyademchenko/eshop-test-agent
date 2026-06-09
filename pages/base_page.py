from playwright.async_api import Page, Locator, expect
from config import settings


class BasePage:
    """Базовый класс для всех Page Object — общие методы навигации и взаимодействия."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = settings.BASE_URL

    async def navigate(self, path: str = "") -> None:
        await self.page.goto(f"{self.base_url}{path}")
        await self.page.wait_for_load_state("networkidle")

    async def wait_for_url(self, pattern: str) -> None:
        await self.page.wait_for_url(f"**{pattern}**")

    async def get_title(self) -> str:
        return await self.page.title()

    async def take_screenshot(self, name: str) -> None:
        path = settings.ROOT_DIR / "screenshots" / f"{name}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        await self.page.screenshot(path=str(path), full_page=True)

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    async def fill(self, selector: str, value: str) -> None:
        await self.page.locator(selector).fill(value)

    async def click(self, selector: str) -> None:
        await self.page.locator(selector).click()

    async def is_visible(self, selector: str) -> bool:
        return await self.page.locator(selector).is_visible()

    async def get_text(self, selector: str) -> str:
        return (await self.page.locator(selector).text_content()) or ""

    async def expect_visible(self, selector: str) -> None:
        await expect(self.page.locator(selector)).to_be_visible()

    async def expect_url_contains(self, substring: str) -> None:
        await expect(self.page).to_have_url(f"**{substring}**")
