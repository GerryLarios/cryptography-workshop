import hashlib

# Generating a hash for the secret prediction
secret_prediction = "your_secret_prediction"
random_nonce = "random_nonce"
hashed_prediction = hashlib.sha256((secret_prediction + random_nonce).encode()).hexdigest()

# Publishing the hash
print("Published Hash:", hashed_prediction)

# Verifying the prediction
user_prediction = "user_input_prediction"
hashed_user_prediction = hashlib.sha256((user_prediction + random_nonce).encode()).hexdigest()

if hashed_user_prediction == hashed_prediction:
    print("Prediction is correct!")
else:
    print("Prediction doesn't match.")
