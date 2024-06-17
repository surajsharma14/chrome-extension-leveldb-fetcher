# chrome-extension-leveldb-fetcher

Step 1: Create a Simple Chrome Extension
First, let's create a simple Chrome extension that stores a value using the chrome.storage API.

To install the extension:

Open Chrome and go to chrome://extensions/.
Enable "Developer mode" (top right).
Click "Load unpacked" and select the directory containing the above files.


Step 2: Locate the LevelDB Database
Chrome stores its data in LevelDB databases in the user profile directory. The exact path varies by OS:

Windows: C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\<Extension ID>
macOS: ~/Library/Application Support/Google/Chrome/Default/Local Extension Settings/<Extension ID>
Linux: ~/.config/google-chrome/Default/Local Extension Settings/<Extension ID>



To find the Extension ID:

Go to chrome://extensions/.
Find your extension and note the ID.
Step 3: Write a Script to Read from the LevelDB Database
We'll use Python with the plyvel library to interact with the LevelDB database. You can install plyvel using pip:

pip install plyvel
