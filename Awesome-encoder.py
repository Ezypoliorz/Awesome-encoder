alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
a = 3
upper_lower = {}
message_encodé_final = ""
mode = input("Voulez-vous encoder (1) ou décoder (2) ? -> ")
if mode == "1" :
    message_original = input("Entrez le message à encoder -> ")
    message_encodé = ""
    for i in range(len(message_original)) :
        if message_original[i].isupper() == True :
            upper_lower[i] = 1
        else :
            upper_lower[i] = 0
    message_original_formaté = str(message_original).split(" ")
    for i in range(len(message_original_formaté)):
        b = len(message_original_formaté[i])
        message_original_upper = message_original_formaté[i].upper()
        for i in range(len(str(message_original_upper))) :
            if str(message_original_upper)[i] in alphabet :
                index_lettre_message_original = alphabet.index(str(message_original_upper)[i])
                index = a*index_lettre_message_original+b
                index = index%26
                message_encodé += alphabet[index]
            else :
                message_encodé += str(message_original_upper)[i]
        
        message_encodé += " "
    message_encodé = message_encodé[:-1]
    for i in range(len(str(message_encodé))) :
        if upper_lower[i] == 0 :
            message_encodé_final += message_encodé[i].lower()
        else :
            message_encodé_final += message_encodé[i]
    print(message_encodé_final)

elif mode == "2" :
    message_original = input("Entrez le message à décoder -> ")
    message_encodé = ""
    for i in range(len(str(message_original))) :
        if message_original[i].isupper() == True :
            upper_lower[i] = 1
        else :
            upper_lower[i] = 0
    message_original_formaté = str(message_original).split(" ")
    for i in range(len(message_original_formaté)) :
        b = len(message_original_formaté[i])
        message_original_upper = message_original_formaté[i].upper()
        for i in range(len(str(message_original_upper))) :
            if str(message_original_upper)[i] in alphabet :
                index_lettre_message_original = alphabet.index(str(message_original_upper)[i])
                for x in range(26):
                    if (a * x) % 26 == 1:
                        a = x
                index = int(a*(index_lettre_message_original-b))
                index = index%26
                message_encodé += alphabet[index]
            else :
                message_encodé += str(message_original_upper)[i]
        message_encodé += " "
    message_encodé = message_encodé[:-1]
    for i in range(len(str(message_encodé))) :
        if upper_lower[i] == 0 :
            message_encodé_final += message_encodé[i].lower()
        else :
            message_encodé_final += message_encodé[i]
    print(message_encodé_final)

else :
    print("Réponse non valide")
    