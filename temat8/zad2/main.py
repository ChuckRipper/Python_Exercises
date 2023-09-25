# Wariant #1
# def create_checker(connection):
#     database_local = connection
#     def check_tables():
#         # Implementacja korzystająca z database_local
#         pass
#     return check_tables

# Wariant #2
def create_checker(connection):
    def check_tables_inside():
        # Wykorzystanie "connection" wewnątrz tej funkcji do sprawdzenia spójności bazy
        pass
    return check_tables_inside
