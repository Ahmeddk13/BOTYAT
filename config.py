token = "EAANAV3M5zh0BO6Ag1s5qRgU0OkudimId5hVZBhejvb2P5qiEvu4zjhZCP3tcnD7iBpctKX45uesrQBEkZAk5g2KHnWYh4IvZAlklTkFZAGdo6RAExdOCBOx7yaTiZBtsfLVMWa9cpbPNKQH1WbFMc1CESzoZCfn0xvlKO6zs89FJgIsanV14YDNoZABHZChlgjHkG"
namebot = "ｂｏｔｙａｔ"
start_down = "ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ sᴛᴀʀᴛᴇᴅ📟📥"
end_down = "ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ ғɪɴɪꜱʜᴇᴅ📟✅"
how_to_use = "\n  ★彡ʜᴏᴡ ᴛᴏ ᴜsᴇ ?彡★  \n♠ᴊᴜsᴛ ᴛʏᴘᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ\nᴛʜᴇ ᴠɪᴅᴇᴏ ᴀɴᴅ ᴡᴀɪᴛ ғᴏʀ\nᴛʜᴇ sᴇᴀʀᴄʜ ʀᴇsᴜʟᴛs ᴏʀ ᴡʀɪᴛᴇ \n♠/ʏᴛ <ᴠɪᴅᴇᴏ ᴜʀʟ>"
ownerfb = "https://www.facebook.com/Mr12PAIN"
owner_name = "ᴍʀ-ᴘᴀɪɴ"
search = "ʙᴏᴛ ꜱᴛᴀʀᴛ ꜱᴇᴀʀᴄʜɪɴɢ📟🔎..."
error_vid = "sᴏʀʀʏ✋, ᴛʜᴇ sɪᴢᴇ ᴏғ ᴛʜɪs ᴠɪᴅᴇᴏ ɪs ᴛᴏᴏ ʙɪɢ, ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ᴠɪᴅᴇᴏ❌😩"
error = "error please try again"
#get the api key from google api keys
ytapi = "AIzaSyC1nSaFT3emN9B1fMuuh2W_PnnprzODEfA"
#do not edit here any thing 
url = "https://www.googleapis.com/youtube/v3/search"
def param(text):
    par = {
        'key': ytapi,
        'part': 'id,snippet',
        'type': 'video',
        'q': text,
        'maxResults':'10'}
    return par
def save_db(data=""): 
    file = open("db.txt","w")
    file.write("\n"+data)
def load_db():
    file = open("db.txt","r")
    return file.read()
#end of the code
