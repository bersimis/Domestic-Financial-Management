#Αυτός είναι ο βασικός καθορισμός των κλάσεων δεδομένων και των συναρτήσεων που θα χρησιμοποιηθούν 
#στην εφαρμογή. Οι συναρτήσεις θα πρέπει να υλοποιηθούν με βάση τις απαιτήσεις 
#της εφαρμογής και τη λογική της. Οτι περισσότερο χρειαστεί θα προστεθεί στην συνέχεια.

#ΚΛΑΣΕΙΣ ΔΕΔΟΜΕΝΩΝ (Απο ERD)

class User:
    def __init__(self, id, username, password_hash, created_at, birth_year, age):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.created_at = created_at
        self.birth_year = birth_year
        self.age = age  # Παράγωγο χαρακτηριστικό (διακεκομμένος κύκλος)

class Category:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

class Transaction:
    def __init__(self, id, user_id, category_id, amount, date, is_monthly):
        self.id = id
        self.user_id = user_id          # Προκύπτει από τη σχέση "Δημιουργεί" (1:N) ξένο κλειδί
        self.category_id = category_id  # Προκύπτει από τη σχέση "Ανήκουν σε" (N:1) ξένο κλειδί
        self.amount = amount
        self.date = date
        self.is_monthly = is_monthly


#ΣΥΝΑΡΤΗΣΕΙΣ (GUI Events + Backend)

# Συναρτήσεις Σύνδεσης & Εγγραφής
def click_login():
    pass

def click_register():
    pass

def click_logout():
    pass

# Συναρτήσεις Συναλλαγών
def click_save_transaction():
    pass

def click_delete_transaction():
    pass

def click_edit_transaction():
    pass

def load_transactions_table():
    pass

# Συναρτήσεις Κατηγοριών
def click_add_category():
    pass

def click_delete_category():
    pass

def load_categories_list():
    pass

# Συναρτήσεις Ανάλυσης & Εξαγωγής
def click_generate_charts():
    pass

def click_export_to_excel():
    pass

def calculate_monthly_summary():
    pass
