# randoms
BaselHack 2023 

# How to install firebase:
https://firebase.google.com/docs/cli#install-cli-mac-linux


# notes for first setup

First command to run:
```
# assuming you have npm installed if not look into node
npm install -g firebase-tools
```

Send Alex Rovner your gmail if not it has be Google Cloud account

Then you can run:
```
firebase init emulators 
```

You will need to select: auth, functions, firestore, and hosting. Space to select them then Enter. 

It will setup you through the install and you add the code to the project then select the following answers: 
```
? Which port do you want to use for the functions emulator? 5001
? Which port do you want to use for the firestore emulator? 8080
? Which port do you want to use for the hosting emulator? 5000
? Which port do you want to use for the auth emulator? 9099
? Would you like to enable the Emulator UI? Yes
? Which port do you want to use for the Emulator UI (leave empty to use any available port)? 
? Would you like to download the emulators now? Yes
```
Then to start the project you run:
```
firebase emulators:start
```

## Running Locally

Make sure you setup a python3 virtual environment with `python3 -m venv venv`.
Install the emulators with `firebase init emulators` and then run `firebase emulators:start` to start the emulators.
The emulator UI will be available under `localhost:4000`. The webpage will be available under `localhost:5000`.