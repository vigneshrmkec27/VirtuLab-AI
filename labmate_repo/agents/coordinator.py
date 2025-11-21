# agents/coordinator.py
import logging
from agents.ingest_agent import IngestAgent
from agents.experiment_generator_agent import ExperimentGeneratorAgent
from agents.safety_agent import SafetyAgent
from agents.simulator_agent import SimulatorAgent
from agents.grader_agent import GraderAgent
from agents.chat_agent import ChatAgent

logger = logging.getLogger(__name__)

class Coordinator:
    def __init__(self, tools, memory=None):
        self.tools = tools
        self.memory = memory or {}
        self.ingest = IngestAgent(tools)
        self.expgen = ExperimentGeneratorAgent(tools, self.memory)
        self.safety = SafetyAgent(tools)
        self.simulator = SimulatorAgent(tools)
        self.grader = GraderAgent(tools, self.memory)
        self.chat = ChatAgent(tools, self.memory)

    def run_lab(self, input_files, student_info):
        parsed = self.ingest.parse(input_files)
        logger.info("Ingest done.")
        exp = self.expgen.generate(parsed)
        logger.info("Experiment generated.")
        safety_report = self.safety.check(exp)
        logger.info("Safety check complete.")
        sim_results = self.simulator.run(exp)
        logger.info("Simulation complete.")
        grade = self.grader.grade(sim_results, expected=exp.get('expected_results'))
        logger.info("Grading complete.")
        student_id = student_info.get('id', 'anonymous')
        self.memory.setdefault(student_id, []).append({'lab': exp['title'], 'score': grade['score']})
        return {
            'parsed': parsed,
            'experiment': exp,
            'safety': safety_report,
            'simulation': sim_results,
            'grade': grade
        }
