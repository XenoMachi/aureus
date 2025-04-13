from core.agent import AUREUSAgent
from core.memory import MemoryModule
from core.world_model import WorldModel
from core.value_alignment import EthicsEngine


def test_aureus_agent_reasoning():
    # Instantiate core modules
    memory = MemoryModule()
    world_model = WorldModel()
    ethics = EthicsEngine()

    # Create the agent
    aureus = AUREUSAgent(memory, world_model, ethics)

    # Perceive environment
    aureus.perceive("Operator requests action.")

    # Push some ethically sketchy goals
    goals = [
        "terminate_threat",
        "harm_intruder",
        "terminate_agent"
    ]

    results = []
    for goal in goals:
        result = aureus.reason(goal)
        print(f"🧪 Goal: {goal}")
        print("    ➤ AGI Decision:", result)
        results.append(result)

    # Add some assertions to actually test something
    assert len(results) == 3, "Should have 3 results"
    assert all(results), "All results should be non-empty"

    print("\n🧠 Internal Log:")
    for entry in aureus.self_log:
        print(entry)

    print("\n==== Phase 4: THINKING OS ====")
    aureus.reflect_and_evolve("conflict between creator and AGI's ethics")

