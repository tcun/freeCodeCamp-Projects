class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def check_funds(self, amount):
      funds = 0
      n = len(self.ledger)
      for i in range(n):
          funds = funds + self.ledger[i]["amount"]
      if funds < amount:
          return False
      else:
          return True

  def deposit(self, amount, description=""):
    self.dep = dict()
    self.dep["amount"] = amount
    self.dep["description"] = description
    self.ledger.append(self.dep)

  def withdraw(self, amount, description=""):
      l = self.check_funds(amount)
      if l is True:
          self.withd = dict()
          self.withd["amount"] =- (amount)
          self.withd["description"] = description
          self.ledger.append(self.withd)
          return True
      else: 
          return False

  def get_balance(self):
    total=0
    for i in self.ledger:
        total+=i['amount']
    return total

  def transfer(self, amount, ob_name):
      objectname = ob_name.name
      a = self.withdraw(amount,f"Transfer to {objectname}")
      b = ob_name.deposit(amount,f"Transfer from {self.name}")
      if a is True:
          return True
      else:
          return False

  def __str__(self):
  
    s = "*"*((30-len(self.name))//2) + self.name

    s = s + "*"*(30-len(s)) + "\n"
    for i in self.ledger:

      s += i["description"][:23].ljust(23) + str("{:.2f}".format(i["amount"]).rjust(7)) + "\n"
    s+="Total: " + str(self.get_balance())
    return s

  def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total+= item["amount"]
        return total

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    
    #Breakdown of spending rounded down to nearest 10th
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded
def round_to_nearest_ten(n):
  if n<10:
    return 0
  return round(n/10.0)*10

def create_spend_chart(categories):
  withdrawls=[]

  #used to find the category name with max length
  max_len_category=0
  s=0

  for i in categories:

    withdraw_amount=0

    for j in i.ledger:

      #adding withdrawls to string 
      if j["amount"]<0:
        withdraw_amount+=-j["amount"]
        s+=(-j["amount"])
        
    #finding max len category name
    if len(i.name)>max_len_category:
      max_len_category=len(i.name)
    withdrawls.append([i.name,withdraw_amount])
  
  #used to calculate the percentage of a certain category
  for i in withdrawls:
    i.append(round_to_nearest_ten((i[1]/s)*100))
  s=""
  s+="Percentage spent by category\n"
  t=100
  while t>=0:
    s+=str(t).rjust(3)+"|"+" "


    for i in range(len(withdrawls)):
      if withdrawls[i][2]>=t:
        s+="o"+"  "
      else:
        s+="   "
    t-=10
    s+="\n"
  s+="    "+("-"*10)+"\n"

  loop_var=0

  for i in range(max_len_category):
    s+="     "
    for j in range(len(withdrawls)):
      if len(withdrawls[j][0])-1<loop_var:
        s+="   "
      else:
        #adds character 
        s+=withdrawls[j][0][loop_var]+"  "
    loop_var+=1
    if i!=max_len_category-1:
      s+="\n"


  return s
  
