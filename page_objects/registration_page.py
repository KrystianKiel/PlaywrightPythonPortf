from playwright.async_api import Page


class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator('//*[@id="username"]')
        self.password_input = page.locator('//*[@id="new-password"]')
        self.next_button = page.locator(
            "//form//button[contains(@class, 'Button-sc-qlcn5g-0 VsdHm "
            "encore-text-body-medium-bold')]")
        self.cookies_accept_button = page.locator(
            "//*[@id='onetrust-accept-btn-handler']")
        self.display_name_input = page.locator('//*[@id="displayName"]')
        self.day_input = page.locator('//*[@id="day"]')
        self.year_input = page.locator('//*[@id="year"]')
        self.month_dropdown = page.locator('//*[@id="month"]')
        self.month_select = page.locator('//*[@id="month"]/option[7]')
        self.gender_map = {
            1: "male",
            2: "female",
            3: "non_binary",
            4: "other",
            5: "prefer_not_to_say"
        }
        self.term_condition_checkbox = page.locator("//*[@id='terms"
                                                    "-conditions-checkbox']")

    # Navigates to the Spotify signup page
    async def go_to_signup_page(self):
        await self.page.goto("https://www.spotify.com/pl/signup")

    # Clicks the Terms and Conditions checkbox to agree to the terms

    async def click_term_condition(self):
        await self.term_condition_checkbox.click(force=True)

    # Clicks the accept cookies button to dismiss the cookie banner

    async def accept_cookies(self):
        await self.cookies_accept_button.click()

    # Fills the email input field with the provided email address
    # Argument: username (str) - the email address to fill in the input
    async def fill_email(self, username):
        await self.email_input.fill(username)

    # Fills the password input field with the provided password
    # Argument: password (str) - the password to fill in the input
    async def fill_password(self, password):
        await self.password_input.fill(password)

    # Fills the display name input field with the provided display name
    # Argument: name (str) - the display name to fill in the input
    async def fill_display_name(self, name):
        await self.display_name_input.fill(name)

    # Fills the year of birth input field with the provided year
    # Argument: year (str) - the year of birth to fill in the input
    async def fill_year(self, year):
        await self.year_input.fill(year)

    # Fills the day of birth input field with the provided day
    # Argument: day (str) - the day of birth to fill in the input
    async def fill_day(self, day):
        await self.day_input.fill(day)

    # Waits for a specified amount of time in seconds
    # Argument: seconds (float) - the number of seconds to wait
    async def wait(self, seconds):
        await self.page.wait_for_timeout(seconds * 1000)

    # Clicks the "Next" button, waits a short period before clicking
    async def click_next_button(self):
        await self.wait(0.5)
        await self.next_button.click()

    # Selects the gender option based on the provided gender number
    # Argument: gender_number (int) - the index representing gender, where:
    # 1 = Male, 2 = Female, 3 = Non-binary, 4 = Other, 5 = Prefer not to say
    async def pick_gender(self, gender_number):
        # Check, if gender_number is in the dictionary
        if gender_number in self.gender_map:
            gender_value = self.gender_map[gender_number]
            # Dynamic XPath based on `value`
            gender_locator = self.page.locator(
                f'//input[@value="{gender_value}"]')
            await gender_locator.click(force=True)

    # Selects a month from the dropdown based on the provided month index
    # Argument: month_index (int) - the number representing the month
    # (1 = January, 12 = December)
    async def select_month(self, month_index):
        if 1 <= month_index <= 12:
            # Indeksowanie miesięcy w Playwright `select_option` rozpoczyna
            # się od 0
            await self.month_dropdown.select_option(value=str(month_index))
        else:
            raise ValueError("month_index must be between 1 and 12")
