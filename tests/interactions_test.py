from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


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

    class TestDroppable:

        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'the element has not been dropped'

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here', 'the dropped element has been accepted'
            assert accept == 'Dropped!', 'the dropped element has not been accepted'

        def test_prevent_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, greedy_inner, greedy_outer = droppable_page.drop_prevent()
            assert not_greedy.replace('\n', ' ') == 'Dropped! Dropped!', ('the element has not been dropped to not '
                                                                          'greedy container')
            assert greedy_inner.replace('\n', ' ') == 'Outer droppable Dropped!', ('the element has not been dropped '
                                                                                   'to not greedy inner container')
            assert greedy_outer.replace('\n', ' ') == 'Dropped! Dropped!', ('the element has not been dropped to not '
                                                                            'greedy outer container after inner not '
                                                                            'greedy container')

        def test_revert_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert('will_revert')
            will_not_after_move, will_not_after_revert = droppable_page.drop_revert('will_not_revert')
            assert will_after_move != will_after_revert, 'the element has not revert'
            assert will_not_after_move == will_not_after_revert, 'the element has reverted'

    class TestDraggable:
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            position_before, position_after = draggable_page.simple_drag_box()
            assert position_before != position_after, 'the element position not been changed'

        def test_axis_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            left_x_before, top_x_before, left_x_after, top_x_after = draggable_page.axis_drag_box("only_x")
            left_y_before, top_y_before, left_y_after, top_y_after = draggable_page.axis_drag_box("only_y")
            assert left_x_before != left_x_after and top_x_before == top_x_after, ('the position by x has not changed '
                                                                                   'or position by y has changed')
            assert left_y_before == left_y_after and top_y_before != top_y_after, ('the position by y has not changed '
                                                                                   'or position by x has not changed')

        def test_container_restricted(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            initial_position, final_position, width_position, height_position = draggable_page.container_restricted()
            assert final_position['x'] <= width_position, "Element moved out of the right container boundary"
            assert final_position['y'] <= height_position, "Element moved out of the bottom container boundary"



