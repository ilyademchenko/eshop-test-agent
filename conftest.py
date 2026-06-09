import pytest
from fixtures import browser_instance, context, page, authenticated_page

# Реэкспорт фикстур для pytest
__all__ = ["browser_instance", "context", "page", "authenticated_page"]
