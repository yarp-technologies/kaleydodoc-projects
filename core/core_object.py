from typing import Dict, Any
from .docx_template_placeholder import DocxTemplatePlaceholder


class Core:

    def __init__(self, file: Any, regex: Dict):
        self.template = file
        self.tags = regex

    def process(self):
        return DocxTemplatePlaceholder(self.template, self.tags).process()
