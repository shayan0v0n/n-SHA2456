import sys
import hashlib

input_message = sys.argv[1]
num_repetitions = int(sys.argv[2])

hash_object = hashlib.sha256()

for _ in range(num_repetitions):
    hash_object.update(input_message.encode('utf-8'))

print(f"SHA-256 Hash: {hash_object.hexdigest()}\nRepetitions: {num_repetitions}")
