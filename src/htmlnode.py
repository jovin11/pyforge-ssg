
class HTMLNode:
    
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list | None = None, 
            props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        strout = ""
        for k, v in self.props.items():
            strout += f' {k}="{v}"'
        return strout
    
    def __repr__(self) -> str:
        return f"tag={self.tag};\nvalue={self.value};\nchildren={self.children};\nprops={self.props}"
    
