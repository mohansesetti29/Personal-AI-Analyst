class AnalystMemory:
    def __init__(self):
        self.hypotheses = []
        self.insights = []

    def add_hypothesis(self, h):
        self.hypotheses.append(h)

    def add_insight(self, i):
        self.insights.append(i)
