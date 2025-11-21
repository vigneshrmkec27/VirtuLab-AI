# agents/simulator_agent.py
import numpy as np
import matplotlib.pyplot as plt
import os

class SimulatorAgent:
    def __init__(self, tools):
        self.tools = tools

    def run(self, experiment_spec, output_dir='outputs'):
        params = experiment_spec.get('parameters', {})
        R = params.get('R', 10000)
        C = params.get('C', 10e-6)
        Vin = params.get('Vin', 5.0)
        t_end = params.get('t_end', 0.05)
        t = np.linspace(0, t_end, 500)
        tau = R*C
        v_c = Vin*(1 - np.exp(-t/(tau)))
        os.makedirs(output_dir, exist_ok=True)
        plot_path = os.path.join(output_dir, 'rc_charge.png')
        plt.figure()
        plt.plot(t, v_c)
        plt.title('RC Capacitor Charge (simulated)')
        plt.xlabel('time (s)')
        plt.ylabel('Vc (V)')
        plt.grid(True)
        plt.savefig(plot_path)
        plt.close()
        results = {'time': t.tolist(), 'vc': v_c.tolist(), 'plot': plot_path, 'time_constant': tau}
        return results
