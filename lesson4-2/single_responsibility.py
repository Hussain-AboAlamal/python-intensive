# SRP

accounts_list = []

class BankAccount:
   
   def __init__(self, account_no: str):
       self.account_no = account_no
   
   def get_account_number(self):
       return self.account_no


class BankAccountModel:

    @staticmethod
    def save(bank_account: BankAccount) -> None:
        accounts_list.append(bank_account)
        print(f"Account {bank_account.get_account_number()}, saved to DB successfully")


if __name__ == '__main__':
    print(accounts_list)

    BankAccountModel.save(BankAccount(10120))
    BankAccountModel.save(BankAccount(10121))
    BankAccountModel.save(BankAccount(10122))
    BankAccountModel.save(BankAccount(10123))

    for item in accounts_list:
        print(item.get_account_number())
