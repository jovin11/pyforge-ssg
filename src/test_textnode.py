import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url="www.google.com")
        node2 = TextNode("This is a text node", TextType.CODE, url="www.google.com")
        self.assertNotEqual(node, node2)
        self.assertEqual(node.url, node2.url)

    def test_text_type(self):
        node = TextNode("This is a bold text", TextType.BOLD, url="www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, url="www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_representation(self):
        node = TextNode("This is a text node", TextType.BOLD)
        repr = f"TextNode({node.text}, {node.text_type.value}, {node.url})"
        self.assertEqual(node.__repr__(), repr)


if __name__ == "__main__":
    unittest.main()
