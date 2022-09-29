from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests 
from time import time , ctime

updater = Updater("5744768131:AAHzb_51eN6by0VJbajp0Oa-Rh-E3tP16wA",
				use_context=True)

 


def start(update: Update, context: CallbackContext):
		update.message.reply_text(
		"""
        Type /help To View All The Categories
        (Pro tip: You can run any command by just clicking it!!)
        /random
        -------------
        In case if any bug or query,
        contact dev @Arhamsayyed\
            or /Contact_Dev
         """)
         

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """

/random
/neko   
/shinobu
/megumin
/bully  
/cuddle 
/cry    
/hug    
/awoo   
/kiss
/lick
/pat
/smug
/bonk
/yeet
/blush
/smile
/wave
/highfive
/handhold
/nom
/bite
/glomp
/slap
/kill
/happy
/wink
/poke
/dance

        """)

# ''''''''''''''''''''' all sfw '''''''''''''''''''''''''
sfw_url = "https://api.waifu.pics/"
# print(sfw_url + "sfw/waifu") 


def random(update: Update, context: CallbackContext):
    random_waifu = sfw_url + "sfw/waifu"
    waifu_raw_url = requests.get(random_waifu)
    waifu = waifu_raw_url.json()['url']
    update.message.reply_photo(photo=waifu)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def neko(update: Update, context: CallbackContext):
    random_neko = sfw_url + "sfw/neko"
    neko_raw_url = requests.get(random_neko)
    neko = neko_raw_url.json()['url']
    update.message.reply_photo(photo=neko)   
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def shinobu(update: Update, context: CallbackContext):
    random_shinobu = sfw_url + "sfw/shinobu"
    shinobu_raw_url = requests.get(random_shinobu)
    shinobu = shinobu_raw_url.json()['url']
    update.message.reply_photo(photo=shinobu)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def megumin(update: Update, context: CallbackContext):
    random_megumin = sfw_url + "sfw/megumin"
    megumin_raw_url = requests.get(random_megumin)
    megumin = megumin_raw_url.json()['url']
    update.message.reply_photo(photo=megumin)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def bully(update: Update, context: CallbackContext):
    random_bully = sfw_url + "sfw/bully"
    bully_raw_url = requests.get(random_bully)
    bully = bully_raw_url.json()['url']
    update.message.reply_video(video=bully)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def cuddle(update: Update, context: CallbackContext):
    random_cuddle = sfw_url + "sfw/cuddle"
    cuddle_raw_url = requests.get(random_cuddle)
    cuddle = cuddle_raw_url.json()['url']
    update.message.reply_video(video=cuddle)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def cry(update: Update, context: CallbackContext):
    random_cry = sfw_url + "sfw/cry"
    cry_raw_url = requests.get(random_cry)
    cry = cry_raw_url.json()['url']
    update.message.reply_video(video=cry)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def hug(update: Update, context: CallbackContext):
    random_hug = sfw_url + "sfw/hug"
    hug_raw_url = requests.get(random_hug)
    hug = hug_raw_url.json()['url']
    update.message.reply_video(video=hug)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def awoo(update: Update, context: CallbackContext):
    random_awoo = sfw_url + "sfw/awoo"
    awoo_raw_url = requests.get(random_awoo)
    awoo = awoo_raw_url.json()['url']
    update.message.reply_photo(photo=awoo)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    


def kiss(update: Update, context: CallbackContext):
    random_kiss = sfw_url + "sfw/kiss"
    kiss_raw_url = requests.get(random_kiss)
    kiss = kiss_raw_url.json()['url']
    update.message.reply_video(video=kiss)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def lick(update: Update, context: CallbackContext):
    random_lick = sfw_url + "sfw/lick"
    lick_raw_url = requests.get(random_lick)
    lick = lick_raw_url.json()['url']
    update.message.reply_video(video=lick)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def pat(update: Update, context: CallbackContext):
    random_pat = sfw_url + "sfw/pat"
    pat_raw_url = requests.get(random_pat)
    pat = pat_raw_url.json()['url']
    update.message.reply_video(video=pat)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def smug(update: Update, context: CallbackContext):
    random_smug = sfw_url + "sfw/smug"
    smug_raw_url = requests.get(random_smug)
    smug = smug_raw_url.json()['url']
    update.message.reply_video(video=smug)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def bonk(update: Update, context: CallbackContext):
    random_bonk = sfw_url + "sfw/bonk"
    bonk_raw_url = requests.get(random_bonk)
    bonk = bonk_raw_url.json()['url']
    update.message.reply_video(video=bonk)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def yeet(update: Update, context: CallbackContext):
    random_yeet = sfw_url + "sfw/yeet"
    yeet_raw_url = requests.get(random_yeet)
    yeet = yeet_raw_url.json()['url']
    update.message.reply_video(video=yeet)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def blush(update: Update, context: CallbackContext):
    random_blush = sfw_url + "sfw/blush"
    blush_raw_url = requests.get(random_blush)
    blush = blush_raw_url.json()['url']
    update.message.reply_video(video=blush)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def smile(update: Update, context: CallbackContext):
    random_smile = sfw_url + "sfw/smile"
    smile_raw_url = requests.get(random_smile)
    smile = smile_raw_url.json()['url']
    update.message.reply_video(video=smile)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def wave(update: Update, context: CallbackContext):
    random_wave = sfw_url + "sfw/wave"
    wave_raw_url = requests.get(random_wave)
    wave = wave_raw_url.json()['url']
    update.message.reply_video(video=wave)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def highfive(update: Update, context: CallbackContext):
    random_highfive = sfw_url + "sfw/highfive"
    highfive_raw_url = requests.get(random_highfive)
    highfive = highfive_raw_url.json()['url']
    update.message.reply_video(video=highfive)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def handhold(update: Update, context: CallbackContext):
    random_handhold = sfw_url + "sfw/handhold"
    handhold_raw_url = requests.get(random_handhold)
    handhold = handhold_raw_url.json()['url']
    update.message.reply_video(video=handhold)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def nom(update: Update, context: CallbackContext):
    random_nom = sfw_url + "sfw/nom"
    nom_raw_url = requests.get(random_nom)
    nom = nom_raw_url.json()['url']
    update.message.reply_video(video=nom)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def bite(update: Update, context: CallbackContext):
    random_bite = sfw_url + "sfw/bite"
    bite_raw_url = requests.get(random_bite)
    bite = bite_raw_url.json()['url']
    update.message.reply_video(video=bite)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def glomp(update: Update, context: CallbackContext):
    random_glomp = sfw_url + "sfw/glomp"
    glomp_raw_url = requests.get(random_glomp)
    glomp = glomp_raw_url.json()['url']
    update.message.reply_video(video=glomp)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def slap(update: Update, context: CallbackContext):
    random_slap = sfw_url + "sfw/slap"
    slap_raw_url = requests.get(random_slap)
    slap = slap_raw_url.json()['url']
    update.message.reply_video(video=slap)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def kill(update: Update, context: CallbackContext):
    random_kill = sfw_url + "sfw/kill"
    kill_raw_url = requests.get(random_kill)
    kill = kill_raw_url.json()['url']
    update.message.reply_video(video=kill)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def kick(update: Update, context: CallbackContext):
    random_kick = sfw_url + "sfw/kick"
    kick_raw_url = requests.get(random_kick)
    kick = kick_raw_url.json()['url']
    update.message.reply_video(video=kick)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def happy(update: Update, context: CallbackContext):
    random_happy = sfw_url + "sfw/happy"
    happy_raw_url = requests.get(random_happy)
    happy = happy_raw_url.json()['url']
    update.message.reply_video(video=happy)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def wink(update: Update, context: CallbackContext):
    random_wink = sfw_url + "sfw/wink"
    wink_raw_url = requests.get(random_wink)
    wink = wink_raw_url.json()['url']
    update.message.reply_video(video=wink)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def poke(update: Update, context: CallbackContext):
    random_poke = sfw_url + "sfw/poke"
    poke_raw_url = requests.get(random_poke)
    poke = poke_raw_url.json()['url']
    update.message.reply_video(video=poke)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def dance(update: Update, context: CallbackContext):
    random_dance = sfw_url + "sfw/dance"
    dance_raw_url = requests.get(random_dance)
    dance = dance_raw_url.json()['url']
    update.message.reply_video(video=dance)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    


def cringe(update: Update, context: CallbackContext):
    random_cringe = sfw_url + "sfw/cringe"
    cringe_raw_url = requests.get(random_cringe)
    cringe = cringe_raw_url.json()['url']
    update.message.reply_video(video=cringe)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    


#################$$$$ nsfw $$$$########################

def waifu_n(update: Update, context: CallbackContext):
    random_waifu_n = sfw_url + "nsfw/waifu"
    waifu_n_raw_url = requests.get(random_waifu_n)
    waifu_n = waifu_n_raw_url.json()['url']
    update.message.reply_photo(photo=waifu_n)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def neko_n(update: Update, context: CallbackContext):
    random_neko_n = sfw_url + "nsfw/neko"
    neko_n_raw_url = requests.get(random_neko_n)
    neko_n = neko_n_raw_url.json()['url']
    update.message.reply_photo(photo=neko_n)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def trap(update: Update, context: CallbackContext):
    random_trap = sfw_url + "nsfw/trap"
    trap_raw_url = requests.get(random_trap)
    trap = trap_raw_url.json()['url']
    update.message.reply_photo(photo=trap)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    

def bj(update: Update, context: CallbackContext):
    random_bj = sfw_url + "nsfw/blowjob"
    bj_raw_url = requests.get(random_bj)
    bj = bj_raw_url.json()['url']
    update.message.reply_video(video=bj)
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    






def v_vxcpbo(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
⋈⋈⋈⋈⋈⋈⋈⋈⋈
Hello sir,==>
I Am Happy To See You!
You Can Choose Any Of These Commands

/waifu_n   
/neko_n
/trap
/bj

Thankyou Sir,
⋈⋈⋈⋈⋈⋈⋈⋈⋈
"""
    )
    print(update.message.from_user.username , update.message.chat_id , update.message.text)
    file = open("logfile.txt" , "a")
    current_DateTime = time()
    file.write("[" + str(ctime(current_DateTime)) + "]: " + str(update.message.from_user.username) + " " + str(update.message.chat_id) + " " + str(update.message.text + "\n"))
    file.close()
    







def Contact_Dev(update: Update, context: CallbackContext):
	update.message.reply_text("Developer's Contact =>\
	@Arhamsayyed \
        https://t.me/Arhamsayyed")
        

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command , contactDev?" % update.message.text)
        

def unknown_text(update: Update, context: CallbackContext):
		update.message.chat_id(
        "Sorry I can't recognize you , you said '%s' contactDev?" % update.message.text , chat_id=1423043294)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('random', random))
updater.dispatcher.add_handler(CommandHandler('neko', neko))
updater.dispatcher.add_handler(CommandHandler('shinobu' , shinobu))
updater.dispatcher.add_handler(CommandHandler('megumin' , megumin))
updater.dispatcher.add_handler(CommandHandler('bully' , bully))
updater.dispatcher.add_handler(CommandHandler('cuddle' , cuddle))
updater.dispatcher.add_handler(CommandHandler('cry' , cry))
updater.dispatcher.add_handler(CommandHandler('hug' , hug))
updater.dispatcher.add_handler(CommandHandler('awoo' , awoo))
updater.dispatcher.add_handler(CommandHandler('kiss' , kiss))
updater.dispatcher.add_handler(CommandHandler('lick' , lick))
updater.dispatcher.add_handler(CommandHandler('pat' , pat))
updater.dispatcher.add_handler(CommandHandler('smug' , smug))
updater.dispatcher.add_handler(CommandHandler('bonk' , bonk))
updater.dispatcher.add_handler(CommandHandler('yeet' , yeet))
updater.dispatcher.add_handler(CommandHandler('blush' , blush))
updater.dispatcher.add_handler(CommandHandler('smile' , smile))
updater.dispatcher.add_handler(CommandHandler('wave' , wave))
updater.dispatcher.add_handler(CommandHandler('highfive',highfive))
updater.dispatcher.add_handler(CommandHandler('handhold',handhold))
updater.dispatcher.add_handler(CommandHandler('nom',nom))
updater.dispatcher.add_handler(CommandHandler('bite',bite))        
updater.dispatcher.add_handler(CommandHandler('glomp',glomp))      
updater.dispatcher.add_handler(CommandHandler('slap',slap))        
updater.dispatcher.add_handler(CommandHandler('kill',kill))        
updater.dispatcher.add_handler(CommandHandler('happy',happy))      
updater.dispatcher.add_handler(CommandHandler('wink',wink))        
updater.dispatcher.add_handler(CommandHandler('poke',poke))
updater.dispatcher.add_handler(CommandHandler('dance',dance))
updater.dispatcher.add_handler(CommandHandler('cringe',cringe))

# __________________________________ $$nsfw$$ ___________________________________________

updater.dispatcher.add_handler(CommandHandler('v_vxcpbo',v_vxcpbo))
updater.dispatcher.add_handler(CommandHandler('waifu_n',waifu_n))
updater.dispatcher.add_handler(CommandHandler('neko_n',neko_n))
updater.dispatcher.add_handler(CommandHandler('trap',trap))
updater.dispatcher.add_handler(CommandHandler('bj',bj))



updater.dispatcher.add_handler(CommandHandler('Contact_Dev', Contact_Dev))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown comm
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

def log(update: Update, context: CallbackContext):
    file = open("testfile.txt" , "a") 
    file.write(str(update.message.from_user.username) + str(update.message.chat_id) + str(update.message.text + "\n"))
    file.close()
    



updater.start_polling()
print("polling started...")
