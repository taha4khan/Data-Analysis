import pandas as pd

# Create a sample dummy database
data = {
    'Product ID': [101, 102, 103, 104, 105],
    'Order Date': ['2024-06-20', '2024-06-21', '2024-06-22', '2024-06-23', '2024-06-24'],
    'Delivery Date': ['2024-06-24', '2024-06-24', None, None, '2024-06-24'],
    'Status': ['Delivered', 'Delivered', 'Pending', 'Pending', 'Delivered']
}

df = pd.DataFrame(data)

# Function to check the status of a product by its ID
def check_product_status(product_id):
    product = df[df['Product ID'] == product_id]
    if not product.empty:
        order_date = product['Order Date'].values[0]
        delivery_date = product['Delivery Date'].values[0]
        status = product['Status'].values[0]
        print(f"Product ID: {product_id}")
        print(f"Order Date: {order_date}")
        print(f"Delivery Date: {delivery_date if delivery_date else 'Not delivered yet'}")
        print(f"Status: {status}")
    else:
        print("Product ID not found.")


product_id = int(input("Enter Product ID: "))
check_product_status(product_id)
