__all__ = ['getFileFromPath']

def getFileFromPath(_path):
    if '/' in _path:
        _path = _path.split('/')[-1:][0]
    return _path

