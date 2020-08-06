def addThisToDicOfThat(this, that, dic):
    if this not in dic:
        dic[this] = [that]
    else:
        dic[this].append(that)


def getNodeIdWithLoc(loc, nodeList):
    dic = {}
    for nodeId, nodeLoc in [(node.id, node.loc) for node in nodeList]:
        dic[nodeLoc] = nodeId
    return dic[loc]


def getNodeLocWithId(ide, nodeList):
    dic = {}
    for nodeId, nodeLoc in [(node.id, node.loc) for node in nodeList]:
        dic[nodeId] = nodeLoc
    return dic[ide]
