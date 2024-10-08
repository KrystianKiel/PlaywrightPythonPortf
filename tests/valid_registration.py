# tests/valid_registration.py
import pytest
from playwright.async_api import async_playwright
from page_objects.registration_page import RegistrationPage

@pytest.mark.asyncio
async def test_registration_email():
    async with async_playwright() as p:
        # Set headless=True to run in background
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        registration_page = RegistrationPage(page)
        # Go to the registration page
        await registration_page.go_to_signup_page()
        # Accept cookies
        await registration_page.accept_cookies()
        # Fill e-mail
        await registration_page.fill_email("portfoliofortests@gmail.com")
        # Click Next
        await registration_page.click_next_button()
        # Fill password
        await registration_page.fill_password("Portfolio132!#")
        # Click Next
        await registration_page.click_next_button()
        # Fill display name
        await registration_page.fill_display_name("Portfolio")
        # Fill day
        await registration_page.fill_day("7")
        # Fill year
        await registration_page.fill_year("1994")
        # Click month button
        await registration_page.select_month(5)
        # Pick gender
        await registration_page.pick_gender(3)
        # Click Next
        await registration_page.click_next_button()
        # Click Term Condition check box
        await registration_page.click_term_condition()
        # Click Registration button
        await registration_page.click_next_button()
        # Wait for screen after registration
        await page.wait_for_selector("//div[contains(@class, "
                                     "'DownloadCta__Content-qizc33-1 "
                                     "cLsytm')]")
        # Close Browser
        await browser.close()
