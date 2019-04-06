aclNum = int(input("Número de ACL de IPv4? "))
if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL de IPv4 estándar.")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL de IPv4 extendida.")
else:
    print("Esto no es una ACL de IPv4 estándar o extendida.")