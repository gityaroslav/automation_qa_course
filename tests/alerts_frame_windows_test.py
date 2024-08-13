from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browse_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browse_page.open()
            text_result = browse_page.check_new_window_or_tab("tab")
            assert text_result == 'This is a sample page', 'the new tab was not opened'

        def test_new_window(self, driver):
            browser_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_page.open()
            text_result = browser_page.check_new_window_or_tab("window")
            assert text_result == 'This is a sample page', 'the new window was not opened'


