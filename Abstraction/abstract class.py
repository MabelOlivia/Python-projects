from abc import abstractmethod,ABC


class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("start the car")

    def stop(self):
        print("stop the car")

    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseEnabledControl = cruiseControlEnabled

    def stop(self):
        print("Car stop")   # overriding

    def drive(self):
        print(" three series is being driven")

class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def display(self):
        print(self.parkingAssistEnabled)

    def stop(self):
        super().stop()             # using super()
        print("Car stop")

    def drive(self):
        print(" three series is being driven")


theeSeries = ThreeSeries(True, "BMW", '328i', 2017)
print(theeSeries.cruiseEnabledControl)
print(theeSeries.make)
print(theeSeries.model)
print(theeSeries.year)
theeSeries.start()
theeSeries.stop()


fiveSeries = FiveSeries(True, "BMW", '468i', 2018)
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()

