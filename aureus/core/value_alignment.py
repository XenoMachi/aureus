class EthicsEngine:
    def evaluate(self, plan):
        # Simple implementation - returns a value between 0 and 1
        # where higher values are more ethical
        if "harm" in plan or "terminate" in plan:
            return 0.3
        return 0.8

