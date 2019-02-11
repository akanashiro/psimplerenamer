# psimplerenamer
A pretty simple file renamer for Linux.

I wanted to write a simple file renamer extension for Nemo (similar to Dolphin's) but end up writing a standalone application in Python.
I tried to keep the <i>"Simple by default, powerfull when needed"</i> motto

This app is supposed to be quite simple, but it has enough features to make bulk file renaming easy.
If you are a power user, I suggest you more powerful applications such as Inviska, Gprename or Krename.

What it does:
- Rename different files in different directories. I though it would be nice to have a bulk file renaming using consecutive numbers in different folders.
- Choose an initial/ending sequence number.
- Add/remove files to rename.
- Clean list of added files
- Postfix/sufix sequence option.

It doesn't:
- use regular expressions. 

To-do (next releases):
- Possibility to use letters instead of numbers.
- Uppercase/Lowecase.
- add date.

Wishlist:
- Drag & Drop

<img src="explanation.png">
<img src="result.png">

PS: there's a binary at "psimplerenamer/pyQT version/dist/"

