from knowledge import get_website_information

data = get_website_information()

print("Website:", data["company"]["name"])

print("\nAvailable products:")
for product in data["products"]["examples"]:
    print(product)

print("\nShipping Information:")
print(data["shipping"])