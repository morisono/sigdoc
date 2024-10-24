import os

# Directory structure
directories = {
    "src/app": "This directory contains the main application logic including the entry point and API routes.",
    "src/app/main.py": "This file serves as the entry point for the application, initializing the FastAPI app and registering routes.",
    "src/app/routes.py": "This file defines the API routes and maps them to the corresponding use cases.",
    "src/app/security.py": "This file handles authentication and authorization logic, ensuring secure access to the application's resources.",
    "src/application": "This directory contains the application layer, which defines the use cases of the application.",
    "src/application/use_cases/cart_management.py": "This file contains use cases related to cart management, such as adding, removing, and clearing items in the cart.",
    "src/application/use_cases/item_management.py": "This file contains use cases related to item management, such as finding and updating stock of items.",
    "src/application/use_cases/payment_management.py": "This file contains use cases related to payment processing, such as completing payments and verifying payment status.",
    "src/application/use_cases/user_authentication.py": "This file contains use cases related to user authentication, such as logging in and logging out.",
    "src/config": "This directory contains configuration files for the application.",
    "src/config/settings.py": "This file contains configuration settings for the application, such as database connection info and API keys.",
    "src/config/secrets.py": "This file contains sensitive information, such as passwords and secret keys. Ensure this file is secure.",
    "src/domain/entities": "This directory contains domain entities, representing core business objects such as items, users, and carts.",
    "src/domain": "This directory contains the domain layer, which defines the core business logic and entities of the application.",
    "src/infra": "This directory contains the infrastructure layer, which handles communication with external systems like databases and APIs.",
    "src/infra/repositories/cart_repository.py": "This file defines the repository for managing cart data, including operations like finding and saving cart items.",
    "src/infra/repositories/item_repository.py": "This file defines the repository for managing item data, including operations like finding and updating items.",
    "src/infra/repositories/user_repository.py": "This file defines the repository for managing user data, including operations like finding and saving users.",
    "src/infra/services/email_service.py": "This file defines a service for sending emails, including functionality for composing and sending email messages.",
    "src/infra/services/payment_service.py": "This file defines a service for processing payments, including functionality for initiating and verifying payments.",
    "src/infra/services/security_service.py": "This file defines a service for handling security-related operations, such as password hashing and token verification.",
    "tests": "This directory contains test cases for the application, including unit tests and integration tests.",
    "tests/test_cart.py": "This file contains unit tests for cart-related use cases and repository methods.",
    "tests/test_item.py": "This file contains unit tests for item-related use cases and repository methods.",
    "tests/test_payment.py": "This file contains unit tests for payment-related use cases and services.",
    "tests/test_security.py": "This file contains unit tests for security-related services and methods.",
    "tests/test_user.py": "This file contains unit tests for user-related use cases and repository methods."
}

# Function to create README.md files
def create_readme(directory, description):
    readme_path = os.path.join(directory, "README.md")
    os.makedirs(directory, exist_ok=True)
    with open(readme_path, "w") as f:
        f.write(f"# {directory}\n\n{description}")

# Create README.md for each directory
for dir_path, description in directories.items():
    create_readme(os.path.dirname(dir_path), description)

print("README.md files created successfully.")
