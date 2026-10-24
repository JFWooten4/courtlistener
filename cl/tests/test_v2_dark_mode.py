from selenium.webdriver.support.ui import WebDriverWait
from waffle.testutils import override_flag

from cl.tests.base import BaseSeleniumTest


@override_flag("use_new_design", active=True)
class NewDesignDarkModeTest(BaseSeleniumTest):
    """The Tailwind/Alpine UI should honor and persist the color preference."""

    def wait_for_mode(self, mode: str) -> None:
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element(
                "tag name", "html"
            ).get_attribute("data-color-mode")
            == mode
        )

    def test_header_toggle_changes_palette_and_persists(self) -> None:
        self.browser.get(self.live_server_url)
        self.browser.execute_script(
            "window.localStorage.setItem('cl-color-mode', 'light');"
        )
        self.browser.refresh()
        self.wait_for_mode("light")

        body = self.browser.find_element("tag name", "body")
        light_background = body.value_of_css_property("background-color")
        toggle = self.browser.find_element(
            "css selector", "[data-theme-toggle]"
        )
        WebDriverWait(self.browser, 10).until(
            lambda browser: toggle.get_attribute("aria-pressed") == "false"
        )
        self.assertEqual(toggle.get_attribute("aria-label"), "Use dark mode")
        toggle.click()

        self.wait_for_mode("dark")
        self.assertEqual(toggle.get_attribute("aria-pressed"), "true")
        self.assertEqual(toggle.get_attribute("aria-label"), "Use light mode")
        self.assertEqual(
            self.browser.execute_script(
                "return window.localStorage.getItem('cl-color-mode');"
            ),
            "dark",
        )
        self.assertNotEqual(
            body.value_of_css_property("background-color"), light_background
        )

        self.browser.refresh()
        self.wait_for_mode("dark")
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element(
                "css selector", "[data-theme-toggle]"
            ).get_attribute("aria-pressed")
            == "true"
        )

    def test_theme_toggle_is_available_in_mobile_header(self) -> None:
        self.browser.set_window_size(375, 812)
        try:
            self.browser.get(self.live_server_url)
            self.browser.execute_script(
                "window.localStorage.setItem('cl-color-mode', 'dark');"
            )
            self.browser.refresh()
            self.wait_for_mode("dark")

            toggle = self.browser.find_element(
                "css selector", "[data-theme-toggle]"
            )
            self.assertTrue(toggle.is_displayed())
            WebDriverWait(self.browser, 10).until(
                lambda browser: toggle.get_attribute("aria-pressed") == "true"
            )
            toggle.click()
            self.wait_for_mode("light")
            self.assertEqual(toggle.get_attribute("aria-label"), "Use dark mode")
        finally:
            self.browser.set_window_size(1024, 768)

    def test_storage_events_synchronize_tabs(self) -> None:
        self.browser.get(self.live_server_url)
        self.browser.execute_script(
            "window.localStorage.setItem('cl-color-mode', 'light');"
        )
        self.browser.refresh()
        self.wait_for_mode("light")
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element(
                "css selector", "[data-theme-toggle]"
            ).get_attribute("aria-pressed")
            == "false"
        )

        self.browser.execute_script(
            """
            window.localStorage.setItem('cl-color-mode', 'dark');
            window.dispatchEvent(new StorageEvent('storage', {
              key: 'cl-color-mode',
              newValue: 'dark',
            }));
            """
        )
        self.wait_for_mode("dark")
        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element(
                "css selector", "[data-theme-toggle]"
            ).get_attribute("aria-pressed")
            == "true"
        )
