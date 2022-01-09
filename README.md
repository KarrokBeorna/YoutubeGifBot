# YouTube Gif Bot

## CI

main - [![Build Status](https://app.travis-ci.com/KarrokBeorna/YoutubeGifBot.svg?branch=main)](https://app.travis-ci.com/github/KarrokBeorna/YoutubeGifBot) 
develop - [![Build Status](https://app.travis-ci.com/KarrokBeorna/YoutubeGifBot.svg?branch=develop)](https://app.travis-ci.com/github/KarrokBeorna/YoutubeGifBot) 

YouTube Gif Bot is a bot that sends a gif to the Telegram chat, following a link from YouTube and two timestamps in the 'link mm:ss mm:ss' format.

## Usage:

1. Find YoutubeGifBot in Telegram;

2. Run the script using Docker or just some IDE;

3. To send any message that doesn't start with a link, you will receive an auxiliary message, which will describe how to use the bot:

![](/images/Help_msg.png)

4. And to the message in the form 'link mm:ss mm:ss' you will receive a GIF:

![](/images/First_use.png)

## Some optional parameters:

1. Decrease FPS - 4 input parameter. By default, YouTube has 30 FPS, and with this function you can reduce their number many times (reducing frames by 2 times doesn't really catch the eye, so it can be used).

2. Issuing a gray picture instead of a color one - parameter 5. I think it would be cool:

![](/images/Gray.png)

## Docker:

1. `docker build -t ygb .`
2. `docker run ygb`
3. The bot is running - you can write to it.

![](/images/Docker.png)

## Problems and Recommendations

1. It would be great not to download the full video from YouTube, and FFMPEG can somehow help with this, but I didn't go into details;
2. Since in my implementation the video is downloaded completely, therefore, I think you understand that you shouldn't give the bot some 10-hour video input;
3. You shouldn't give timestamps with a difference of more than 15 seconds, since Telegram may not accept such a GIF.
