import sqlite3
import os

class DatabaseManager:
    
    # A class to manage interactions with the SQLite database.

    def __init__(self, db_path='data/prompts.db'):
        
        # Initializes the DatabaseManager with the path to the database.
        # Ensures the data directory exists, connects to the database, and creates the table.
        
        self.db_path = db_path
        self._ensure_data_directory_exists()
        self.connection = self._connect_to_database()
        self.cursor = self.connection.cursor()
        self.create_table()

    def _ensure_data_directory_exists(self):
        
        # Ensures that the data directory exists.
        # Creates the directory if it does not exist.
        
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def _connect_to_database(self):
        
        # Connects to the SQLite database and returns the connection object.
        # Handles any connection errors.
        
        try:
            return sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        
        # Creates the 'prompts' table in the database if it does not already exist.
        
        if self.connection:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS prompts (
                    id INTEGER PRIMARY KEY,
                    domain TEXT,
                    expertise TEXT,
                    task TEXT,
                    user_input TEXT,
                    generated_prompt TEXT
                )
            ''')
            self.connection.commit()

    def insert_prompt(self, domain, expertise, task, user_input, generated_prompt):
        
        # Inserts a new prompt record into the 'prompts' table.
        
        # Parameters:
        # - domain: The domain of the prompt.
        # - expertise: The expertise level related to the prompt.
        # - task: The task associated with the prompt.
        # - user_input: Additional user input for the prompt.
        # - generated_prompt: The generated prompt text.
        
        if self.connection:
            self.cursor.execute('''
                INSERT INTO prompts (domain, expertise, task, user_input, generated_prompt)
                VALUES (?, ?, ?, ?, ?)
            ''', (domain, expertise, task, user_input, generated_prompt))
            self.connection.commit()

    def close(self):
        
        # Closes the database connection.
        
        if self.connection:
            self.connection.close()