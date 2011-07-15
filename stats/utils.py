

def parseFolder(folder):
    #name = folder.getProperties()['cmis:name']
    children = folder.getChildren().getResults()
    
    if len(children) == 0: 
        return folder.name,
    else: 
        sublist = []
        for object in children: 
            if type(object).__name__ == 'Folder': 
                sublist.append(parseFolder(object))
            else: 
                sublist.append(object.name)
        return (folder.name, sublist)
