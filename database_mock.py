# database_mock.py
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """
        Establishes a mock database connection.
        """
        self.connection = f"Connected to {self.db_name}"

    def disconnect(self):
        """
        Closes the database connection.
        """
        self.connection = None

    def status(self):
        """
        Returns the connection status.
        """
        return "Connected" if self.connection else "Disconnected"
