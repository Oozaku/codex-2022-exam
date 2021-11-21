# Description

This is a simple todo list manager written in Python3. It has the following functionalities:

- Add tasks to be done
- Mark tasks as done
- Remove tasks from list
- Show all notes and show only tasks that need to be done

The current limitations are:

- Marking a task as done is irreversible, there is no option to unmark as done
- Exiting with C-c is not reccomendable as it can result in data loss
- Not tested in Windows, the main potential risk is that notes are not saved in disk 
- File that is used to saving the current state is visible to Linux users and Windows and it
is located in HOME

# Requirements

You only need Python3! The library that is used to save current state in disk is Pickle and it
is a standard library. 

# Usage

Just run the command bellow to run the todo list manager.

~~~sh
python3 tasks.py
~~~

# Trobleshooting 

You may lose some notes if you exit with `C-c` (control + C), avoid it and use it only
if the program stops responding. 

This program was not fully tested as it is a part of the exam's exercise and major bugs
may happen, as I did not tested in Windows environment as an example.

# Video

You can see my program working in this link.

https://drive.google.com/file/d/1KNUiu6L_pRq38s-oqQM7LKOG73YOR5xE/view?usp=sharing

0:00 - run the program with no data saved

0:10 - add random notes

0:52 - print cheatlist of commands

0:58 - show all notes

1:00 - mark a note as done

1:12 - show all notes

1:20 - show only not done notes

1:35 - quit

1:37 - run the program with saved data

1:40 - show that data was saved and loaded successfully

1:50 - delete note

