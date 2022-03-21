
class Dialog:

    def __init__(self, text="", children=[]):
        self.text = text
        self.children = children

    def load_from_file(self, filelocation, dialog_path="/dialog"):
        lines = 0
        with open(dialog_path + filelocation, 'r+') as f:
            lines = f.readlines()
        for line in lines:
            if '#' in line:
                child = Dialog()
                print(dialog_path + filelocation)
                print(line.replace('#', '').rstrip())
                child.load_from_file(line.replace('#', '').rstrip(), dialog_path)
                self.children.append(child)
            else:
                self.text = line
