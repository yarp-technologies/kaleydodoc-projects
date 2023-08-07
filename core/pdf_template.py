from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class PDFTemplate:
    doc: Any
    regex: Dict = None
    error: str = 0