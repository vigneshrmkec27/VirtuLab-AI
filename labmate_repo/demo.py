# demo.py
import os
from agents.coordinator import Coordinator

def ensure_sample_manual():
    os.makedirs('sample_data', exist_ok=True)
    p = 'sample_data/rc_lab_manual.txt'
    if not os.path.exists(p):
        with open(p, 'w', encoding='utf-8') as f:
            f.write("RC Circuit Lab\nObjective: observe charging behavior of capacitor.\nSteps:\n1. Build RC with R=10k, C=10uF\n2. Apply 5V step.\n3. Measure capacitor voltage vs time.")
    return p

def main():
    manual_path = ensure_sample_manual()
    tools = {}
    mem = {}
    coord = Coordinator(tools, memory=mem)
    input_files = {'manual_path': manual_path}
    student_info = {'id': 'student_001', 'name': 'Demo Student'}
    result = coord.run_lab(input_files, student_info)

    print("=== LabMate Demo Result ===")
    print("Experiment title:", result['experiment']['title'])
    print("Objective:", result['experiment']['objective'])
    print("--- Safety ---")
    print(result['safety'])
    print("--- Simulation plot saved at ---")
    print(result['simulation']['plot'])
    print("--- Grader feedback ---")
    print(result['grade'])
    print("--- Memory snapshot ---")
    print(mem)

if __name__ == '__main__':
    main()
