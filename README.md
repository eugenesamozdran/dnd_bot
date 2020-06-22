This is my project for practice. I wanted to learn how to make a simple bot from scratch and set up interaction with MySQL database.
It is called "dnd helper" because it helps to quickly find tricky info from the rules of "Dungeons and Dragons" - tabletop RPG which I like a lot.

The bot is available at https://t.me/dnd_assistant_bot

It is deployed to DigitalOcean droplet with apache server installed.

Sent and received messages are handled by Python script. Bot takes info for sending answers from MySQL database on the same server.

Database was created using MySQL Workbench, CSV file can be found in the repository.


You would need to install Flask and mysql.connector libraries to run this on your machine. Of course, you would also need to create your own basic Telegram bot via @BotFather in order to have access to unique bot token.
