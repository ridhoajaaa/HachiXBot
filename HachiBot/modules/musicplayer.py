__help__ = """
🔘 Setting up.
❍ Make bot admin.
❍ Invite Assistant with type /userbotjoin or ask at @demonszxx for assistant.
❍ Start a voice chat.
❍ Try /play [song name] for the first time by an admin.
❍ If userbot joined enjoy music, If not add manually to your group and retry.

🔘 Commands.

⇝ Auth User

Note :
-Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.

/auth [Username or Reply to a Message] 
- Add a user to AUTH LIST of the group.

/unauth [Username or Reply to a Message] 
- Remove a user from AUTH LIST of the group.

/authusers 
- Check AUTH LIST of the group.

⇝ Blacklist

/blacklistedchat 
- Check Blacklisted Chats of Bot.


Note:
Only for Sudo Users.

/blacklistchat [CHAT_ID] 
- Blacklist any chat from using Music Bot

/whitelistchat [CHAT_ID] 
- Whitelist any blacklisted chat from using Music Bot


⇝ Join/Leave

Note:
Only for Sudo Users

/joinassistant [Chat Username or Chat ID]
- Join assistant to a group.

/leaveassistant [Chat Username or Chat ID]
- Assistant will leave the particular group.

/leavebot [Chat Username or Chat ID]
- Bot will leave the particular chat.


⇝ Playlist

/playplaylist 
- Start playing Your Saved Playlist.

/playlist 
- Check Your Saved Playlist On Servers.

/delmyplaylist
- Delete any saved music in your playlist

/delgroupplaylist
- Delete any saved music in your group's playlist [Requires Admin Rights.]


⇝ Server

Note:
Only for Sudo Users

/get_log
- Get log of last 100 lines from Heroku.

/get_var
- Get a config var from Heroku or .env.

/del_var
- Delete any var on Heroku or .env.

/set_var [Var Name] [Value]
- Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

/usage
- Get Dyno Usage.

/update
- Update Your Bot.

/restart 
- Restart Bot [All downloads, cache, raw files will be cleared too].


⇝ Speedtest

/speedtest 
- Check Server Latency and Speed.


⇝ Stats

/stats
- Check the Stats of Bot.
- Gets the stat of MongoDb , Assistant, System etc


⇝ SudoUsers

/sudolist 
    Check the sudo user list of Bot. 


Note:
Only for Sudo Users. 

/addsudo [Username or Reply to a user]
- To Add A User In Bot's Sudo Users.

/delsudo [Username or Reply to a user]
- To Remove A User from Bot's Sudo Users.

/maintenance [enable / disable]
- When enabled Bot goes under maintenance mode. No one can play Music now.

/logger [enable / disable]
- When enabled Bot logs the searched queries in logger group.

/clean
- Clean Temp Files and Logs.


⇝ Theme

/settheme
- Set a theme for thumbnails.

/theme
- Check Theme for your chat.


⇝ Video/Stream

/play [Reply to any Video] or [YT Link] or [Music Name]
- Stream Video on Voice Chat

For Sudo User:-

/set_video_limit [Number of Chats]
- Set a maximum Number of Chats allowed for Video Calls at a time.


⇝ Voice Chat

/pause
- Pause the playing music on voice chat.

/resume
- Resume the paused music on voice chat.

/skip
- Skip the current playing music on voice chat

/end or /stop
- Stop the playout.

/queue
- Check queue list.


Note:
Only for Sudo Users

/activevc
- Check active voice chats on bot.

/activevideo
- Check active video calls on bot.


⇝ Assistant.

Note :
- Only for Sudo Users

.block [ Reply to a User Message] 
- Blocks the User from Assistant Account.

.unblock [ Reply to a User Message] 
- Unblocks the User from Assistant Account.

.approve [ Reply to a User Message] 
- Approves the User for DM.

.disapprove [ Reply to a User Message] 
- Disapproves the User for DM.

.pfp [ Reply to a Photo] 
- Changes Assistant account PFP.

.bio [Bio text] 
- Changes Bio of Assistant Account.


𝕣𝕖𝕒𝕕  𝕗𝕣𝕠𝕞  𝕥𝕠𝕡  𝕓𝕖𝕓𝕪  𝕒𝕟𝕛𝕘 ❤️.
"""
__mod_name__ = "Music Player"
