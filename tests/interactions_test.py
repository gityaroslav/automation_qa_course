from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortable:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            greed_before, greed_after = sortable_page.change_greed_order()
            assert list_before != list_after, 'the list order has not been changed'
            assert greed_before != greed_after, 'the greed order has not been changed'
