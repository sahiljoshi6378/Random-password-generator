import time
import random
game_name=' WELCOME TO :Rock Paper scissors';
for i in game_name:

    time.sleep(0.1)
    print(i, end="");
print();
user_details=[];
Temp_user_name=input('Please Drop your name to Continue -:');
print('Please wait...');
time.sleep(0.6)
should_do1=input(f'Sure you want to continue with this name : {Temp_user_name} : ');
if (should_do1=='yes' or should_do1=='Yes' or should_do1 =='y' or should_do1 =='Y'):
    print("please wait...")
    time.sleep(1);
    print('Adding your name');
    user_details.append(Temp_user_name);
elif (should_do1=='no' or should_do1=='No' or should_do1 =='n' or should_do1 =='N'):
    edited_name=input('OK,Enter your new name :');
    print('Please wait...');
    time.sleep(2);
    user_details.append(edited_name);
else:
    print("SORRY WRONG INPUT ");
    time.sleep(2);
    print('Starting the new process');
    user_details.append(Temp_user_name);
for i in user_details:
    print(i);
time.sleep(1);
print('Let\'s start the game');
Computer_name='MR. butler';
time.sleep(1.5);
print(f'Hey, meet our computer:{Computer_name}');
computer_selections=['rock','paper','sicer'];
game_mode=True;
game_stop=6;
userPoints=[];
computerPoints=[];
while (game_mode):
    game_stop=game_stop-1;
    if(game_stop!=0):
        compute_play = random.choice((computer_selections));
        use_play = input('Enter your input :');
        if (use_play == 'r' and compute_play == 'paper'):
            print('Ckeecking..')
            time.sleep((1.5));
            userPoints.append(1);
            print('you won!');
        elif (use_play == 'p' and compute_play == 'scissors'):
            print('Ckeecking..')
            time.sleep((1.5));
            computerPoints.append(1);
            print('you loose');
        elif (use_play == 's' and compute_play == 'rock'):
            print('Ckeecking..')
            time.sleep((1.5));
            computerPoints.append(1);
            print('you loose');
        elif (use_play == 'r' and compute_play == 's'):
            print('Ckeecking..')
            time.sleep((1.5));
            userPoints.append(1);
            print('you won');
        elif (use_play == 'p' and compute_play == 's'):
            print('Ckeecking..')
            time.sleep((1.5));
            computerPoints.append(1);
            print('you loose');
        elif (use_play == 'r' and compute_play == 'rock'):
            print('Ckeecking..')
            time.sleep((1.5));
            print('you both had tia');
        elif (use_play == 'p' and compute_play == 'paper'):
            print('Ckeecking..')
            time.sleep((1.5));
            print('you both had tia');
        elif (use_play == 's' and compute_play == 'scissors'):
            print('Ckeecking..')
            time.sleep((1.5));
            print('you both had tia');
        elif (use_play == 'p' and compute_play == 'rock'):
            print('Ckeecking..')
            time.sleep((1.5));
            userPoints.append(1);
            print('you won!');
        elif (use_play == 's' and compute_play == 'paper'):
            print('Ckeecking..')
            time.sleep((1.5));
            userPoints.append(1);
            print('you won!');
        elif (use_play == 'r' and compute_play == 'scissors'):
            print('Ckeecking..')
            time.sleep((1.5));
            userPoints.append(1);
            print('you won!');
        else:
            print('Ckeecking..')
            time.sleep((1.5));
            print('it looks you entred Wrong Input');
            print('Shutting Down the System...');
            time.sleep(2);
            exit()
    elif(game_stop==0):
        print('OK You have used all 5 chances');
        time.sleep(1.3);
        print('Now let\'s cheeck who won');
        print('Shutting down the System...');
        time.sleep(2);
        game_mode=False;
comp_won=len(computerPoints);
user_won=len(userPoints);
if comp_won>user_won:
    print('Computer won')
    print('And you loose');
    print(comp_won)
    print(computerPoints)
    print(user_won)
    print(userPoints);
elif comp_won<user_won:
    print(f'{Temp_user_name} won')
    print(f'And {Computer_name} loose');
    print(comp_won)
    print(computerPoints)
    print(user_won)
    print(userPoints);




