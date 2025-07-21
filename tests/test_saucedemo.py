from playwright.sync_api import Page
import pytest

def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

