import unittest

from htmlnode import HTMLNode

class TestTestNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_one_prop(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={"href": "https://www.google.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            tag="a",
            value="Click me",
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
        
    def test_children(self):
        child = HTMLNode(tag="span", value="child text")
        parent = HTMLNode(tag="div", children=[child])
        if parent.children != None:
            self.assertEqual(parent.children[0].value, "child text")

    def test_repr(self):
        node = HTMLNode(
            tag="p",
            value="Hello",
            children=[],
            props={"class": "paragraph"}
        )

        self.assertEqual(
            repr(node),
            "tag=p;\nvalue=Hello;\nchildren=[];\nprops={'class': 'paragraph'}"
        )


if __name__ == "__main__":
    unittest.main()