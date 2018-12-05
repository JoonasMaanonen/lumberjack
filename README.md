# Bot that can play the Telegram bot game Lumberjack

## Story
I hacked this bot together when this lumberjack game was popular in our guilds Telegram chat. 
It can get scores of ~150, which is OK but humans can still beat it easily, if they practice the game a bit. Maybe if I had more time I could try to make it smarter.

## Implementation
This bot is very basic. As there's no output other than the image from the game, the bot just takes screenshots of the game and scans specific pixel locations for trees.

This puts a hard limit to the performance of the bot, since the animation has to end before we can spot a tree

## Top Score
![alt text](bot_top_score.png)

