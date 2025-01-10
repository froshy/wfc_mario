def parseTXT(file):
    level = [[]]
    with open(f'levels/{file}') as foo:
        while True:
            f = foo.read(1)

            if not f:
                break
            
            if f == '\n':
                level.append([])
            else:
                level[-1].append(f)
        
        if len(level[-1]) != len(level[0]):
            level.pop(-1)
        return level