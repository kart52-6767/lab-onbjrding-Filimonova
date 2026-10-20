def process_transaction(user_id, amount, db_connection):
    log_entry = "Start processing"
    status = "pending"  # Инициализация до if (исправление 1)

    if amount > 0:
        status = "approved"
        balance = get_balance(user_id)
        new_balance = balance - amount
        update_balance(user_id, new_balance)
        # Мертвое присваивание log_entry удалено (исправление 2)

    # Использование with open (исправление 3: утечка ресурса)
    log_entry = "Transaction finished with status: " + status
    with open("audit_log.txt", "w") as file:
        file.write(log_entry)

    return status
