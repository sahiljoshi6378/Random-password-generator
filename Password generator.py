import string
import  random
import time
string_abc=string.ascii_lowercase;
string_ABC=string.ascii_uppercase;
string_123=string.digits;
strint_special=string.punctuation;

complet_string_list=[];
complet_string_list.extend(list(strint_special));
complet_string_list.extend(list(string_abc));
complet_string_list.extend(list(string_ABC));
complet_string_list.extend(list(string_123));
random.shuffle(complet_string_list);
# print(complet_string_txt[0:5]);
user_input=int(input('Please enter password lenght :'))
if user_input >78:
    print('WRONG INPUT');
    exit();
elif user_input<=8:
    print('TIP -: You should use a stronger password')
    user_input2=int(input('Please increase the password lenght -:'));
    random.shuffle(complet_string_list);
    complet_string_txt = (''.join(complet_string_list));
    time.sleep(1);
    print('Please wait...');
    time.sleep(0.3);
    print('Creating your new password...');
    time.sleep(0.5);
    print(F'YOUR NEW PASSWORD -: {complet_string_txt[0:user_input2]}');
    time.sleep(0.3);
    print('THANKS FOR USING OUR PWD GENERATOR ');
elif user_input >8:
    random.shuffle(complet_string_list);
    complet_string_txt = (''.join(complet_string_list));
    time.sleep(1);
    print('Please wait...');
    time.sleep(0.3);
    print('Creating your new password...');
    time.sleep(0.5);
    print(F'YOUR NEW PASSWORD -: {complet_string_txt[0:user_input]}');
    time.sleep(0.3);
    print('THANKS FOR USING OUR PWD GENERATOR ');

else:
    exit();
