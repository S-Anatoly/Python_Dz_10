class MinStat:
    def __init__(self):
        self.list1 = []

    def add_numbers(self, num):
        self.list1.append(num)

    def result(self):
        if self.list1 != []:
            return min(self.list1)
        else:
            return None


class MaxStat(MinStat):

    def result(self):
        if self.list1 != []:
            return max(self.list1)
        else:
            return None


class AverageStat(MinStat):
    def result(self):
        if self.list1 != []:
            return (sum(self.list1)) / len(self.list1)
        else:
            return None


values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

for v in values:
    mins.add_numbers(v)
    maxs.add_numbers(v)
    average.add_numbers(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# print(mins.result(), maxs.result(), average.result())
