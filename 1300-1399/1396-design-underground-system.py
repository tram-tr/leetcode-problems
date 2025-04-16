# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.travel = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        travel_time = t - start_time
        if (start_station, stationName) in self.travel:
            total_time, count_travel = self.travel[(start_station, stationName)]
            self.travel[(start_station, stationName)] = (travel_time + total_time, count_travel + 1)
        else:
            self.travel[(start_station, stationName)] = (travel_time, 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count_travel = self.travel[(startStation, endStation)]
        return total_time / count_travel



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
