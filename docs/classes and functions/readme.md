# How We Handle Code in This Project

Here’s a simple guide to how we’re organizing our classes and functions. The goal is to keep things clean and easy to find.

## Classes

Think of the classes in this project as simple blueprints for our data. They don't have a lot of complex logic in them. Their main job is to hold information in a structured way.

*   **`User`**: Holds all the info about a single user.
*   **`Category`**: Represents a single income or expense category.
*   **`Transaction`**: Stores the details of one financial transaction.

When you need to pass data around, just create an instance of one of these classes.

## Functions

The functions are the "actions" of our app. Most of them are named to match what they do when a user interacts with the interface (like `click_login` or `click_save_transaction`).

*   **Event-Driven**: Most functions are triggered by an event, like a button click.
*   **Single Purpose**: Each function should do one thing and do it well. For example, `load_transactions_table` only fetches and displays the transactions.
