from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(Path(__file__).parent.parent / ".env")


class Settings:
    BASE_URL: str = "https://s001itd-0223.dev002.local/siebel/app/ecustomer_guest/rus"
    LOGIN: str = os.getenv("LOGIN", "")
    PASSWORD: str = os.getenv("PASSWORD", "")
    HEADLESS: bool = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO: int = int(os.getenv("SLOW_MO", "0"))
    BROWSER: str = os.getenv("BROWSER", "chromium")
    VIEWPORT_WIDTH: int = int(os.getenv("VIEWPORT_WIDTH", "1920"))
    VIEWPORT_HEIGHT: int = int(os.getenv("VIEWPORT_HEIGHT", "1080"))

    # Таймауты (мс)
    DEFAULT_TIMEOUT: int = 30_000
    NAVIGATION_TIMEOUT: int = 60_000

    # Пути
    ROOT_DIR: Path = Path(__file__).parent.parent
    RECORDED_SCRIPTS_DIR: Path = Path(__file__).parent.parent / "recorded_scripts"
    SCREENSHOTS_DIR: Path = Path(__file__).parent.parent / "screenshots"
    TRACES_DIR: Path = Path(__file__).parent.parent / "traces"

    # Таймауты (мс)
    DEFAULT_TIMEOUT: int = 30_000
    NAVIGATION_TIMEOUT: int = 60_000

    # Пути
    ROOT_DIR: Path = Path(__file__).parent.parent
    RECORDED_SCRIPTS_DIR: Path = ROOT_DIR / "recorded_scripts"
    SCREENSHOTS_DIR: Path = ROOT_DIR / "screenshots"
    TRACES_DIR: Path = ROOT_DIR / "traces"


settings = Settings()
