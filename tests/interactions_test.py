from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortable:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            greed_before, greed_after = sortable_page.change_greed_order()
            assert list_before != list_after, 'the list order has not been changed'
            assert greed_before != greed_after, 'the greed order has not been changed'

    class TesteSelectable:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selected_list_items = selectable_page.select_list_items()
            list_result = selectable_page.check_selected_list_items()
            selected_greed_items = selectable_page.select_greed_items()
            greed_result = selectable_page.check_selected_greed_items()
            assert sorted(selected_greed_items) == sorted(
                greed_result), 'the list elements has not been selected correctly'
            assert sorted(selected_list_items) == sorted(
                list_result), 'the list elements has not been selected correctly'

    class TestResizable:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizeable_box()
            max_resizeable, min_resizeable = resizable_page.change_size_resizeable()
            assert max_box == ('500px', '300px')
            assert min_box == ('150px', '150px')
            assert min_resizeable != max_resizeable

