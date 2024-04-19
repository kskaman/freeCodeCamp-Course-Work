class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount, 'description':description})

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def __str__(self):
        header = f'{self.name:*^30}\n'
        items_str = ''
        for item in self.ledger:
            items_str += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
        total = f"Total: {self.get_balance()}"
        return header + items_str + total

def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        withdrawal = 0
        for item in category.ledger:
            if item['amount'] < 0:
                withdrawal += abs(item['amount'])
        withdrawals.append(withdrawal)
  
    total = sum(withdrawals)
    percentages = [withdrawal/total * 100 for withdrawal in withdrawals]

    s = "Percentage spent by category"
    for i in range(100, -1, -10):
        s += "\n" + str(i).rjust(3) + "|"
        for percentage in percentages:
            if percentage > i:
                s += " o "
            else:
                s += "   "
        s += " "
    s += "\n    ----------"

    length = []
    for category in categories:
        length.append(len(category.name))
    max_length = max(length)

    for i in range(max_length):
        s += "\n    "
        for j in range(len(categories)):
            if i < length[j]:
                s += " " + categories[j].name[i] + " "
            else:
                s += "   "
        s += " "

    return s
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount':amount, 'description':description})

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        return False

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def __str__(self):
        header = f'{self.name:*^30}\n'
        items_str = ''
        for item in self.ledger:
            items_str += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
        total = f"Total: {self.get_balance()}"
        return header + items_str + total

def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        withdrawal = 0
        for item in category.ledger:
            if item['amount'] < 0:
                withdrawal += abs(item['amount'])
        withdrawals.append(withdrawal)
  
    total = sum(withdrawals)
    percentages = [withdrawal/total * 100 for withdrawal in withdrawals]

    s = "Percentage spent by category"
    for i in range(100, -1, -10):
        s += "\n" + str(i).rjust(3) + "|"
        for percentage in percentages:
            if percentage > i:
                s += " o "
            else:
                s += "   "
        s += " "
    s += "\n    ----------"

    length = []
    for category in categories:
        length.append(len(category.name))
    max_length = max(length)

    for i in range(max_length):
        s += "\n    "
        for j in range(len(categories)):
            if i < length[j]:
                s += " " + categories[j].name[i] + " "
            else:
                s += "   "
        s += " "

    return s
