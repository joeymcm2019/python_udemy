#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def get_names(): 
    with open("./Input/Names/invited_names.txt") as file:
        names = []
        content = file.readline()
        content = content.replace("\n", "")
        while (content != ""):
            names.append(content)
            content = file.readline()
            content = content.replace("\n", "")
        file.close()
        return names


def compose_letter(name):
    letter_lines = []
    with open("./Input/Letters/starting_letter.txt") as file:
        content = file.readline()
        content = content.replace("[name]", f"{name}")
        while (content != ""):
            letter_lines.append(content)
            content = file.readline()
        file.close()    
    return letter_lines
            

def write_letter(name):
    letter = compose_letter(name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as file:
        for line in letter:
            file.write(line)
        file.close()

def create_invitations():
    guest_list = get_names()
    for guest in guest_list:
        write_letter(guest)

create_invitations()