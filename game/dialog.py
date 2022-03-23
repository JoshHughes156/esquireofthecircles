
class Dialog:

    def __init__(self, text=list(), children=list()):
        self.text = text
        self.children = children

    @staticmethod
    def load_from_file(filelocation, dialog_path="/dialog"):
        lines = 0
        text = list()
        children = list()
        with open(dialog_path + filelocation, 'r+') as f:
            lines = f.readlines()
        for line in lines:
            if '#' in line:
                child = Dialog()
                s = line.split('#')
                child.load_from_file(s[1].rstrip(), dialog_path=dialog_path)
                children.append(child)

                text.append("> " + s[0])
            else:
                text.append(line)
                
        return (text, children)