from dataclasses import dataclass, asdict


@dataclass
class User:
    tg_id: str
    username: str
    last_pc: int = None
    last_pc_date: str = None
    last_ps: int = None
    last_ps_date: str = None

    def to_dict(self):
        return asdict(self)
