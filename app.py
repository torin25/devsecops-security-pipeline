import os
import subprocess

#Hardcoded secret (for Gitleaks to detect)
API_KEY = "AKIAIOSFODNN7EXAMPLE"

#Insecure use of subprocess (Bandit will flag this)
def list_directory(path):
    return subprocess.check_output("ls " + path, shell=True).decode()

#Use of assert (Bandit flags B101)
def authenticate(user):
    assert user != "admin", "Admin login disabled!"

#Weak hashing (Bandit flags B303)
import hashlib
def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

#Hardcoded password (Gitleaks will catch)
DB_PASSWORD = "password123"

print("Directory listing:", list_directory("."))
print("Weak hash of 'test':", weak_hash("test"))
authenticate("guest")
print("App running...")
