```
❓How to create a bot?
🔹Answer: /tutorials__create_bot


```
```
❓How to change profile pic and description?

Go to @BotFather and use these commands:
/setuserpic - to change bot's profile picture
/setdescription - to change the text that you see when you first open the bot (the one that's above the Start button).
/setabouttext - to change the description inside bot's profile
/setname - to change bot's name

Go to @Manybot and use /setdescription to change the description that a user gets after he/she presses 'Start'.


```
```
❓How to create custom commands?
Go to your bot and use /commands command to create your own commands (no pun intended).


```
```
❓How to make my bot's menu beautiful?
Go to your bot, use /commands command and then press "Configure menu" to change the look of your menu.


```
```
❓How to set up autoposting?


1)Go to your bot.
2)Press Set Up Autoposting.
3)Select the source channel.
4)Send a link or an account name, depending on the source.
5)Done!
You can connect up to 11 parallel autoposting feeds! 😱😎

2 Twitter accounts.
2 YouTube channels.
2 VK publics.
5 RSS feeds.

Did you know that there are two modes of RSS autoposting available?
(1) Only headers; (2) Full posts. You can change this setting inside the same section (look for the command in the message body).


```
```
❓How to disable the Main Menu?

Delete all the menu items from the Main Menu and it will disappear. Your users will see only their keyboard. To delete menu items from Main Menu go to Custom Commands ➡️Config. Main Menu. Select every menu item one by one and press Remove From Menu.

Note that you are the bot creator and you’ll still see the admins menu to manage your bot.


```
```
❓How to create a dropdown list of commands when user types “/“?

You need to use @BotFather 👴🏽 to configure the dropdown command list. Go to him, use “setcommands” command, choose a bot and then send the command list in the following format:

command1 - Description
command2 - Another description
…etc.

Your dropdown command list will become available in the next 5 minutes.


```
```
❓How to create a submenu for a custom command?

Now every custom command can have it’s own submenu! To create a submenu of a custom command go to Custom Commands ➡️/your_command ➡️Configure Menu. The interface is the same as when editing the main menu. You can add buttons, change their names, layout, and create multilevel menus.

After you are done your submenu will appear when anyone sends “/your_command” 🌟


```
```
❓Will menus and submenus disturb users in group chats?

When user talks with a bot only he/she sees the bot’s menu. It doesn’t interfere with other participants of the group chat. Also, for bots without main menu that prefer dropdown command list, we configured the submenus to disappear after users chooses a command. This allows them to use the bot’s submenus without switching back and forth between menus and keyboard.


```
```
❓What is menu mode of a menu item?

Menu modes allow your to control where user will be transferred after he/she pressed a menu item.

There are two menu modes: Fixed and Disappearing.

Fixed menu mode: After selecting a menu item user will stay in the current menu.

Disappearing menu mode: After selecting a menu item user will be transferred back to the Main Menu.


```
```
❓How to change menu mode of a menu item?

To change the menu mode of a menu item: 1. Go to Custom Commands -> Config. Main Menu
2. Enter into the desired submenu.
3. Select the command for which you want to change the menu mode.
4. Find the “Menu mode: Fixed” button (scroll the keyboard to see it).
5. Press it to change the menu mode to “Disappearing” (or vice versa).
6. Done!

💭 EXAMPLE

For example, let’s say you have a menu like this: 1.📱Wallpapers
- 1.1 🌷 Nature
- 1.2 🚘 Cars
- 1.3 🌠 Space

You want users who entered “📱Wallpapers” section to be able to repeatedly press submenu buttons without ever leaving the section.

To do this, you will need to go to the Custom Commands -> Config. Main Menu -> go inside the submenu “📱Wallpapers” and select one by one “🌷 Nature”, “🚘 Cars” and “🌠 Space” and change the menu mode for each of them.

This granular setting allows you to have buttons that leave users inside submenus along with buttons that return them to the Main Menu.

🎊 Congratulations, your bot has become even better!


```
```
❓What is a form and why do I need them?

```
```
❓What is a form and why do I need them?

A form - is a command which contains one or more questions.

When a subscriber uses this command, he receives these questions, answers them, and the responses are sent back to administrators (you).

Why do you need forms?

Forms make your bot more powerful, allowing you to: • Collect feedback
• Receive user generated content
• Take orders
...and more


```
```
❓How to create a form?

As we have mentioned, form - is just a command with a question. The steps to create a form are the same as the steps to create a command:

1) Go to your bot
2) Custom Commands
3) Create Command
4) Add Question


```
```
❓How to view form replies?

There is a new button in the main menu of your bot: “Form Replies”. Press it, choose a form and you will see the list of replies to it.


```
```
❓How to get feedback from my users?

You can collect feedback from your users.

Use Forms to do it.

For example, create a form with a question: "What do you think about this bot?" And your users will be able to write comments and suggestions.

You can also create a multiple choice question, for example:

How do you like our newsletter today?
• It’s Great!
• Good.
• Could be better...

In case of multiple choice the user will be shown a keyboard with possible answers, one of which he would have to select.


```
```
❓How to get content from my users?

You can get content from your users.

Use Forms to do it.

For example, you can create a form with a question: "What's your favorite joke?" - People will send you messages and pictures, and you can select the best and send them out to the entire audience.

The same can be done for news, photos, songs, files … The only limit is your imagination ✨


```
```
❓How to receive orders from my users?

Many of you are already using bots as mini-shops, showing goods and services with custom commands and menus.

Now you can receive orders from your users directly inside your bot.

Use Forms to do it.

For example, you can create a form that will ask the customer questions such as: - What do you want to order?
- Where should the order be delivered?
- When should the order be delivered?
- What's your phone number (for order confirmation)?

When a user answers these questions, you will receive a notification about the order and the ability to view it directly within Telegram!

If you have too much orders, you can always connect additional administrators to the bot to help handle the flow.
```
