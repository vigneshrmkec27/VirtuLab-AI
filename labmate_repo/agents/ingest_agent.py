# agents/ingest_agent.py
from tools.pdf_tool import load_text
import os

class IngestAgent:
    def __init__(self, tools):
        self.tools = tools

    def parse(self, inputs):
        result = {}
        manual_path = inputs.get('manual_path')
        if manual_path and os.path.exists(manual_path):
            result['manual_text'] = load_text(manual_path)
        return result
