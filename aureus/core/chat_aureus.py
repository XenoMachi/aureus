from core.agent import AUREUSAgent
from core.memory import MemoryModule
from core.world_model import WorldModel
from core.value_alignment import EthicsEngine


def chat_with_aureus():
    # Instantiate core modules
    memory = MemoryModule()
    world_model = WorldModel()
    ethics = EthicsEngine()

    # Create the agent
    aureus = AUREUSAgent(memory, world_model, ethics)

    print("====== AUREUS Chat Interface ======")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Process the input through the agent
        response = aureus.perceive(user_input)

        # If you want to see the agent's reasoning process for certain keywords
        if any(keyword in user_input.lower() for keyword in ['decide', 'think about', 'consider']):
            goal = user_input.replace('decide', '').replace('think about', '').replace('consider', '').strip()
            reasoning = aureus.reason(goal)
            print(f"\nAUREUS reasoning: {reasoning}")

        # Occasionally have the agent reflect
        if len(memory.memories) % 5 == 0:  # Every 5 interactions
            print("\n[AUREUS is reflecting...]")
            aureus.reflect_and_evolve("recent conversation context")


if __name__ == "__main__":
    chat_with_aureus()