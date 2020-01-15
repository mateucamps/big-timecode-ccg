__all__ = ['getFileFromPath']

def getFileFromPath(_path):
    path = _path
    if '/' in path:
        path = path.split('/')[-1:][0]
    return path