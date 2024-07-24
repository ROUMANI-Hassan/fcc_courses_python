class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []
        self.deposit_amount = 0
        self.withdrawals = 0
        
    def __str__(self):
        total = 0
        ledger = self.ledger
        category = self.category
        length = len(category)
        half_length = (30 - length) // 2
        left = half_length
        right = half_length if (30 - length) % 2 == 0 else half_length + 1

        title = f"{'*' * left}{category}{'*' * right}"

        items = ''
        for item in ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:>7.2f}"
            items += f"{description:<23}{amount}\n"

        total = f"Total: {self.deposit_amount:.2f}"

        return f"{title}\n{items}{total}"

    def deposit(self,amount,description=''):
        self.deposit_amount += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        self.withdrawals += amount
        if amount < self.deposit_amount:
            self.deposit_amount -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False


    def transfer(self,amount,category):
        description_to = f'Transfer to {category.category}'
        description_from = f'Transfer from {self.category}'
        if amount < self.deposit_amount:
            category.deposit(amount,description_from)
            self.withdraw(amount,description_to)
            return True
        else:
            return False
    def get_balance(self):
        return self.deposit_amount
    def check_funds(self,amount):
        if self.deposit_amount>=amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.category, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")



food = Category('Food')
food.deposit(900, 'deposit')
food.withdraw(30, 'milk, cereal, eggs, bacon, bread')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10)
clothing2 = Category('Clothing2')
clothing2.deposit(500)
clothing2.withdraw(10)
print(create_spend_chart([food,clothing,clothing2]))
