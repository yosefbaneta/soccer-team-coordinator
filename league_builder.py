import csv

## this is to stop the program from running if imported
if __name__=='__main__':
    ##opening the csv file
    with open('soccer_players.csv','r') as mainfile:
        file=csv.reader(mainfile,delimiter='|')
        ##converting the data from the csv file to list
        file=list(file)
        
        experience=[] ## this list is to store the names of the experienced players
        
        noexperience=[]## this list is to store the names of the unexperienced  players
        
        for i in  range(1,len(file)):## this loop loops through our file so we can work on each of the items
            answer=file[i]
            answerr=''.join(answer)
            
            li=(answerr.split(','))## 
            li.remove(li[1])

            ## differentiating the experienced and the un experienced players
            if 'YES' in  li:
                experience.append(li)
            else:
                noexperience.append(li)

       
        ## here i created a list for each team which will be used when i split the players 
        sharks=[]
        dragons=[]
        raptors=[]
        teams={}## this dictionary is for saving the players name as a key and their team as a value so i can
                 ## easily know which player is in which team
        
        
        for j in range(3):## this for loop is for splitting the players in to three teams

            ## here i assign equal number of players to the three teams and at the same time i save the players name
            ## and the team in a dictionary
            sharks.append(experience[j])
            teams[experience[j][0]]='sharks'
            
            sharks.append(noexperience[j])
            teams[noexperience[j][0]]='sharks'

            dragons.append(experience[j+3])
            teams[experience[j+3][0]]='dragons'
            
            dragons.append(noexperience[j+3])
            teams[noexperience[j+3][0]]='dragons'

            raptors.append(experience[j+6])
            teams[experience[j+6][0]]='raptors'

            
            raptors.append(noexperience[j+6])

            teams[noexperience[j+6][0]]='raptors'


        ## here i put the list of players in the teams in a text file
        txfile=open('teams.txt','a')
        txfile.write('\n............LIST OF TEAMS.................      \n')

        txfile.write('\n\n         Sharks\n\n')
        txfile=open('teams.txt','a')
        for item in sharks:
            
           
            txfile.write(','.join(item)+'\n\n')
        txfile=open('teams.txt','a')       
        txfile.write('\n\n         Dragons\n\n')
        txfile=open('teams.txt','a')
        for item in dragons:
            
            txfile.write(','.join(item)+'\n\n')

        txfile.write('\n\n         Raptors\n\n')
        
        txfile=open('teams.txt','a')
        for item in raptors:
            txfile=open('teams.txt','a')
            
            txfile.write(','.join(item)+'\n\n')
        txfile=open('teams.txt','a')


        with open('soccer_players.csv','r') as mainfile:
            file=csv.reader(mainfile,delimiter='|')
            file=list(file)
            experience=[]
            noexperience=[]
            for i in  range(1,len(file)):

                answer=file[i]
                answerr=''.join(answer)
                li=(answerr.split(','))
                li.remove(li[1])

                 ## here i create the welcome texts for all of the players
                for i in range (18):
                    name=li[0].lower().split()## here i make the name of the player all small letters
                    final_name=str(name[0])+'_'+str(name[1])## here i insert the underscore in the name 
                    players_welcome= open(str(final_name)+'.txt','w')
                    players_welcome.write('Dear   '+str(li[2]))
                    players_welcome.write('\n\nplayers name: '+str(li[0]))

                    players_welcome.write('\n\nTeam: '+str(teams[li[0]]))

                    players_welcome.write('\n\nFirst training will be held on 3/25/2019, at 2:00PM')

        
            
            
                
            
            
       

        



    



    
                
                


            

      
            
            
            
                    
            
            
            
            
            
            
            
            
