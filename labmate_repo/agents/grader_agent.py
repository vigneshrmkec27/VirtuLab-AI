# agents/grader_agent.py
class GraderAgent:
    def __init__(self, tools, memory):
        self.tools = tools
        self.memory = memory

    def grade(self, sim_results, expected):
        reported_tau = sim_results.get('time_constant')
        expected_tau = expected.get('time_constant')
        error = abs(reported_tau - expected_tau) / expected_tau if expected_tau else 1.0
        if error < 0.05:
            score = 90
        elif error < 0.15:
            score = 75
        elif error < 0.30:
            score = 60
        else:
            score = 40
        feedback = f"Expected tau={expected_tau:.6f}, simulated tau={reported_tau:.6f}, relative error={error:.3f}"
        return {'score': score, 'feedback': feedback}
