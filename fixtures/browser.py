import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from config import settings


@pytest.fixture
async def browser_instance():
    async with async_playwright() as pw:
        browser_type = getattr(pw, settings.BROWSER)
        browser: Browser = await browser_type.launch(
            headless=settings.HEADLESS,
            slow_mo=settings.SLOW_MO,
            args=["--start-maximized"],
        )
        yield browser
        await browser.close()


@pytest.fixture
async def context(browser_instance: Browser):
    ctx: BrowserContext = await browser_instance.new_context(
        viewport={"width": settings.VIEWPORT_WIDTH, "height": settings.VIEWPORT_HEIGHT},
        base_url=settings.BASE_URL,
        locale="ru-RU",
        timezone_id="Europe/Moscow",
        record_video_dir=str(settings.ROOT_DIR / "videos") if not settings.HEADLESS else None,
    )
    ctx.set_default_timeout(settings.DEFAULT_TIMEOUT)
    ctx.set_default_navigation_timeout(settings.NAVIGATION_TIMEOUT)
    yield ctx
    await ctx.close()


@pytest.fixture
async def page(context: BrowserContext) -> Page:
    pg = await context.new_page()
    yield pg
    await pg.close()


@pytest.fixture
async def authenticated_page(page: Page):
    """Страница с уже выполненной авторизацией (пользователь «КЗДТ»)."""
    from steps import AuthSteps
    steps = AuthSteps(page)
    await steps.login()
    yield page
