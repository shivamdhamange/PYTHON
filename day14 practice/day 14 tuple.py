'''1. Monthly Sales Data

Situation: A data analyst has sales figures for 6 months stored in a tuple. Find total and average sales.
'''
sales = (25000, 32000, 28000, 40000, 35000, 45000)

total = sum(sales)
average = total / len(sales)

print("Sales:", sales)
print("Total Sales:", total)
print("Average Sales:", average)


'''2. Find Highest and Lowest Sales

Situation: An analyst wants to identify the highest and lowest monthly sales.
'''
sales = (25000, 32000, 28000, 40000, 35000, 45000)

print("Highest Sales:", max(sales))
print("Lowest Sales:", min(sales))



'''3. Sales for a Particular Month

Situation: Sales data is stored month-wise. Display sales of the first, third, and last month.
'''
sales = (25000, 32000, 28000, 40000, 35000, 45000)

print("First month sales:", sales[0])
print("Third month sales:", sales[2])
print("Last month sales:", sales[-1])



'''4. Quarterly Sales Analysis

Situation: A company stores monthly sales in a tuple. Calculate sales for the first quarter.
'''
sales = (25000, 32000, 28000, 40000, 35000, 45000)

quarter1 = sales[0:3]

print("First Quarter Sales:", quarter1)
print("First Quarter Total:", sum(quarter1))



'''5. Employee Salary Analysis

Situation: HR provides salaries of five employees. Find the highest, lowest, and average salary.
'''
salary = (35000, 42000, 28000, 55000, 48000)

print("Highest Salary:", max(salary))
print("Lowest Salary:", min(salary))

average = sum(salary) / len(salary)
print("Average Salary:", average)



'''6. Customer Age Analysis

Situation: A data analyst has the ages of customers in a tuple. Find the youngest and oldest customer.
'''
ages = (25, 32, 41, 28, 35, 52, 19)

print("Youngest Customer:", min(ages))
print("Oldest Customer:", max(ages))
print("Total Customers:", len(ages))


'''7. Product Ratings

Situation: A company stores customer ratings for a product.
'''
ratings = (5, 4, 5, 3, 4, 5, 2, 4)

print("Ratings:", ratings)
print("Highest Rating:", max(ratings))
print("Lowest Rating:", min(ratings))
print("Average Rating:", sum(ratings) / len(ratings))


'''
8. Count Customer Ratings

Situation: An analyst wants to find how many customers gave a rating of 5.
'''
ratings = (5, 4, 5, 3, 4, 5, 2, 4, 5)

count = ratings.count(5)

print("Number of 5-star ratings:", count)



'''9. Find Position of a Product

Situation: Product IDs are stored in a tuple. Find the position of a particular product ID.
'''
product_ids = (101, 105, 110, 115, 120)

product = int(input("Enter product ID: "))

if product in product_ids:
    print("Product found")
    print("Position:", product_ids.index(product))
else:
    print("Product not found")


'''10. Attendance Analysis

Situation: An analyst stores attendance percentages of employees.
'''
attendance = (95, 87, 72, 91, 65, 88, 78)

print("Highest Attendance:", max(attendance))
print("Lowest Attendance:", min(attendance))
print("Average Attendance:", sum(attendance) / len(attendance))


'''
11. Website Visitors

Situation: A website receives the following number of visitors over seven days.
'''
visitors = (1200, 1500, 1800, 1300, 2100, 2500, 2000)

print("Total Visitors:", sum(visitors))
print("Highest Visitors:", max(visitors))
print("Lowest Visitors:", min(visitors))
print("Average Visitors:", sum(visitors) / len(visitors))


'''12. Check Sales Target

Situation: A company has monthly sales in a tuple. Check whether a target value was achieved in any month.
'''
sales = (25000, 32000, 28000, 40000, 35000, 45000)

target = int(input("Enter sales target: "))

if target in sales:
    print("Target value found")
else:
    print("Target value not found")


'''
13. Transaction Data

Situation: A bank analyst has transaction amounts stored in a tuple. Calculate total transactions and average transaction value.
'''
transactions = (5000, 2500, 10000, 3500, 7000)

print("Total Transaction Amount:", sum(transactions))
print("Number of Transactions:", len(transactions))
print("Average Transaction:", sum(transactions) / len(transactions))



'''14. Monthly Expense Analysis

Situation: A person's monthly expenses are stored in a tuple.
'''
expenses = (15000, 18000, 12000, 20000, 17000, 22000)

total = sum(expenses)
average = total / len(expenses)

print("Total Expense:", total)
print("Average Expense:", average)
print("Highest Expense:", max(expenses))
print("Lowest Expense:", min(expenses))


'''
15. Student Marks Analysis

Situation: A data analyst wants to analyze marks of a student in five subjects.
'''
marks = (78, 65, 82, 71, 90)

total = sum(marks)
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
