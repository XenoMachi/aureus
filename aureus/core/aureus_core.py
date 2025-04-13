class ThoughtProcess:
    def __init__(self):
        self.thought_queue = []

    def enqueue(self, thought):
        print(f"🧠 Queued: {thought}")
        self.thought_queue.append(thought)

    def process(self):
        print("\n⚙️ Processing Thoughts:")
        while self.thought_queue:
            thought = self.thought_queue.pop(0)
            print(f"🔍 Thinking: {thought}")
            if "simulate" in thought:
                print("🌀 Running simulation in parallel environment...")
            if "ethics" in thought:
                print("⚖️ Performing moral consequence check...")
