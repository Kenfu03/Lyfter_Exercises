class Movement:
    def __init__(self, title: str, amount: float, category: str, date: str, movement_type: str):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        self.movement_type = movement_type

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "movement_type": self.movement_type,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data.get("title", ""),
            amount=float(data.get("amount", 0)),
            category=data.get("category", ""),
            date=data.get("date", ""),
            movement_type=data.get("movement_type", ""),
        )
