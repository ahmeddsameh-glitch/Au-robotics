#even: the credit card will be
#378282246310005
# 0 * 2 + 0 * 2 + 3 * 2 + 4 * 2 + 2 *2 + 2 * 2 + 7 * 2 = 36
# 0 + 0 +6 +8+4+4+1+4= 27
#3 +8 + 8 +2 +6 +1 +0+5= 33

number= str(input("Enter your credit card number : "))
def is_valid_card_number(card_number):
    odd = 0
    if len(card_number) % 2:
        odd = 1
    card_number = str(card_number)
    if not card_number.isdigit():
        return False
    checksum = 0
    for i in range(0+odd, len(card_number), 2):
        digit=int(card_number[i]) * 2
        if digit > 9:
            digit=str(digit)
            digit=int(digit[0]) + int(digit[1])
        checksum += digit 
    for i in range(1-odd, len(card_number), 2):
        checksum += int(card_number[i])
    return not checksum % 10
def credit_card(card_number):
    if card_number.startswith("37") or card_number.startswith("34"):
        return "American Express"
    elif card_number.startswith("51") or card_number.startswith("52") or card_number.startswith("53") or card_number.startswith("54") or card_number.startswith("55"):
        return "MasterCard"
    elif card_number.startswith("4"):
        return "Visa"
    else:
        return "Unknown"
if is_valid_card_number(number):
    print(credit_card(number))
else:
    print("is not valid")