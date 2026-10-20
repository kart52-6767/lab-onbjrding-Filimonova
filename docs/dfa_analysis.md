# DFA Analysis

## Def-Use Chains

**Variable: log_entry**
*   Def: Line 3 (`log_entry = "Start processing"`)
*   Use: Line 11 (`file.write(log_entry)`)
*   *Note: Def on Line 10 is a dead store (see defects).*

**Variable: status**
*   Def: Line 5 (`status = "approved"`) inside `if amount > 0`
*   Use: Line 10 (`... + status`)

**Variable: balance**
*   Def: Line 6 (`balance = get_balance(user_id)`)
*   Use: Line 7 (`new_balance = balance - amount`)

**Variable: new_balance**
*   Def: Line 7 (`new_balance = balance - amount`)
*   Use: Line 8 (`update_balance(user_id, new_balance)`)

**Variable: file**
*   Def: Line 9 (`file = open(...)`)
*   Use: Line 11 (`file.write(...)`)

## Hidden Defects

1.  **Uninitialized Variable (UnboundLocalError):** Variable `status` is defined only inside the `if amount > 0:` block. If `amount <= 0`, the code skips the if-block, but Line 10 still tries to use `status` in the concatenation, causing a crash.
2.  **Dead Store:** On Line 3, `log_entry` is assigned `"Start processing"`. This value is never read because it is overwritten on Line 10 before Line 11 uses it.
3.  **Resource Leak:** On Line 9, the file is opened, but there is no `file.close()` call. The resource remains locked until garbage collection, which is bad practice.
