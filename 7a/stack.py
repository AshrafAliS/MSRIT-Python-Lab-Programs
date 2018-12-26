items=[]
def GetStack():
    return(items)
def isEmpty():
    return items==[]
def push(item):
    items.append(item)
def pop():
    return items.pop()
def top():
    return items[len(items)-1]
