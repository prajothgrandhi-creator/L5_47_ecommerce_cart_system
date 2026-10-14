"""E-commerce shopping cart with basic checkout and receipt utilities."""

import hashlib
import secrets
from pathlib import Path

cart_items = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}


def add_item_to_cart(item_id, name, price, qty=1, audit_log=None):
    """Add an item to the cart and optionally record the action."""
    if item_id in cart_items:
        return False
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a non-negative number.")
    if not isinstance(qty, int) or qty < 1:
        raise ValueError("Quantity must be a positive integer.")

    if audit_log is None:
        audit_log = []
    cart_items[item_id] = {"name": name, "price": float(price), "qty": qty}
    audit_log.append(f"Added {item_id} with price {price:.2f}")
    return True


def remove_item_from_cart(item_id):
    """Remove an item from the cart; return False if it does not exist."""
    try:
        del cart_items[item_id]
    except KeyError:
        return False
    return True


def check_cart_status(item_id):
    """Return whether an item exists in the cart with positive quantity."""
    item = cart_items.get(item_id)
    return item is not None and item["qty"] > 0


def calculate_discounted_total(item_id, discount_rate):
    """Calculate an item's discounted price using a rate from 0.0 to 1.0."""
    if item_id not in cart_items:
        raise KeyError(f"Item {item_id!r} is not in the cart.")
    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be a number.")
    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1.")

    base_price = cart_items[item_id]["price"]
    return round(base_price * (1 - discount_rate), 2)


def generate_item_hash(item_id):
    """Return a SHA-256 digest for an item identifier."""
    return hashlib.sha256(item_id.encode("utf-8")).hexdigest()


def generate_checkout_pin():
    """Generate a cryptographically strong four-digit checkout PIN."""
    return secrets.randbelow(9000) + 1000


def export_cart_receipt(filename="receipt.txt"):
    """Write the current cart to a UTF-8 text receipt."""
    receipt_path = Path(filename)
    with receipt_path.open("w", encoding="utf-8") as receipt_file:
        for item_id, details in cart_items.items():
            receipt_file.write(
                f"{item_id}: {details['name']} | "
                f"price={details['price']:.2f} | qty={details['qty']}\n"
            )
    print(f"Receipt saved to: {receipt_path}")


def get_cart_summary(items):
    """Return the total quantity of items with positive quantities."""
    return sum(
        details["qty"]
        for details in items.values()
        if details["qty"] > 0
    )


def main():
    """Run a short demonstration of the shopping cart features."""
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1)
    remove_item_from_cart("ITEM2")
    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print("Discounted Price:", calculate_discounted_total("ITEM1", 0.10))
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())
    export_cart_receipt()
    print("Total items:", get_cart_summary(cart_items))


if __name__ == "__main__":
    main()
