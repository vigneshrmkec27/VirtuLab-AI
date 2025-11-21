def generate_simulation_code(spec):
    code = f"""# Auto-generated simulator for {spec['title']}
import numpy as np
def run_sim(R={spec['parameters']['R']}, C={spec['parameters']['C']}, Vin={spec['parameters']['Vin']}, t_end={spec['parameters']['t_end']}):
    import numpy as np
    t = np.linspace(0, t_end, 500)
    vc = Vin*(1 - np.exp(-t/(R*C)))
    return t, vc
"""
    return code
