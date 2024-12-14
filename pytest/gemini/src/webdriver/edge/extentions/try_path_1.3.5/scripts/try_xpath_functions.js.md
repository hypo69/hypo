```python
import pytest
from unittest.mock import MagicMock, patch
import json
import types

# Mocking the DOM API
class MockNode:
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12

    def __init__(self, nodeType, nodeName=None, nodeValue=None, textContent=None, parentElement=None, parentNode=None, ownerDocument=None):
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.textContent = textContent
        self.parentElement = parentElement
        self.parentNode = parentNode
        self.ownerDocument = ownerDocument
        self.attributes = {}
        self.classList = MockClassList()
        self.childNodes = []

    def hasAttribute(self, name):
        return name in self.attributes

    def getAttribute(self, name):
        return self.attributes.get(name)

    def setAttribute(self, name, value):
        self.attributes[name] = value

    def removeAttribute(self, name):
        if name in self.attributes:
          del self.attributes[name]

    def appendChild(self, child):
      self.childNodes.append(child)
      child.parentElement = self if self.nodeType == MockNode.ELEMENT_NODE else None
      child.parentNode = self
      if isinstance(child, MockNode) and child.ownerDocument is None:
          child.ownerDocument = self.ownerDocument

    def removeChild(self, child):
        if child in self.childNodes:
            self.childNodes.remove(child)
            child.parentElement = None
            child.parentNode = None
    
    @property
    def firstChild(self):
        return self.childNodes[0] if self.childNodes else None
    
    
class MockAttr:
    def __init__(self, name, value, ownerElement):
        self.name = name
        self.value = value
        self.ownerElement = ownerElement
        self.ownerDocument = ownerElement.ownerDocument
    
class MockClassList:
    def __init__(self):
        self.classes = set()
        
    def add(self, cls):
        self.classes.add(cls)
        
class MockDocument(MockNode):
    def __init__(self):
      super().__init__(MockNode.DOCUMENT_NODE, nodeName="#document")
      self.ownerDocument = self
      self.body = MockNode(MockNode.ELEMENT_NODE, nodeName="body", ownerDocument=self)
      self.appendChild(self.body)

    def createElement(self, tagName):
        return MockNode(MockNode.ELEMENT_NODE, nodeName=tagName, ownerDocument=self)

    def createTextNode(self, text):
      return MockNode(MockNode.TEXT_NODE, nodeValue=text, textContent=text, ownerDocument=self)
    
    def createDocumentFragment(self):
        return MockNode(MockNode.DOCUMENT_FRAGMENT_NODE, nodeName="#document-fragment", ownerDocument=self)
    
    def evaluate(self, expr, context, resolver, resultType, _):
      if expr == "//test" and context.nodeName == "body":
          return MockXPathResult([MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=self)], MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE)
      elif expr == "/test" and context == self:
        return MockXPathResult([MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=self)], MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE)
      elif expr == "//attr" and context.nodeName == "body":
          return MockXPathResult([MockAttr(name="test", value="value", ownerElement=MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=self))], MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE)
      elif expr == "count(//test)" and context == self:
          return MockXPathResult(numberValue=2, resultType=MockXPathResult.NUMBER_TYPE)
      elif expr == "string(//test)" and context == self:
          return MockXPathResult(stringValue="test_value", resultType=MockXPathResult.STRING_TYPE)
      elif expr == "boolean(//test)" and context == self:
           return MockXPathResult(booleanValue=True, resultType=MockXPathResult.BOOLEAN_TYPE)
      else:
          return MockXPathResult([], MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE)
    
    def querySelector(self, selector):
      if selector == "test":
        return MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=self)
      return None

    def querySelectorAll(self, selector):
        if selector == "test":
            return [MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=self), MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=self)]
        return []

    def getElementsByTagName(self, tagName):
        if tagName == "iframe":
            return [MockNode(MockNode.ELEMENT_NODE, nodeName="iframe", ownerDocument=self)]
        return []

class MockXPathResult:
  ANY_TYPE = 0
  NUMBER_TYPE = 1
  STRING_TYPE = 2
  BOOLEAN_TYPE = 3
  UNORDERED_NODE_ITERATOR_TYPE = 4
  ORDERED_NODE_ITERATOR_TYPE = 5
  UNORDERED_NODE_SNAPSHOT_TYPE = 6
  ORDERED_NODE_SNAPSHOT_TYPE = 7
  ANY_UNORDERED_NODE_TYPE = 8
  FIRST_ORDERED_NODE_TYPE = 9

  def __init__(self, nodes=None, resultType=None, numberValue=None, stringValue=None, booleanValue=None):
    self.nodes = nodes or []
    self.resultType = resultType
    self.numberValue = numberValue
    self.stringValue = stringValue
    self.booleanValue = booleanValue
    self.snapshotLength = len(self.nodes)
    self._index = 0

  def iterateNext(self):
    if self._index < len(self.nodes):
      node = self.nodes[self._index]
      self._index += 1
      return node
    return None

  def snapshotItem(self, index):
    if index < len(self.nodes):
        return self.nodes[index]
    return None
    
  @property
  def singleNodeValue(self):
      return self.nodes[0] if self.nodes else None

class MockWindow:
    def __init__(self, document, frames = []):
      self.document = document
      self.frames = frames
      self.frameElement = None
      self.location = MockLocation()

class MockLocation:
    def __init__(self, href="about:blank"):
        self.href = href
        
# Mocking the `tryxpath` namespace and its functions
@pytest.fixture(scope="function")
def tryxpath_mock():
    tryxpath = types.SimpleNamespace()
    tryxpath.functions = types.SimpleNamespace()

    def execExpr(expr, method, opts):
      opts = opts or {}
      context = opts.context or document
      resolver = opts.resolver if "resolver" in opts else None
      doc = opts.document or fu.getOwnerDocument(context) or context
      items = []
      resultType = None

      if method == "evaluate":
        if not fu.isNodeItem(context) and not fu.isAttrItem(context):
            raise Exception("The context is either Nor nor Attr.")
        resolver = fu.makeResolver(resolver)
        resultType = opts.resultType or MockXPathResult.ANY_TYPE
        result = doc.evaluate(expr, context, resolver, resultType, None)
        items = fu.resToArr(result, resultType)
        if resultType == MockXPathResult.ANY_TYPE:
           resultType = result.resultType

      elif method == "querySelector":
          if not fu.isDocOrElem(context):
                raise Exception("The context is either Document nor Element.")
          elem = context.querySelector(expr)
          items = [elem] if elem else []
          resultType = None
      else:
        if not fu.isDocOrElem(context):
              raise Exception("The context is neither Document nor Element.")
        elems = context.querySelectorAll(expr)
        items = fu.listToArr(elems)
        resultType = None

      return {
        "items": items,
        "method": method,
        "resultType": resultType
      }
    tryxpath.functions.execExpr = execExpr

    def resToArr(res, type):
        if type is None or type == MockXPathResult.ANY_TYPE:
            type = res.resultType

        arr = []
        if type == MockXPathResult.NUMBER_TYPE:
            arr.append(res.numberValue)
        elif type == MockXPathResult.STRING_TYPE:
            arr.append(res.stringValue)
        elif type == MockXPathResult.BOOLEAN_TYPE:
            arr.append(res.booleanValue)
        elif type in [MockXPathResult.ORDERED_NODE_ITERATOR_TYPE, MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE]:
            node = res.iterateNext()
            while node is not None:
                arr.append(node)
                node = res.iterateNext()
        elif type in [MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE, MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE]:
            for i in range(res.snapshotLength):
                arr.append(res.snapshotItem(i))
        elif type in [MockXPathResult.ANY_UNORDERED_NODE_TYPE, MockXPathResult.FIRST_ORDERED_NODE_TYPE]:
            arr.append(res.singleNodeValue)
        else:
             raise Exception("The resultType is invalid. " + str(type))
        return arr
    tryxpath.functions.resToArr = resToArr
    
    def makeResolver(obj):
        if obj is None:
            return None
        if isinstance(obj, types.FunctionType):
          return obj

        dict = None
        if isinstance(obj, str):
            try:
                dict = json.loads(obj)
            except json.JSONDecodeError as e:
              raise Exception("Invalid resolver [" + obj + "]. : " + str(e)) from e
        else:
            dict = obj
        
        if fu.isValidDict(dict):
          map = fu.objToMap(dict)
          def resolver(str):
            if map.has(str):
               return map.get(str)
            return ""
          return resolver
        raise Exception("Invalid resolver. " + json.dumps(dict, indent=None))
    tryxpath.functions.makeResolver = makeResolver

    def isValidDict(obj):
      if not isinstance(obj, dict) or obj is None:
        return False
      for key in obj:
        if not isinstance(obj[key], str):
            return False
      return True
    tryxpath.functions.isValidDict = isValidDict

    def objToMap(obj):
        map =  dict()
        for item in obj:
          map[item] = obj[item]
        return map
    tryxpath.functions.objToMap = objToMap
    
    def isDocOrElem(obj):
      return isinstance(obj, MockNode) and (obj.nodeType == MockNode.ELEMENT_NODE or obj.nodeType == MockNode.DOCUMENT_NODE)
    tryxpath.functions.isDocOrElem = isDocOrElem
    
    def listToArr(list_):
        return list(list_)
    tryxpath.functions.listToArr = listToArr

    def getItemDetail(item):
        if isinstance(item, str):
            return {
                "type": "String",
                "name": "",
                "value": item,
                "textContent": ""
            }
        if isinstance(item, (int, float)):
          return {
              "type": "Number",
              "name": "",
              "value": str(item),
              "textContent": ""
            }
        if isinstance(item, bool):
             return {
                "type": "Boolean",
                "name": "",
                "value": str(item),
                "textContent": ""
            }
        if fu.isElementItem(item):
          return {
              "type": "Node " + fu.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + str(item.nodeType) + ")",
              "name": item.nodeName,
              "value": "",
              "textContent": item.textContent
          }
        if fu.isAttrItem(item):
             return {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            }

        return {
            "type": "Node " + fu.getNodeTypeStr(item.nodeType) + "(nodeType="
                + str(item.nodeType) + ")",
            "name": item.nodeName,
            "value": item.nodeValue or "",
            "textContent": item.textContent or ""
        }
    tryxpath.functions.getItemDetail = getItemDetail
    
    def getItemDetails(items):
      details = []
      for item in items:
        details.append(fu.getItemDetail(item))
      return details
    tryxpath.functions.getItemDetails = getItemDetails
    
    nodeTypeMap = {
        MockNode.ELEMENT_NODE: "ELEMENT_NODE",
        MockNode.ATTRIBUTE_NODE: "ATTRIBUTE_NODE",
        MockNode.TEXT_NODE: "TEXT_NODE",
        MockNode.CDATA_SECTION_NODE: "CDATA_SECTION_NODE",
        MockNode.ENTITY_REFERENCE_NODE: "ENTITY_REFERENCE_NODE",
        MockNode.ENTITY_NODE: "ENTITY_NODE",
        MockNode.PROCESSING_INSTRUCTION_NODE: "PROCESSING_INSTRUCTION_NODE",
        MockNode.COMMENT_NODE: "COMMENT_NODE",
        MockNode.DOCUMENT_NODE: "DOCUMENT_NODE",
        MockNode.DOCUMENT_TYPE_NODE: "DOCUMENT_TYPE_NODE",
        MockNode.DOCUMENT_FRAGMENT_NODE: "DOCUMENT_FRAGMENT_NODE",
        MockNode.NOTATION_NODE: "NOTATION_NODE"
    }
    
    def getNodeTypeStr(nodeType):
        return nodeTypeMap.get(nodeType, "Unknown")
    tryxpath.functions.getNodeTypeStr = getNodeTypeStr

    xpathResultMaps = {
          "numToStr" : {
              MockXPathResult.ANY_TYPE: "ANY_TYPE",
              MockXPathResult.NUMBER_TYPE : "NUMBER_TYPE",
              MockXPathResult.STRING_TYPE : "STRING_TYPE",
              MockXPathResult.BOOLEAN_TYPE : "BOOLEAN_TYPE",
              MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE : "UNORDERED_NODE_ITERATOR_TYPE",
              MockXPathResult.ORDERED_NODE_ITERATOR_TYPE : "ORDERED_NODE_ITERATOR_TYPE",
              MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE : "UNORDERED_NODE_SNAPSHOT_TYPE",
              MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE : "ORDERED_NODE_SNAPSHOT_TYPE",
              MockXPathResult.ANY_UNORDERED_NODE_TYPE: "ANY_UNORDERED_NODE_TYPE",
              MockXPathResult.FIRST_ORDERED_NODE_TYPE: "FIRST_ORDERED_NODE_TYPE"
          },
          "strToNum" : {
            "ANY_TYPE": MockXPathResult.ANY_TYPE,
            "NUMBER_TYPE": MockXPathResult.NUMBER_TYPE,
            "STRING_TYPE": MockXPathResult.STRING_TYPE,
            "BOOLEAN_TYPE": MockXPathResult.BOOLEAN_TYPE,
            "UNORDERED_NODE_ITERATOR_TYPE": MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE,
            "ORDERED_NODE_ITERATOR_TYPE": MockXPathResult.ORDERED_NODE_ITERATOR_TYPE,
            "UNORDERED_NODE_SNAPSHOT_TYPE": MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE,
            "ORDERED_NODE_SNAPSHOT_TYPE": MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
            "ANY_UNORDERED_NODE_TYPE": MockXPathResult.ANY_UNORDERED_NODE_TYPE,
            "FIRST_ORDERED_NODE_TYPE": MockXPathResult.FIRST_ORDERED_NODE_TYPE
          }
    }

    def getxpathResultStr(resultType):
      return xpathResultMaps["numToStr"].get(resultType, "Unknown")
    tryxpath.functions.getxpathResultStr = getxpathResultStr

    def getxpathResultNum(resultTypeStr):
      return xpathResultMaps["strToNum"].get(resultTypeStr, float('NaN'))
    tryxpath.functions.getxpathResultNum = getxpathResultNum

    def isAttrItem(item):
      return isinstance(item, MockAttr)
    tryxpath.functions.isAttrItem = isAttrItem

    def isNodeItem(item):
        if fu.isAttrItem(item):
            return False
        return not isinstance(item, (str, int, float))
    tryxpath.functions.isNodeItem = isNodeItem
    
    def isElementItem(item):
        return fu.isNodeItem(item) and item.nodeType == MockNode.ELEMENT_NODE
    tryxpath.functions.isElementItem = isElementItem

    def addClassToItem(clas, item):
      if fu.isElementItem(item):
        item.classList.add(clas)
    tryxpath.functions.addClassToItem = addClassToItem
    
    def addClassToItems(clas, items):
      for item in items:
          fu.addClassToItem(clas, item)
    tryxpath.functions.addClassToItems = addClassToItems

    def saveItemClass(item):
        if not fu.isElementItem(item):
            return None

        clas = item.getAttribute("class") if item.hasAttribute("class") else None
        return {
            "elem": item,
            "origClass": clas
        }
    tryxpath.functions.saveItemClass = saveItemClass

    def restoreItemClass(savedClass):
        if not savedClass:
            return None
        if savedClass["origClass"] is None:
            savedClass["elem"].removeAttribute("class")
        else:
            savedClass["elem"].setAttribute("class", savedClass["origClass"])
    tryxpath.functions.restoreItemClass = restoreItemClass
    
    def saveItemClasses(items):
        savedClasses = []
        for item in items:
           savedClasses.append(fu.saveItemClass(item))
        return savedClasses
    tryxpath.functions.saveItemClasses = saveItemClasses
    
    def restoreItemClasses(savedClasses):
        for savedClass in savedClasses:
           fu.restoreItemClass(savedClass)
    tryxpath.functions.restoreItemClasses = restoreItemClasses
    
    def setAttrToItem(name, value, item):
        if fu.isElementItem(item):
           item.setAttribute(name, value)
    tryxpath.functions.setAttrToItem = setAttrToItem
    
    def removeAttrFromItem(name, item):
        if fu.isElementItem(item):
            item.removeAttribute(name)
    tryxpath.functions.removeAttrFromItem = removeAttrFromItem

    def removeAttrFromItems(name, items):
        for item in items:
             fu.removeAttrFromItem(name, item)
    tryxpath.functions.removeAttrFromItems = removeAttrFromItems
    
    def setIndexToItems(name, items):
       for i, item in enumerate(items):
           fu.setAttrToItem(name, i, item)
    tryxpath.functions.setIndexToItems = setIndexToItems

    def getParentElement(item):
      if fu.isAttrItem(item):
         return item.ownerElement
      if fu.isNodeItem(item):
          if item.parentElement:
              return item.parentElement
          if item.parentNode and item.parentNode.nodeType == MockNode.ELEMENT_NODE:
              return item.parentNode
      return None
    tryxpath.functions.getParentElement = getParentElement
    
    def getAncestorElements(elem):
      ancs = []
      cur = elem
      parent = cur.parentElement
      while parent:
         ancs.append(parent)
         cur = parent
         parent = cur.parentElement
      parent = cur.parentNode
      while parent and parent.nodeType == MockNode.ELEMENT_NODE:
          ancs.append(cur)
          cur = parent
          parent = cur.parentNode
      return ancs
    tryxpath.functions.getAncestorElements = getAncestorElements

    def getOwnerDocument(item):
        if fu.isAttrItem(item):
            if item.ownerElement:
               return item.ownerElement.ownerDocument
            return item.ownerDocument
        if fu.isNodeItem(item):
            return item.ownerDocument
        return None
    tryxpath.functions.getOwnerDocument = getOwnerDocument
    
    def createHeaderRow(values, opts):
        opts = opts or {}
        doc = opts.get("document", document)

        tr = doc.createElement("tr")
        for value in values:
            th = doc.createElement("th")
            th.textContent = value
            tr.appendChild(th)
        return tr
    tryxpath.functions.createHeaderRow = createHeaderRow

    def createDetailTableHeader(opts):
       opts = opts or {}
       doc = opts.get("document", document)

       tr = doc.createElement("tr")
       th = doc.createElement("th")
       th.textContent = "Index"
       tr.appendChild(th)

       th = doc.createElement("th")
       th.textContent = "Type"
       tr.appendChild(th)

       th = doc.createElement("th")
       th.textContent = "Name"
       tr.appendChild(th)
       
       th = doc.createElement("th")
       th.textContent = "Value"
       tr.appendChild(th)
       
       th = doc.createElement("th")
       th.textContent = "Focus"
       tr.appendChild(th)
       
       return tr
    tryxpath.functions.createDetailTableHeader = createDetailTableHeader

    def createDetailRow(index, detail, opts):
        opts = opts or {}
        doc = opts.get("document", document)
        keys = opts.get("keys", ["type", "name", "value"])

        tr = doc.createElement("tr")
        td = doc.createElement("td")
        td.textContent = str(index)
        tr.appendChild(td)

        for key in keys:
            td = doc.createElement("td")
            td.textContent = str(detail[key])
            tr.appendChild(td)
        
        td = doc.createElement("td")
        button = doc.createElement("button")
        button.textContent = "Focus"
        button.setAttribute("data-index", str(index))
        td.appendChild(button)
        tr.appendChild(td)

        return tr
    tryxpath.functions.createDetailRow = createDetailRow

    async def appendDetailRows(parent, details, opts):
        opts = opts or {}
        chunkSize = opts.get("chunkSize", 1000)
        begin = opts.get("begin", 0)
        end = opts.get("end", len(details))
        createRow = opts.get("createRow", fu.createDetailRow)
        detailKeys = opts.get("detailKeys")

        doc = parent.ownerDocument
        frag = doc.createDocumentFragment()
        index = max(begin, 0)
        chunkEnd = min(index + chunkSize, len(details), end)

        for i in range(index, chunkEnd):
          frag.appendChild(createRow(i, details[i], {
              "document": doc,
              "keys": detailKeys
          }))
        parent.appendChild(frag)

        if index < end and index < len(details):
          await fu.appendDetailRows(parent, details, {
              "chunkSize": chunkSize,
              "begin": index,
              "end": end,
              "createRow": createRow,
              "detailKeys": detailKeys
          })
        return
    tryxpath.functions.appendDetailRows = appendDetailRows
    
    async def updateDetailsTable(parent, details, opts):
      opts = opts or {}
      chunkSize = opts.get("chunkSize", 1000)
      begin = opts.get("begin", 0)
      end = opts.get("end", len(details))
      detailKeys = opts.get("detailKeys")
      headerValues = opts.get("headerValues")

      if headerValues:
          headerValues = ["Index"] + headerValues + ["Focus"]
      else:
          headerValues = ["Index", "Type", "Name", "Value", "Focus"]

      doc = parent.ownerDocument
      fu.emptyChildNodes(parent)
      parent.appendChild(fu.createHeaderRow(headerValues, { "document": doc }))

      await fu.appendDetailRows(parent, details, {
          "chunkSize": chunkSize,
          "begin": begin,
          "end": end,
          "detailKeys": detailKeys
      })
    tryxpath.functions.updateDetailsTable = updateDetailsTable

    def emptyChildNodes(elem):
       while elem.firstChild:
         elem.removeChild(elem.firstChild)
    tryxpath.functions.emptyChildNodes = emptyChildNodes

    def saveAttrForItem(item, attr, storage, overwrite):
      storage = storage or {}

      if not fu.isElementItem(item):
           return storage
      
      if item in storage:
         elemStor = storage[item]
      else:
         elemStor = {}
         storage[item] = elemStor
      
      val = item.getAttribute(attr) if item.hasAttribute(attr) else None

      if overwrite or attr not in elemStor:
          elemStor[attr] = val
      return storage
    tryxpath.functions.saveAttrForItem = saveAttrForItem

    def saveAttrForItems(items, attr, storage, overwrite):
        storage = storage or {}
        for item in items:
           fu.saveAttrForItem(item, attr, storage, overwrite)
        return storage
    tryxpath.functions.saveAttrForItems = saveAttrForItems

    def restoreItemAttrs(storage):
      for item in storage:
        elemStor = storage[item]
        for attr in elemStor:
          value = elemStor[attr]
          if value is None:
             item.removeAttribute(attr)
          else:
             item.setAttribute(attr, value)
    tryxpath.functions.restoreItemAttrs = restoreItemAttrs
    
    def getFrameAncestry(inds, win):
        win = win or window

        frames = []
        for i in inds:
           win = win.frames[i]
           if not win:
                raise Exception("The specified frame does not exist.")
           try:
                frame = win.frameElement
           except Exception as e:
                raise Exception("Access denied.") from e
           frames.append(frame)
        return frames
    tryxpath.functions.getFrameAncestry = getFrameAncestry

    def isNumberArray(arr):
        if not isinstance(arr, list):
            return False
        for item in arr:
           if not isinstance(item, (int, float)):
              return False
        return True
    tryxpath.functions.isNumberArray = isNumberArray

    def onError(err):
      # print(err)
      pass
    tryxpath.functions.onError = onError

    def isBlankWindow(win):
        try:
          return win.location.href == "about:blank"
        except Exception:
          return False
    tryxpath.functions.isBlankWindow = isBlankWindow

    def collectBlankWindows(top):
      wins = []
      frames = top.frames
      for win in frames:
          if fu.isBlankWindow(win):
              wins.append(win)
              wins.extend(fu.collectBlankWindows(win))
      return wins
    tryxpath.functions.collectBlankWindows = collectBlankWindows

    def findFrameElement(win, parent):
        try:
            frames = parent.document.getElementsByTagName("iframe")
            for frame in frames:
              if win == frame.contentWindow:
                 return frame
        except Exception:
          pass
        return None
    tryxpath.functions.findFrameElement = findFrameElement

    def findFrameIndex(win, parent):
      try:
         wins = parent.frames
         for i, currentWin in enumerate(wins):
             if win == currentWin:
                 return i
      except Exception:
        pass
      return -1
    tryxpath.functions.findFrameIndex = findFrameIndex

    def makeDetailText(detail, keys, separator = ",", replacers = {}):
        texts = []
        for key in keys:
            val = detail[key]
            if key in replacers:
              val = replacers[key](val)
            texts.append(val)
        return separator.join(texts)
    tryxpath.functions.makeDetailText = makeDetailText
    
    return tryxpath
  
@pytest.fixture(scope="function")
def document():
    return MockDocument()

@pytest.fixture(scope="function")
def window(document):
  return MockWindow(document)

@pytest.fixture
def fu(tryxpath_mock):
    return tryxpath_mock.functions


def test_execExpr_evaluate_valid_input(fu, document):
    """Checks correct behavior of execExpr with valid XPath expression."""
    document.body.appendChild(MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=document))
    result = fu.execExpr("//test", "evaluate", {"context": document.body})
    assert result["items"]
    assert result["method"] == "evaluate"
    assert result["resultType"] == MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE
    assert len(result["items"]) == 1
    assert result["items"][0].nodeName == "test"

def test_execExpr_evaluate_invalid_context(fu, document):
  """Checks exception handling for invalid context in evaluate method."""
  with pytest.raises(Exception, match="The context is either Nor nor Attr."):
      fu.execExpr("//test", "evaluate", {"context": "string"})

def test_execExpr_querySelector_valid_input(fu, document):
  """Checks correct behavior of execExpr with valid querySelector."""
  document.body.appendChild(MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=document))
  result = fu.execExpr("test", "querySelector", {"context": document.body})
  assert result["items"]
  assert result["method"] == "querySelector"
  assert result["resultType"] is None
  assert len(result["items"]) == 1
  assert result["items"][0].nodeName == "test"
  
def test_execExpr_querySelector_invalid_context(fu, document):
  """Checks exception handling for invalid context in querySelector method."""
  with pytest.raises(Exception, match="The context is either Document nor Element."):
      fu.execExpr("test", "querySelector", {"context": "string"})
      
def test_execExpr_querySelectorAll_valid_input(fu, document):
    """Checks correct behavior of execExpr with valid querySelectorAll."""
    document.body.appendChild(MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=document))
    document.body.appendChild(MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=document))
    result = fu.execExpr("test", "querySelectorAll", {"context": document.body})
    assert result["items"]
    assert result["method"] == "querySelectorAll"
    assert result["resultType"] is None
    assert len(result["items"]) == 2
    assert result["items"][0].nodeName == "test"
    assert result["items"][1].nodeName == "test"

def test_execExpr_querySelectorAll_invalid_context(fu, document):
    """Checks exception handling for invalid context in querySelectorAll method."""
    with pytest.raises(Exception, match="The context is neither Document nor Element."):
        fu.execExpr("test", "querySelectorAll", {"context": "string"})

def test_resToArr_number_type(fu):
    """Checks correct conversion of NUMBER_TYPE result to array."""
    res = MockXPathResult(numberValue=10, resultType=MockXPathResult.NUMBER_TYPE)
    arr = fu.resToArr(res, MockXPathResult.NUMBER_TYPE)
    assert arr == [10]

def test_resToArr_string_type(fu):
    """Checks correct conversion of STRING_TYPE result to array."""
    res = MockXPathResult(stringValue="test", resultType=MockXPathResult.STRING_TYPE)
    arr = fu.resToArr(res, MockXPathResult.STRING_TYPE)
    assert arr == ["test"]

def test_resToArr_boolean_type(fu):
    """Checks correct conversion of BOOLEAN_TYPE result to array."""
    res = MockXPathResult(booleanValue=True, resultType=MockXPathResult.BOOLEAN_TYPE)
    arr = fu.resToArr(res, MockXPathResult.BOOLEAN_TYPE)
    assert arr == [True]

def test_resToArr_ordered_node_iterator_type(fu, document):
    """Checks correct conversion of ORDERED_NODE_ITERATOR_TYPE result to array."""
    nodes = [MockNode(MockNode.ELEMENT_NODE, nodeName="test", ownerDocument=document), MockNode(MockNode.ELEMENT_NODE, nodeName="test2", ownerDocument=document)]
    res = MockXPathResult(nodes, MockXPathResult.ORDERED_NODE_ITERATOR_TYPE)
    arr = fu.resToArr(res, MockXPathResult.ORDERED_NODE_ITERATOR_TYPE)
    assert len(arr) == 2
    assert arr[0].nodeName == "test"
    assert arr[1].nodeName == "test2"
    
def test_resToArr_unordered_node_iterator_type(fu, document):
    """Checks correct conversion of UNORDERED_NODE_ITERATOR_