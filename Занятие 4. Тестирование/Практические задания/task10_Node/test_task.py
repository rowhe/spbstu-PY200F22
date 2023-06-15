import unittest

from task import Node


class TestCase(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(1)  # c помощью метода assertIsNone проверить следующий узел
        self.assertIsNone(node.next)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        node = Node(1)
        node2 = Node(2, node)
        # node.next= node2
        self.assertEqual(node2.next, node)  # проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node(1)
        self.assertEqual(repr(node), f"Node({node.value}, {None})")  # проверить метод __repr__ без следующего узла

    @unittest.skip("skipping")  # пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(1)
        node2 = Node(2, node)
        self.assertEqual(repr(node2), f"Node({node2.value}, Node(1))")

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        self.assertEqual(node.value, 5)
        # проверить строковое представление

    def test_is_valid(self):
         # проверить метод is_valid при корректных узлах
        node = Node(1)
        self.assertTrue(node, (type(None), Node))

        # с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
        nodepo='srt'
        with self.assertRaises(TypeError):
            Node.is_valid(nodepo)
