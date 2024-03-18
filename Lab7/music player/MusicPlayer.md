# Music Player Information
## Basic information
This music player works as follows: first, it asks for a folder to be selected using the corresponding folder button.
Then, after selection, all of the music files (mp3, ogg, wav) are added to the queue in alphabetical order. The queue is saved after each session in a separate .json file.
## Buttons (Accessed by the mouse)
### Folder button
Folder button uses tkinter, python's built-in module to create a directory dialog window and return a path. All of the audio files(.mp3, .wav, .ogg) are then stored in a list variable `queue` and sorted in ascending order.
### Clear Button
Clear button when clicked clears the entire queue. At this point, you can still reload the queue with the songs in the songlist file. In other words, it is possible to delete the songs that were added during the current session while still maintaining the songs in the queue that were added before the current session.
When the clear button is clicked while holding `SHIFT`, it results in the entire songlist beign deleted, meaning that the songs that were previously included in the songlist will be deleted altogether. 
Either way, the clear button will stop the playback.
### Back button
Back button when clicked restarts the current song.
When back button is clicked twice the playback goes to the previous song.
If the current song is the first in the queue, the playback is stopped.
### Forward button
Forward button moves the playback to the next song.
If the current song is the last in the queue, the playback is stopped and the index is set to the first song in the queue.
### Play button
When clicked, starts playback if it has not started yet.
If the playback has already started, pauses the playback.
If the playback has already started and the playback is paused, the button resumes playback.
## Keybinds
- `SPACE` - play/pause
- `CTRL-O` - folder selection
- `LEFT` - rewind. Combined with `SHIFT` - previous song
- `RIGHT` - next song
- `UP` - volume up
- `DOWN` - volume down
- `DELETE` - clear the queue
- `SHIFT-DELETE` - delete the entire songlist
