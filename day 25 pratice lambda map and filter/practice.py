'''1. Filtering Out Inactive Users
Scenario: You have a list of user dictionaries, and you want to quickly filter out the users who are currently inactive.
'''

users = [
    {"username": "alice", "active": True},
    {"username": "bob", "active": False},
    {"username": "charlie", "active": True},
    {"username": "diana", "active": False}
]

active_users = list(filter(lambda x : x['active'],users))
print(active_users)


'''2. Sorting a List of Products by Price
Scenario: You are building an e-commerce sorting feature and need to sort a list of products from cheapest to most expensive.
'''

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Mouse", "price": 25.50},
    {"name": "Keyboard", "price": 75.00}
]

sorted_product = sorted(products,key = lambda x : x["price"])
print(sorted_product)



'''3. Applying a Discount to Prices
Scenario: A flash sale requires applying a 20% discount across an entire list of item prices.
'''

prices = [100, 250, 50, 500]

discounted_prices = list(map(lambda price: price * 0.8, prices))

print(discounted_prices)



'''1. Extracting Specific Data from API Responses
Scenario: An API returns a list of user profiles, but your UI only needs a list of their email addresses.
'''


profiles = [
    {"id": 1, "email": "alice@example.com"},
    {"id": 2, "email": "bob@example.com"},
    {"id": 3, "email": "charlie@example.com"}
]
emails = list(map(lambda profile: profile["email"], profiles))
print(emails)


'''2. Finding the Longest Word in a List
Scenario: You want to find the longest search keyword entered by users from a list of strings.
'''


keywords = ["python", "lambda", "programming", "code"]

longest_keyword = max(keywords, key=lambda word: len(word))
print(longest_keyword)


'''3. Conditional Formatting / Quick Inline Logic
Scenario: You are generating a receipt summary and need a quick inline check to see if an order qualifies for free shipping (orders over $50).
'''


shipping_status = lambda amount: "Free Shipping" if amount > 50 else "Standard Shipping ($5)"

print(shipping_status(35))


'''4. Cleaning Up String Input (Stripping Whitespace)
Scenario: Users typed extra spaces around their usernames in a form, and you want to clean them up instantly.
'''

raw_inputs = ["  alice ", "bob   ", "  charlie  ", "diana"]
cleaned_inputs = list(map(lambda name: name.strip(), raw_inputs))

print(cleaned_inputs)
