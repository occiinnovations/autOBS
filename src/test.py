import requests

while True:
    num = input("Enter integer to trigger: ")
    if num.lower() == 'exit':
        break

    # This automatically shoots the number to your main script
    requests.post(f"http://127.0.0.1:8000/{num}")
