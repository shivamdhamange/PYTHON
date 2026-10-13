def check_target(sales, target):
    if sales>=target:
        print("Target Acheived")
    else:
        print("Target Not Acheived")

check_target(20000,15000)


def purchase_status(amount):
    if amount>5000:
        print("High purchase")
    elif amount<5000 and amount>1000:
        print("Medium Purchase")
    else:
        print("low Purchase")
        
purchase_status(6000)


def employee_performance(score):
    if score>=90:
        print("excellent")
    elif score<=89 and score>=75:
        print("good")
    elif score<74 and score>=50:
        print("average")
    else:
        print("poor")
        
        
def sales_growth(previous_sales, current_sales):
    growth = ((current_sales - previous_sales) / previous_sales) * 100

    if growth>0:
        print("Sales Increased")
    elif growth<0:
        print("Sales Decreased")
    else:
        print("no change")

sales_growth(5000,6000)


def validate_salary(salary):
    
    if salary ==0:
        print("Salary Missing")
    elif salary>0:
        print("valid salary")
    else:
        print("invalid salary")

validate_salary(50000)


def stock_status(stock):
    if stock ==0:
        print("out of stock")
    elif stock>1 and stock < 10:
        print("Low Stock")
    elif stock >11 and stock <50:
        print("Normal Stock")
    else:
        print("high stock")
stock_status(45)


def churn_status(status):
    if status == "yes":
        print("Customer Churned")
    elif status == "no":
        print("Customer Active")
    else:
        print("Invalid Status")

status1 = "yes"
churn_status(status1)


def traffic_status(visitors):
    if visitors<1000:
        print("Low traffic")
    elif visitors>=1000 and visitors<5000:
        print("Medium traffic")
    elif visitors>=5000 and visitors<10000:
        print("high traffic")
    else:
        print("very high traffic")

traffic_status(3000)

def kpi_status(value):
    if value>=90:
        print("Excellent KPI")
    elif value<89 and value>=70:
        print("Good KPI")
    elif value<70 and value>=50:
        print("average KPI")
    elif value<89:
        print("poor KPI")
        
kpi_status(69)

def calculate_commission(sales):
    if sales<50000:
        print("5% commission")
    elif sales>50000 and sales<100000:
        print("10% commission")
    else:
        print("15% commission")
        
calculate_commission(80000)