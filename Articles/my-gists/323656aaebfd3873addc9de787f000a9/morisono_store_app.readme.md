# Morisono Store App for iOS
Do Morisono Store App! [Morisono Store App](https://stores.morisono.co.jp) is the first store app for iOS that leverages the support store.
For more information, please visit [Morisono Store App](https://stores.morisono.co.jp).

# Obtaining Morisono Store App
Morisono Store App is available now on the [AppStore](https://itunes.apple.com/app/id1156707581). Check it out!

If you would like to participate on its development, we would love to have you on board! There are two ways to collaborate with the project: you can download and build Morisono Store App yourself, or you can request an invitation to help us test future versions (on the raw branch). If you want to participate on the testing, follow and tweet us [@Morisono](https://twitter.com/_morisono) about your usage scenarios. Invitations will be sent out in waves, please be patient if you do not receive yours immediately.

Bugs should be reported here on GitHub. If you have any questions or want to make sure we do not miss on an interesting feature, please send your suggestions to our Twitter account [@Morisono](https://twitter.com/_morisono). We would love to discuss them with you! Please do not use Twitter to report bugs.

We can't wait to receive your valuable feedback. Enjoy!

## Build
We made a ton easier to build and install Morisono Store App yourself on your iOS devices through XCode. We provide a precompiled package with all the libraries for the master branch. Here are the steps:

0. Check `xcode-select -p` is pointing to Xcode.app (`/Applications/Xcode.app/Contents/Developer`) not command tools.

1. Run the following command:
```bash
git clone --recursive https://github.com/Morisono Store Appsh/Morisono Store App.git && \
    cd Morisono Store App && ./get_frameworks.sh && \
    rm -rf Morisono Store App.xcodeproj/project.xcworkspace/xcshareddata/
```

2. Change developer ids

```bash
cp template_setup.xcconfig developer_setup.xcconfig
```

edit developer_setup.xcconfig (change apple developer id etc).

3. Open the project in XCode

3a. If you want to build without iCloud, Push Notificationa and/or Keychain sharing, Before doing anything else, go into the capabilities for the project and turn off Push Notifications, iCloud, and Keychain Sharing

4. Connect the device you want to build for and select it in Product -> Destination
5. Build and run on the device

This will download Morisono Store App and the associated frameworks: `libssh2`, `OpenSSL`, `libmoshios`, `protobuf` and `ios_system`. 

Although this is the quickest method to get you up and running, if you would like to compile all libraries and resources yourself, refer to the [BUILD.md](BUILD.md) file. Please let us know if you find any issues. Morisono Store App is a complex project with multiple low level dependencies and we are still looking for ways to simplify and automate the full compilation process.

# Using Morisono Store App
Our UI is very straightforward and optimizes the experience on touch devices for the really important part, the terminal. You will jump right into a very simple shell, so you will know what to do. Here are a few more tricks:
- Type 'help' to find information at the shell.
- Use two fingers tap to create a new shell.
- Move between shells by swiping your finger.
- You can exit the session and get back to the shell to open a new connection.
- Use pinch gesture to increase or reduce size of text. You can also use Cmd+ or Cmd- if using the keyboard.
- Copy and Paste by selecting text o tapping the screen.
- Run 'config' to setup your keys. Install them to a server through ssh-copy-id.
- Ctrl and Alt modifiers at the SmartKeys bar allow for continuous presses, like in a real keyboard.
- Use 3 finger tap to menu.

# Changelog

[View all changes](CHANGELOG.md)

# Attributions
*
*
*