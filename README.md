# HackDavis2021
This is our Canvas extension project to consolidate assignment and quiz dates to send automatic reminders

## Get started
Canvas API: https://github.com/ucfopen/canvasapi

Canvas API documentation: https://canvasapi.readthedocs.io/en/stable/

Documentation of specific objects: https://canvas.instructure.com/doc/api/courses.html#method.courses.users

Canvas keyword arguments: https://canvasapi.readthedocs.io/en/stable/keyword-args.html

Matty B's Canvas work: https://github.com/mfbutner/CanvasHelpers https://github.com/RebekahGrace4219/CanvasHelpers

Link to codeshare: https://codeshare.io/5M8OjW

## Installing the Canvas API
First, make sure you have Python 3.x by typing:
```python --version```
Get the most recent version here: https://www.python.org/downloads/

Install Canvas API:
```pip install canvasapi```

Run main.py script by typing
```python3 main.py```

## To test the extension
Open Chrome and go to chrome://extensions/

At the top right, enable Developer Mode

Drag src/ folder to the screen

Your extension is uploaded! View it under the list at the top right.

## To run the server
You'll need to download flask and flask_cors first.
Then type:
```export FLASK_APP=main.py```
```flask run```

The server is currently hosted on localhost:5000 on your personal machine, but we can use ngrok to get a link other people can use.

## To do:
1. Send multiple arguments from frontend to backend. These would be:
  a. Canvas API key
  b. The period of time you want to search for assignment due dates
  c. A list of time periods when you want to receive reminders
2. Have each assignment name be an active link to its Canvas page
3. Allow users to search by course maybe
4. Better UI/UX for the table display
