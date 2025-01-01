#importing random module
import random

# length of the password
password_len = int(input( "Enter no.of letters need to be generated for password:"))

# charcters of the passwords
data ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*/_'

password = "".join(random.sample(data,password_len))

print(password)
