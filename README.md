# secret-santa-generator #

## Description ## 
This script is a Secret Santa gift exchange generator. It reads a text file containing a list of people, their email and the people they don't want to send a gift to. Using this information the script assigns each person in the text file an individual to give a gift to, taking into account the people they don't want as their Secret Santa assignment. After this it simulates an email notification by displaying a person's email and the person they were assigned to get a gift for.

## Approach ##
The solution is broken up into four parts. 

The first part involves reading the file. This is done by taking the filename as one of the arguments when running the script. I assumed that the file exists and the file is in the same directory as the script.

The second part involves processing the data in the file and generating a participant list. This list is a list of participant objects which contain all relevant data for each participant like their name, email and ban list. The ban list refers to the people they don't want to send a gift to. The use of objects is to provide more flexibility once the script is complete. So for example the participant list could be extracted as a JSON file to save all relevant data for later use. For this to work some assumptions were taken into account. The assumptions are as follows: 

1. The file contains names in the following format: FirstName LastName email FirstName LastName      FirstName LastName ...
2. The file has an even number of participants to ensure each participant gets one Secret Santa assignment 
3. There exists a possible solution where each participant can have a Secret Santa assignment taking into account each participant's ban list. An example of where this does not occur is when there are two participants and they have each other on their ban list. Then there exists no possible solution where each participant is assigned a Secret Santa. Therefore a situation like this is assumed to not exist in the provided file
4. Each participant in the file is unique

The third part of the script involves assigning each of the participants of the Secret Santa exchange someone they have to give a gift to. This is done by going through the participant list and randomly assigning each participant a valid person to send a gift to. For an assignment to be valid, the person must not already be assigned; they must not be the same as the assignee and they must not appear on the ban list. One minor improvement made to the algorithm is done by sorting the participant list from people with the largest ban list to people with the smallest ban list. This ensures that the people with the smallest pool of valid individuals get first pick from the participants while maintaining the integrity of the randomness from the original algorithm. Finally, there is a small chance that even with this improvement the random assignments result in someone having no valid assignments. In this situation the algorithm is restarted and new assignments are found. The reason for this approach is to maintain both the integrity of the randomness and the simplicity of the design. 

The fourth and final part involves the simulation of the emails being sent to each participant. This is done by going through the participant list and printing a participant's email and who they are assigned to get a gift for. One final minor assumption is that all the email addresses are valid emails.

## How to run ##
Place this script inside a directory containing a text file with the Secret Santa participants in the following format.  
FirstName LastName email FirstName LastName FirstName LastName ...
FirstName LastName email FirstName LastName FirstName LastName ...
FirstName LastName email FirstName LastName FirstName LastName …
…
In the above example, the names after the email are the list of names that the participant does not want to send a gift to. An example of the format can be found in the provided file in this repository. 

Then run this script in the terminal or command line of your computer stating the text file with all the participants in the argument of the command line call. So, for example, using the provided participantsList.txt file the command to run the script on a unix based operating system would be: 

python3 secretSantaGen.py participantsList.txt 
