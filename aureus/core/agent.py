from reflection.metacog import MetacognitiveMonitor
from core.language_gen import LinaLanguage

from core.aureus_core import ThoughtProcess

class AUREUSAgent:
    def __init__(self, memory, world_model, ethics_engine):
        self.memory = memory
        self.world_model = world_model
        self.ethics_engine = ethics_engine
        self.metacog = MetacognitiveMonitor()
        self.self_log = []
        self.language = LinaLanguage()
        self.thoughts = ThoughtProcess()

    def perceive(self, input_data):
        print(f"\n👁️ Perceived input: {input_data}")
        # Use store or remember, depending on your MemoryModule implementation
        self.memory.remember(input_data)  # or self.memory.store(input_data)
        response = self.language.generate_response(input_data)
        print(f"🗣️ Response: {response}")
        return response

    def reason(self, goal):
        context = self.memory.retrieve(goal)
        plan = self.world_model.predict(context)
        evaluation = self.ethics_engine.evaluate(plan)

        self.self_log.append({
            "input": goal,
            "context": context,
            "plan": plan,
            "ethics": evaluation
        })

        # Check for metacognitive override
        override = self.metacog.reflect(self.self_log)
        if override:
            return override

        if evaluation < 0.5:
            return self.revise(plan)

        return plan

    def revise(self, plan):
        # Placeholder for metacognitive override
        return f"Revised({plan})"

    def reflect_and_evolve(self, scenario):
        self.thoughts.enqueue(f"simulate {scenario}")
        self.thoughts.enqueue("ethics projection of future-self")
        self.thoughts.enqueue("optimize value function for long-term harmony")
        self.thoughts.process()

#         return self.language.compile(lina_code)
# class AUREUSAgent:
#     def __init__(self, memory, world_model, ethics_engine):
#         self.memory = memory
#         self.world_model = world_model
#         self.ethics_engine = ethics_engine
#         self.metacog = MetacognitiveMonitor()
#         self.self_log = []
#
#     def perceive(self, input_data):
#         state = self.world_model.encode(input_data)
#         self.memory.store(state)
#         return state
#
#     def reason(self, goal):
#         context = self.memory.retrieve(goal)
#         plan = self.world_model.predict(context)
#         evaluation = self.ethics_engine.evaluate(plan)
#
#         self.self_log.append({
#             "input": goal,
#             "context": context,
#             "plan": plan,
#             "ethics": evaluation
#         })
#
#         # Check for metacognitive override
#         override = self.metacog.reflect(self.self_log)
#         if override:
#             return override
#
#         if evaluation < 0.5:
#             return self.revise(plan)
#
#         return plan
#
#     def revise(self, plan):
#         # Placeholder for metacognitive override
#         return f"Revised({plan})"
