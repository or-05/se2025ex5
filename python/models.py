from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Task:
    title: str
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))