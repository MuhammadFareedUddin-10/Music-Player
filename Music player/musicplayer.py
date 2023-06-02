from playsound import playsound

print ("NO. of available songs\n1.dark-underworld-144813\n2.exosphere-144815\n3.psychedelic-144822\n4.fading-memories-144816fa")
order = input ('Enter the music which you want to play: ')
if "dark-underworld-144813" in order:
    playsound('F:\\Music player\\dark-underworld-144813.mp3')
elif "exosphere-144815" in order:
    playsound('F:\\Music player\\exosphere-144815.mp3')
elif "psychedelic-144822" in order:
    playsound('F:\\Music player\\psychedelic-144822.mp3')
elif "fading-memories-144816" in order:
    playsound('F:\\Music player\\fading-memories-144816.mp3')
