# https://leetcode.com/problems/invalid-transactions/description

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        data = defaultdict(set)
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            data[(name, time)].add(city) # get the set of cities

        print(data)

        res = []
        for transaction in transactions:
            name, curr_time, amount, city = transaction.split(',')
            curr_time = int(curr_time)
            if int(amount) > 1000: 
                res.append(transaction)
                continue
            for t in range(curr_time - 60, curr_time + 61):
                if (name, t) not in data: # check if there are other transactions within 60 mins
                    continue
                # check if other transactions are made in different cities
                if len(data[(name, t)]) > 1 or city not in data[(name, t)]: 
                    res.append(transaction)
                    break

        return res




            
