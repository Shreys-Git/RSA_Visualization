from django.shortcuts import render
from django.http import HttpResponse

# RSA Encryption: 
# BASIC SETUP - P, Q => n => phi_n

# Declare P and Q ( Both 4 digit Primes as requested ) 
p = 1237
q = 1723

# Calculate N 
n = p*q

# Calculate Phi_N (Since both are prime)
phi_n = (p-1)*(q-1)

# Find e (e is a coprime with phi_n)
e = 1277

# Calculate d (-1 if d is not found)
# Calculate d 
def get_d_value(e, phi_n):
    for i in range(1, phi_n):
        if (((e%phi_n) * (i%phi_n)) % phi_n == 1):
            return i
    return -1

# Function call to get the d 
d = get_d_value(e, phi_n)
print(d)
# FIND THE KEYS - Private and Public 

# Public Key 
public_key = (e,n)

# Private Key 
private_key = (d,n)
#-----------------------------------------------------------------------------------------------

# Home page -> Send messages from here 
def index(request):
    return render(request, "index.html")

# Key Generation
def keys(request):
    # FIND THE KEYS - Private and Public 

    # Public Key 
    public_key = (e,n)

    # Private Key 
    private_key = (d,n)

    return render(request, "second.html", {'private_key':private_key,'public_key':public_key})

# Encryption and Decryption
def encrypted(request):
    # User Input 
    text = request.POST.get('your_name', False)
    print(text)
    
    if text:

        # Encoding the Message from the user (String -> Array)
        message = []
        for ch in text: 
            message.append(ord(ch))
        print(message)

        # Encrypt the Plain Text (Array -> Array)
        cipher = []
        for P in message:
            cipher.append(pow(P,e,n))
        print(cipher)

        # Display the encrypted Data (Str form)
        encrypted_data ='#'
        for pt in cipher:
            encrypted_data += str(pt)
        
        # Decrypt the Plain Text
        plain = []
        for c in cipher: 
            plain.append(pow(c,d,n))
        print(cipher)

        # Final Message decoded on the Reciever Side 
        text = ''
        for p in plain: 
            text += chr(p)
        
        print(text)

    return render(request, "third.html",{'encrypted_data': encrypted_data, 'final_message':text} )
