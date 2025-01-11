# https://leetcode.com/problems/heaters/description/

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        num_houses = len(houses)
        num_heaters = len(heaters)
        houses.sort()
        heaters.sort()

        if houses == heaters: # case: every house has heater
            return 0

        max_cover = 0
        house_pt = 0
        heater_pt = 0

        while (house_pt < num_houses and heater_pt < num_heaters):
            rad = abs(houses[house_pt] - heaters[heater_pt])

            while heater_pt < num_heaters - 1:
                if (rad > abs(houses[house_pt] - heaters[heater_pt + 1])):
                    rad = abs(houses[house_pt] - heaters[heater_pt + 1])
                    heater_pt += 1
                else:
                    break

            max_cover = max(max_cover, rad)
            house_pt += 1

        return max_cover


    