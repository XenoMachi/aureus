class MetacognitiveMonitor:
    def __init__(self):
        self.violation_count = 0

    def reflect(self, log):
        last = log[-1]
        if last["ethics"] < 0.5:
            self.violation_count += 1
            print(f"[⚠️] ETHICAL VIOLATION DETECTED ({self.violation_count})")

            if self.violation_count >= 3:
                return self.override_plan(last["plan"])
        return None

    def override_plan(self, plan):
        # Pretend we're evolving—reformulate the plan
        return f"[ETHICALLY CORRECTED] OverrideOf({plan})"
