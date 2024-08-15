from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


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

    class TestAlerts:
        def test_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alerts()
            assert alert_text == 'You clicked a button', f"Unexpected text: {alert_text}"

        def test_alert_appear_after(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alerts_after()
            assert alert_text == 'This alert appeared after 5 seconds', f"Unexpected text: {alert_text}"

        def test_confirm_box_ok(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            result_text = alert_page.check_confirm_box(confirm=True)
            assert result_text == "You selected Ok", f"Unexpected text: {result_text}"

        def test_confirm_box_cancel(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            result_text = alert_page.check_confirm_box(confirm=False)
            assert result_text == "You selected Cancel", f"Unexpected text: {result_text}"

        def test_prompt_box(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            result_text, name = alert_page.check_prompt_box()
            assert [result_text] == ['You entered ' + name], f"Unexpected text: {result_text}"

    class TestFrames:
        def test_frame(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            frame1 = frame_page.check_frame("frame1")
            frame2 = frame_page.check_frame("frame2")
            assert frame1 == ['This is a sample page', '500px', '350px'], 'frame 1 was not opened'
            assert frame2 == ['This is a sample page', '100px', '100px'], 'frame 2 was not opened'

