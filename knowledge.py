# ShopEase Website Knowledge Base

website_info = {

    "company": {
        "name": "ShopEase",
        "description": "ShopEase is an online shopping platform offering electronics, fashion and home essentials.",
        "founded": "2022",
        "location": "Kolkata, India"
    },

    "products": {
        "categories": [
            "Electronics",
            "Fashion",
            "Home Essentials"
        ],

        "examples": [
            "Wireless Headphones - ₹1499",
            "Smart Watch - ₹2499",
            "Laptop Backpack - ₹899",
            "Cotton T-Shirt - ₹499",
            "Desk Lamp - ₹799"
        ]
    },

    "shipping": {
        "standard_delivery": "3-5 business days",
        "free_shipping": "Available on orders above ₹999",
        "tracking": "Customers can track orders through the My Orders section."
    },

    "returns": {
        "return_period": "7 days from delivery",
        "refund_time": "5-7 business days after return approval",
        "conditions": "Products must be unused and returned in their original packaging."
    },

    "payment": {
        "methods": [
            "UPI",
            "Credit Card",
            "Debit Card",
            "Cash on Delivery"
        ]
    },
        "orders": {
        "ORD1001": {
            "product": "Wireless Headphones",
            "status": "Shipped",
            "estimated_delivery": "8 November 2026"
        },
        "ORD1002": {
            "product": "Smart Watch",
            "status": "Out for Delivery",
            "estimated_delivery": "6 November 2026"
        },
        "ORD1003": {
            "product": "Laptop Backpack",
            "status": "Processing",
            "estimated_delivery": "10 November 2026"
        }
    },
     "cancellation": {
            "policy": "Orders can be cancelled before they are shipped.",
            "refund": "For prepaid orders, refunds are processed within 5-7 business days after cancellation approval."
    },
    "customer_support": {
        "email": "support@shopease.demo",
        "hours": "Monday to Saturday, 9 AM - 6 PM"
    }
   
}


def get_website_information():
    """
    Returns all available website information.
    """
    return website_info