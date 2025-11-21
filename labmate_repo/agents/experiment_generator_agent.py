# agents/experiment_generator_agent.py
from tools.codegen_tool import generate_simulation_code

class ExperimentGeneratorAgent:
    def __init__(self, tools, memory):
        self.tools = tools
        self.memory = memory

    def generate(self, parsed):
        manual = parsed.get('manual_text', '')
        lines = [l.strip() for l in manual.splitlines() if l.strip()]
        title = lines[0] if lines else 'Untitled Lab'
        objective = lines[1] if len(lines) > 1 else 'Study the system.'
        spec = {
            'title': title,
            'objective': objective,
            'steps': [
                'Assemble RC circuit with R=10kΩ, C=10μF',
                'Apply a step voltage of 5V at t=0',
                'Measure voltage across capacitor vs time'
            ],
            'parameters': {'R': 10000, 'C': 10e-6, 'Vin': 5.0, 't_end': 0.05},
        }
        R = spec['parameters']['R']
        C = spec['parameters']['C']
        tau = R*C
        spec['expected_results'] = {'time_constant': tau, 'expected_behavior': 'exponential charge with tau=R*C'}
        sim_code = generate_simulation_code(spec)
        spec['sim_code'] = sim_code
        return spec
