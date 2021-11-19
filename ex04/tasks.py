import os
import pickle

# Back end like side of the app
class TodoList:
    def __init__(self,):
        # Initializing values and load files if there is a backup file in home
        self.storage = []
        self.next_id = 0
        self.backupFile = os.path.join(os.path.expanduser('~'),
                                       'my-notes-backup-123')
        self._reload()

    def _update(self,):
        # After each update, increment id and save state in file
        self.next_id += 1
        self._save()

    def _reload(self):
        # If there is a backup file, load it and restore next_id
        if os.path.exists(self.backupFile):
            with open(self.backupFile, 'rb') as file:
                self.storage = pickle.load(file)

            # Restore next_id to be bigger than all currently available notes' id
            self.next_id = max([note['id'] for note in self.storage]) + 1

            print('Notes were loaded successfully')
        else:
            # Print warning message that we did not find a backup file
            print(f'There was no {self.backupFile} to be loaded!')

    def _save(self):
        # Save state of program
        with open(self.backupFile, 'wb') as file:
            pickle.dump(self.storage, file)

    def close(self):
        # Save state before exiting app
        self._save()

    def addNote(self, title, text):
        # Add new note and it is marked as not done
        new = {
            "id":       self.next_id,
            "title":    title,
            "body":     text,
            "done":     False,
        }
        self.storage.append(new)
        self._update()

    def deleteNote(self, id):
        # Delete a note from storage by id
        deleted = False
        for idx, note in enumerate(self.storage):
            if note['id'] == id:
                self.storage.pop(idx)
                deleted = True
                self._update()
                break
        if not deleted:
            # Error message that there was no note with id
            print(f'There is no note with id {id}')
        else:
            print(f'Note with id {id} deleted')

    def showNotes(self):
        # Show all notes
        print("=====================ALL NOTES=======================")
        for note in self.storage:
            print(f"----------------{note['title']}----------------")
            print(f"title: {note['title']}")
            print(f"Id:    {note['id']}")
            print(f"body:  {note['body']}")
            print("Done" if note['done'] else 'Undone!')
        if len(self.storage) == 0:
            print('Nothing to show!')


    def showUndoneNotes(self):
        # Show all notes that werer not mark as done
        def onlyUndone(note):
            return not note['done']

        print("=====================UNDONE NOTES=======================")

        # Selecting all notes marked as not done
        notes = filter(onlyUndone, self.storage)

        numberShown = 0

        # Print all tasks that were not done
        for note in notes:
            print(f"----------------{note['title']}----------------")
            print(f"Title: {note['title']}")
            print(f"Id:    {note['id']}")
            print(f"Body:  {note['body']}")
            print(f"Done" if note['done'] else 'Undone!')
            numberShown += 1

        if  numberShown== 0:
            print('Free time! No task to be done!')

    def markAsDone(self, id):
        # Mark the note with id as done
        found = False
        for note in self.storage:
            if note['id'] == id:
                note['done'] = True
                found = True
                break
        if not found:
            print(f"Note with id {id} does not exists!")
        else:
            print(f"Note with id {id} marked as done successfully!")


# Front end like side of the app
class UI:
    def __init__(self,):
        # Initialize back end
        self.editor = TodoList()

    def run(self,):
        # Print helpfull messages to user and enter a loop, leaving only when command q is executed
        self._welcome()
        self._instructions()
        command = 'S'
        while True:
            # Small hand to help user when he accidentally adds parameters after main command
            command = input('Add a command: ').strip().split()[0]

            if command == 'q':
                # Quit program
                self.editor.close()
                break

            elif command == 'n':
                # Add new note
                title = input('Title: ').strip()
                body =  input('Body: ')
                self.editor.addNote(title, body)

            elif command == 's':
                # Show all notes
                self.editor.showNotes()

            elif command == 'S':
                # Show only the not done notes
                self.editor.showUndoneNotes()

            elif command == 'd':
                # Delete note by id
                try:
                    id = int(input("Note's id to be deleted: ").strip())
                    self.editor.deleteNote(id)
                except ValueError:
                    print('Error: id must be an integer')

            elif command == 'm':
                # Mark note as done
                try:
                    id = int(input("Note's id to be marked as done: ").strip())
                    self.editor.markAsDone(id)
                except ValueError:
                    print('Error: id must be an integer')

            elif command == 'c':
                # Clear terminal
                terminal_cmd = 'cls' if os.name in ('nt', 'dos') else 'clear'
                os.system(terminal_cmd)

            elif command == '?':
                # Print commands cheatlist
                self._instructions()

            else:
                # Command invalid!
                print(f"Command '{command}' invalid")
                self._instructions()

            print()

    def _welcome(self,):
        # Welcome message
        print('Welcome to Note')

    def _instructions(self,):
        # Intruction with the commands
        print('=======================================================')
        print('Instructions of how to use it')
        print()
        print('q - quit the program (please do not exit with C-c)')
        print('n - create a new note')
        print('s - display all notes')
        print('S - display only the have to do notes')
        print('d - delete a note by id')
        print('m - mark a note as completed')
        print('c - clear console')
        print('? - prints this help page')
        print('=======================================================')

if __name__ == '__main__':
    front = UI()
    front.run()
    print('Program closed successfully')
