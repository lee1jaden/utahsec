#c=cipherText
c=421345306292040663864066688931456845278496274597031632020995583473619804626233684
#n=modulus
n=631371953793368771804570727896887140714495090919073481680274581226742748040342637
#public exponent
e=65537



# Compute cube root of C
M, exact = gmpy2.iroot(c, e)

# If the message M is exact, you have the plaintext
if exact:
    print("Plaintext:", M)
else:
    print("Cube root not exact. Different attack might be needed.")