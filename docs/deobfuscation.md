# Deobfuscation Analysis

## Decoded String
`import os; os.system('rm -rf /')`

## Threat Analysis
The script uses the `exec()` function to execute an obfuscated Base64 payload. The decoded payload imports the `os` module and executes the system command `rm -rf /`. This command attempts to recursively and forcefully delete all files and directories starting from the root directory (`/`). On a Linux/Unix system with sufficient privileges (e.g., running as root), this would destroy the entire operating system, leading to catastrophic data loss and system unavailability.

## Protection Methods
1. **Avoid `exec` on untrusted input:** Never use `exec()` or `eval()` on data received from external sources.
2. **Static Analysis:** Use SAST tools that can detect the use of dangerous functions like `exec` combined with `base64.b64decode`.
3. **Input Validation / Sandboxing:** Run suspicious scripts in a restricted sandbox or container with no write access to the host filesystem.
4. **Principle of Least Privilege:** Ensure scripts do not run with root privileges.
