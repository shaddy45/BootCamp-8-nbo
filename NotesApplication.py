''' 
A Notes taking application 

'''
class NotesApplication(object):
    def __init__(self,author):
        self.author = author
        self.notes_list = []

    def create(self, note_content):
        self.notes_list.append(note_content)
    
    def list(self):
        for notes in self.notes_list:
            print("Note ID: {0}\n {1}\n By author {2}".format(self.notes_list.index(notes),notes,self.author))
    
    def get(self, note_id):
        return str(self.notes_list[note_id])
    
    def search(self, search_text):
       mysearch_list = [content for content in self.notes_list if search_text in content]
       if len(mysearch_list)>0:
           print("showing results for search %s"%search_text)
           for notes in mysearch_list:
               print("Note ID: {0}\n {1}\n By author {2}".format(self.notes_list.index(notes),notes,self.author))
    
    def edit(self, note_id, new_content):
        self.notes_list[note_id]=new_content
        return self.notes_list
notes=NotesApplication("Cyrus")
print(notes.create("Where are you John?"))
print(notes.create("My Wifi connection is not working!"))
print(notes.create("I love playing chess"))
# print out the list of strings created
print(notes.list())
# Edit text in specified index 
print(notes.edit(1,"no way! come back"))
print(notes.get(0))
print(notes.search("chess"))

