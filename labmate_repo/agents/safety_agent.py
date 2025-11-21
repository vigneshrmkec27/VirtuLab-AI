# agents/safety_agent.py
class SafetyAgent:
    def __init__(self, tools):
        self.tools = tools

    def check(self, experiment_spec):
        issues = []
        params = experiment_spec.get('parameters', {})
        Vin = params.get('Vin', 0)
        if Vin > 50:
            issues.append('Voltage > 50V: Requires lab supervisor and PPE')
        return {'ok': len(issues) == 0, 'issues': issues}
