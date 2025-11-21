import os

msg = []
name = input("Type your name: ")  # get username

while True:
    os.system("clear")  # clear terminal

    if len(msg) > 0:  # check if there are messages
        for m in msg:  # if you have messages display
            print(m["name"], "-", m["text"])

    print("_________________")

    # getting text
    text = input("Message: ")  # receive the message
    if text == "end":  # if it is the word "end" the loop is interrupted
        break

    # if it is not the word "end" it adds the message to the list
    msg.append(
        {
            "name": name,
            "text": text,
        }
    )
