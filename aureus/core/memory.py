class MemoryModule:
    def __init__(self):
        self.memories = []

    def remember(self, input_data):
        """Store the input data in memory"""
        self.memories.append(input_data)
        return True

    def retrieve(self, query=None):
        """Retrieve memories, optionally filtered by a query"""
        if query is None:
            return self.memories

        # Simple implementation - could be more sophisticated
        return [m for m in self.memories if query in str(m)]