import hashlib
input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data)
result = result.hexdigest()
print(result)