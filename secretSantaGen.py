import os 
import sys 
import random

class Participant: # Participant class holds all data about participant 
    def __init__(self,name,email,ban_list):
        self.name = name
        self.email = email
        self.ban_list = ban_list
        self.is_assigned = False
        self.assigned_participant = None

    def reset_assignment(self):
        self.is_assigned = False
    
def get_ban_list_size (participant):
    return -1*len(participant.ban_list)
        
def valid_assignment (current_participant,check_participant):# Checks if it is possible to assign a participant to someone based on the defined criteria
    if check_participant.is_assigned == True :
        return False
    elif current_participant.name == check_participant.name:
        return False
    elif check_participant.name in current_participant.ban_list:
        return False
    else:
        return True

def generate_assignment(participant_list):
    # The sorting here reducing probably of a incorrect assignment by giving participants with the largest ban_list the first pick of possible secret santas 
    participant_list.sort(key=get_ban_list_size) 
    retart = True
    # In the rare chance where the possible solution is incorrect the algorithm tries again
    while retart == True: 
        retart = False
        for i in range(0,len(participant_list)):
            current_participant = participant_list[i]
            valid_list = []
            for j in range(0,len(participant_list)):
                check_participant = participant_list[j]
                check_valid_assignment = valid_assignment(current_participant,check_participant)
                if check_valid_assignment:
                    valid_list.append(check_participant)
            if len(valid_list) == 0:
                retart = True
                for participant in participant_list: participant.reset_assignment() # reset assignments
                break
            valid_participant = random.choice(valid_list)
            current_participant.assigned_participant = valid_participant.name
            valid_participant.is_assigned = True
        
def generate_participant_list(source_path):
    #Assumptions
    #1. The file contains names in the following format: FirstName LastName email FirstName LastName FirstName LastName ...
    # names after email are names the user does not want to receive as their secret santa (i call it the ban list) 
    #2. The file has an even number of participants to ensure each participant gets one secret santa assignment 
    #3. There exists a possible solution where each participant can have a secret santa assignment taking into account each participants ban list 
    #4. Each participant in the file is unique
    participant_list=[]
    file = open(source_path,'r')
    lines = file.readlines()
    for line in lines:
        if line.isspace():
            break
        ban_list = []
        tokens = line.split()
        for i in range(3,len(tokens),2):    
            ban_list.append(tokens[i]+" "+tokens[i+1])
        participant_list.append(Participant(tokens[0]+ " "+tokens[1],tokens[2],ban_list))
    return participant_list

def main(source_path):
    # the section below reads in file and stores all the participants in a list of Participant objects 
    participant_list=generate_participant_list(source_path)
    
    # this section is for determining each participants secret santa using the generate_assignment function
    generate_assignment(participant_list)
    
    # this Final section is the "email section"
    # Minor Assumption while the emails are not sent it is assumed they are real emails 
    for participant in participant_list:
        print ("Notifying "+participant.email+" that he/she is assigned to get a gift for "+participant.assigned_participant+".")
    

# Assumptions 
# 1. Text file in same directory as this script
# 2. The file is provided in the arguments of the scripts, if no file is provided it asks for one and ensure that file exsists 
if __name__ == "__main__":  
    arguments = sys.argv
    current_working_directory = os.getcwd()
    
    if len(arguments) != 2:
        is_valid_file=False
    else:
        file_path = os.path.join(current_working_directory,arguments[1])
        is_valid_file = os.path.isfile(file_path)
    
    #Makes sure a valid file is entered
    while(is_valid_file == False):
        print("Please ensure that you enter one filename and the file exsists in the current directory")
        input_file = input("Enter your value: ").strip()
        file_path = os.path.join(current_working_directory,input_file)
        is_valid_file = os.path.isfile(file_path)
            
    main(file_path)