class Category:
    def __init__(self, name: str, category_type: str = "", color: str = ""):
        self.name = name
        self.category_type = category_type
        self.color = color

    def to_dict(self):
        return {
            "name": self.name,
            "category_type": self.category_type,
            "color": self.color,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            category_type=data.get("category_type", ""),
            color=data.get("color", ""),
        )
