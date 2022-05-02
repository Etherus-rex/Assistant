
import os


Assistant_Active = True


# Function to check Word Present
def word_is_present(word,char):
    if word.find(char)==-1:
        return('not Found')
    else:
        return('present')



# Function to Open THe Driectories through Python Script
def unfold(route):
    os.startfile(route)



################                        Route              ############################

google = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
cmd = 'C:\\Users\\Rimuru\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk'
vscode = 'C:\\Users\\Rimuru\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
data = 'C:\\Users\\Rimuru\\Desktop\\Data'
anime_dir = 'C:\\Users\\Rimuru\Desktop\\Data\\Anime'
music_dir = 'C:\\Users\\Rimuru\\Desktop\Data\\Music'
filmora = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
emulator = ''
git = 'C:\\Program Files\\Git\\git-bash.exe'
settings = 'C:\\Siesta\\Settings.lnk'
vlc = "C:\\Program Files (x86)\\VideoLAN\VLC\\vlc.exe"
control_pannel = 'C:\\Users\\Rimuru\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk'
playlist_alpha = 'C:\\Siesta\\Alpha_ Music.mp3.xspf'
playlist_beta  = 'C:\\Siesta\\Beta_ Music.mp4.xspf'
playlist_gamma = ''




######    START UP GReet     #####
print('starting')
print('system Protocols initiated')
print('server connection stable')
print('machine state up and running')
print('okay sir , everything looks fine')
print('all systems are initiated without fail')
print('so sir , what do u need me for ?')













while Assistant_Active:

    ai = input("Command : ")
    user_input = ai.lower()

    print(user_input)
    #####       THE OPEN COMMANDS        ######

    if 'open' in user_input:
        print('okay sir')

        print(user_input)
        
        if 'google' in user_input:
            print('activating google chrome')
            unfold(google)
    
        elif word_is_present(user_input,'cmd')=='present':
            print('activating cmd')
            unfold(cmd)
        
        elif word_is_present(user_input,'vscode')=='present':
            print('opennig vs code')
            unfold(vscode)
        
        elif word_is_present(user_input,'code')=='present':
            print('opennig vs code')
            unfold(vscode)



        elif word_is_present(user_input,'data')=='present':
            print('accessing data')
            unfold(data)
        
        elif word_is_present(user_input,'anime')=='present':
            print('opening directory')
            unfold(anime_dir)
        
        elif word_is_present(user_input,'music')=='present':
            print('locating music directory')
            unfold(music_dir)
        
        elif word_is_present(user_input,'filmora')=='present':
            print('activating filmora')
            unfold(filmora)
        
        elif word_is_present(user_input,'vlc')=='present':
            print('firing off vlc')
            unfold(vlc)
        
        elif word_is_present(user_input,'android')=='present':
            unfold(emulator)
        
        elif word_is_present(user_input,'emulator')=='present':
            unfold(emulator)
        
        elif word_is_present(user_input,'git')=='present':
            print('firing of git bash')
            unfold(git)
        
        elif word_is_present(user_input,'bash')=='present':
            print('firing of git bash')
            unfold(git)
        
        elif word_is_present(user_input,'setting')=='present':
            print('opening system settings')
            unfold(settings)
        
        elif word_is_present(user_input,'control pannel')=='present':
            print('activating control pannel')
            unfold(control_pannel)
        
        elif word_is_present(user_input,'youtube')=='present':
            print('opening youtube')
            webbrowser.open('https://youtube.com/')
        
        elif word_is_present(user_input,'gmail')=='present':
            print('accessing gmail account')
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')


       ######     THE FIRE OFF COMMANDS      ######         


    
    elif word_is_present(user_input,'fire off') == 'present':
        
        if word_is_present(user_input,'google')=='present':
            print('firing off google chrome')
            unfold(google)
        
        elif word_is_present(user_input,'cmd')=='present':
            print('firing off cmd')
            unfold(cmd)
        
        elif word_is_present(user_input,'vscode')=='present':
            print('firing off vscode')
            unfold(vscode)
        
        elif word_is_present(user_input,'data')=='present':
            print('firing off data directory')
            unfold(data)
        
        elif word_is_present(user_input,'anime directory')=='present':
            print('firing off anime directory')
            unfold(anime_dir)
        
        elif word_is_present(user_input,'music directory')=='present':
            print('firing off music directory')
            unfold(music_dir)
        
        elif word_is_present(user_input,'filmora')=='present':
            print('firing off filmora')
            unfold(filmora)
        
        elif word_is_present(user_input,'vlc')=='present':
            print('firing off vlc')
            unfold(vlc)
        
        elif word_is_present(user_input,'android')=='present':
            print('emulator')
            unfold(emulator)
        
        elif word_is_present(user_input,'emulator')=='present':
            print('emulator')
            unfold(emulator)
        
        elif word_is_present(user_input,'git')=='present':
            print('firing off git bash')
            unfold(git)
        
        elif word_is_present(user_input,'bash')=='present':
            print('firing off git bash')
            unfold(git)
        
        elif word_is_present(user_input,'setting')=='present':
            print('firing off settings')
            unfold(settings)
        
        elif word_is_present(user_input,'control pannel')=='present':
            print('firing off control panel')
            unfold(control_pannel)
        
        elif word_is_present(user_input,'youtube')=='present':
            print('accessing youtube')
            webbrowser.open('https://youtube.com/')
        
        elif word_is_present(user_input,'gmail')=='present':
            print('accessing gmail')
            webbrowser.open('https://accounts.google.com/b/0/AddMailService')
    
    
    
            ########   THE PLAY COMMANDS    #######


    elif word_is_present(user_input,'play ')=='present':
    
        if word_is_present(user_input,'music alpha')=='present':
            print('playing the alpha series playlist')
            unfold(playlist_alpha)
    
        elif word_is_present(user_input,'music beta')=='present':
            print('playing the beta series playlist')
            unfold(playlist_beta)
     
        elif word_is_present(user_input,'playlist gamma')=='present':
            print('playlist')
            unfold(playlist_gamma)
    
    
     ########      THE GOOGLE SEARCH COMMAND     #######
    
    elif word_is_present(user_input,'search for')=='present':
        print('searching')
        index = user_input.find('search for ') + 11
        info = user_input[index::]
        search(info)

     ############    THE INFORMATION SEARCH  COMMAND  ###########

    elif word_is_present(user_input,'about')=='present':
        print('finding')
        index = user_input.find('about ') + 6
        info = user_input[index::]
        search(info)
    

    ###############          THE YOUTUBE COMMAND         ##############


    elif word_is_present(user_input,'youtube')=='present':
        print('accessing youtube')
        webbrowser.open('https://youtube.com/')
    

    ############         THE GMAIL COMMAND        #################
    
    elif word_is_present(user_input,'gmail')=='present':
        print('accessing gamil')
        webbrowser.open('https://accounts.google.com/b/0/AddMailService')


    ############    THE SHUTDOWN OR EXIT COMMANDS
    
    
    elif word_is_present(user_input,'exit')=='present':
        print('exiting')
        break
    elif word_is_present(user_input,'who are u')=='present':
        print('sir u programmed me i am siesta')
    elif word_is_present(user_input,'your current version')=='present':
        print('my current version is 1.0.1')
    elif word_is_present(user_input,'shutdown')=='present':
        print('shuting down third party')
        break



print('shutting down the core programme')
print('shutting down all other servers and system protocols')
print('if u need something just ask')
print('have a nice time')