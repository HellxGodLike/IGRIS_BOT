[IGRIS](https://wallpapercave.com/wp/wp4275385.jpg) 
# IGRIS_BOT
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6141417ceaf84545bab6bd671503df51)](https://app.codacy.com/gh/AnimeKaizoku/SaitamaRobot?utm_source=github.com&utm_medium=referral&utm_content=AnimeKaizoku/SaitamaRobot&utm_campaign=Badge_Grade_Settings)  [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://perso.crans.org/besson/LICENSE.html) [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com) [![Updates channel!](https://img.shields.io/badge/Join%20Channel-!-red)](https://t.me/IGRIS_BOT1)


A modular Telegram Python bot running on python3 with a sqlalchemy database.

Originally a Marie fork, Saitama evolved further and was built to be more robust and more dedicated to Anime Chats. 

Can be found on telegram as [IGRIS_BOT](https://t.me/IGRIS_BOT).

The Support group can be reached out to at [IGRIS_BOT Support](https://t.me/IGRIS_SUPPORT), where you can ask for help about [IGRIS_BOT](https://t.me/IGRIS_BOT), discover/request new features, report bugs, and stay in the loop whenever a new update is available. 

News channel as at [SOME ASSOCIATION](https://t.me/IGRIS_BOT1) 

## How to setup/deploy.

### Read these notes carefully before proceeding 

 - Your code must be open source and a link to your fork's repository must be there in the start reply of the bot. [See this](https://github.com/AnimeKaizoku/SaitamaRobot/blob/shiken/SaitamaRobot/__main__.py#L25)
 - Lastly, if you are found to run this repo without the code being open sourced or the repository link not mentioned in the bot, we will push a gban for you in our network because of being in violation of the license, you are free to be a dick and not respect the open source code (we do not mind) but we will not be having you around our chats.


<details>
  <summary>Steps to deploy on Heroku !! </summary>

```
Fill in all the details, Deploy!
Now go to https://dashboard.heroku.com/apps/(app-name)/resources ( Replace (app-name) with your app name )
Turn on worker dyno (Don't worry It's free :D) & Webhook
Now send the bot /start, If it doesn't respond go to https://dashboard.heroku.com/apps/(app-name)/settings and remove webhook and port.
```

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HellxGodLike/IGRIS_BOT.git)

</details>  
<details>
  <summary>Steps to self Host!! </summary>

Note: This instruction set is just a copy-paste from Marie, note that [One Punch Support](https://t.me/OnePunchSupport) aims to handle support for @SaitamaRobot and not how to set up your own fork. If you find this bit confusing/tough to understand then we recommend you ask a dev, kindly avoid asking how to set up the bot instance in the support chat, it aims to help our own instance of the bot and not the forks.

  ## Setting up the bot (Read this before trying to use!):
Please make sure to use python3.6, as I cannot guarantee everything will work as expected on older Python versions!
This is because markdown parsing is done by iterating through a dict, which is ordered by default in 3.6.

  ### Configuration

There are two possible ways of configuring your bot: a config.py file, or ENV variables.

The preferred version is to use a `config.py` file, as it makes it easier to see all your settings grouped together.
This file should be placed in your `SaitamaRobot` folder, alongside the `__main__.py` file. 
This is where your bot token will be loaded from, as well as your database URI (if you're using a database), and most of 
your other settings.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all 
