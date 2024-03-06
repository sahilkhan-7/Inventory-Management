import time 

# with open('inventory.txt', 'r') as file:
#     products = file.readlines()
#     for i in products:
#         print(i, end='')

def AddProductsinStock(file):
    with open(file, 'a') as file:
        n = int(input('How many products you want to add:'))
        for i in range(n):
            id = input(f"Enter the id of {i+1} product: ")
            name = input("Enter the product name: ")
            price = input("Enter the product price: ")
            quantity = input("Enter the product quantity: ")
            file.write(f'{id}, {name}, {price}, {quantity}\n')

# AddProductsinStock('inventory.csv')
            
def take_user_info():
    # Taking user input for pucharsing the product
    user_name = input("Enter your name: ")
    user_phone = input("Enter your phone number: ")
    user_email = input("Enter your email: ")
    user_address = input("Enter your address: ")


with open('inventory.csv', 'r') as file:

    # Taking user input for pucharsing the product
    user_name = input("Enter your name: ")
    user_phone = input("Enter your phone number: ")
    user_email = input("Enter your email: ")
    prod_name = input("Enter the product name: ")
    prod_quant = int(input("Enter the quantity: "))

    # reading the inventory file
    products = file.readlines()

    # for updating the quantity of the product 
    updated_product_inv = []
    product_found = False

    # checking the product in the inventory
    for product in products:
        product = product.replace('\n', '')
        prod_details = product.split(", ")
        if (prod_details[1].lower().strip() == prod_name.lower().strip()):

            # checking the quantity of the product
            if int(prod_details[3]) >= prod_quant:
                print('-'*40)
                # print(f'Product ID                 : {prod_details[0]}')
                print(f'Product Name               : {prod_details[1]}')
                print(f'Product Price Per piece    : {prod_details[2]}')
                print(f'Product Quantity           : {prod_quant}')
                print('-'*40)
                print(f'Amount to be paid: {int(prod_quant) * int(prod_details[2])}')
                print('-'*40)
                prod_details[3] = str(int(prod_details[3]) - prod_quant)
                product_found = True

                # story the user information in the sales file
                # after each purchase the sales file will be updated
                with open('sales.csv', 'a') as file:

                    # writing the user information in the sales file
                    # user_name, user_phone, user_email, product_name, product_quantity, total_amount 
                    sales_info = f"{user_name}, {user_phone}, {user_email}, {prod_details[1]}, {prod_quant}, {int(prod_quant) * int(prod_details[2])}, {time.ctime()}\n"
                    file.write(sales_info)


            else: 
                print("Sorry we are not having enough quatity for this product.")
                print(f'We are only having {prod_details[3]} quantity of {prod_details[1]}')

                # Asking user if they want to buy the available quantity
                choice = input("Do you want to buy the available quantity? (yes/no): ")

                # if user wants to buy the available quantity
                if choice.lower() == 'yes':
                    print('-'*40)
                    print(f'Product ID                 : {prod_details[0]}')
                    print(f'Product Name               : {prod_details[1]}')
                    print(f'Product Price Per piece    : {prod_details[2]}')
                    print(f'Product Quantity           : {prod_details[3]}')
                    print('-'*40)
                    print(f'Amount to be paid: {int(prod_details[3]) * int(prod_details[2])}')
                    print('-'*40)
                    prod_details[3] = '0'
                    product_found = True

                # Else thanking the user
                else:
                    print("Thank you for visiting our store. Have a great day!")
                product_found = True

        # updating inventory
        updated_product_inv.append(prod_details)

    # if the product not found in the inventory
    if not product_found:
        print("Product not found")

# updating the inventory file
with open('inventory.csv', 'w') as file:
    for product in updated_product_inv:
        file.write(", ".join(product) + "\n")

# print("Inventory updated successfully!")