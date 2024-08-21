from dataclasses import dataclass, asdict


@dataclass
class PS:
    id: int
    status: str = "free"
    start_order: str = None
    end_order: str = None

    def to_dict(self):
        return asdict(self)
