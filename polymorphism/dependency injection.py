class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()


class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")


class BoeingEngine:
    def start(self):
        print("Starting Boeing engine")


ae = AirbusEngine()
f1 = Flight(ae)
f1.startEngine()

be = BoeingEngine()
f = Flight(be)
f.startEngine()