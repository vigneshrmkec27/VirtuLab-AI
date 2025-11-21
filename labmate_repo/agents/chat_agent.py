# agents/chat_agent.py
class ChatAgent:
    def __init__(self, tools, memory):
        self.tools = tools
        self.memory = memory

    def answer(self, question, context):
        ctx = context.get('manual_text', '')
        for sentence in ctx.split('.'):
            if any(word.lower() in sentence.lower() for word in question.split()[:2]):
                return {'answer': sentence.strip(), 'sources': ['manual']}
        return {'answer': "I don't know — try asking about 'time constant' or 'RC circuit'.", 'sources': []}
