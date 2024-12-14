```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Mock the DOM environment
class MockNode:
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    DOCUMENT_NODE = 9
    
    def __init__(self, nodeType, nodeName=None, nodeValue=None, textContent=None, attributes=None, parentNode=None, ownerDocument=None, parentElement=None, classList=None):
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.textContent = textContent
        self.attributes = attributes if attributes is not None else {}
        self.parentNode = parentNode
        self.ownerDocument = ownerDocument
        self.parentElement = parentElement
        self.classList = classList if classList is not None else MockClassList()
    
    def hasAttribute(self, attr):
        return attr in self.attributes
    
    def getAttribute(self, attr):
       return self.attributes.get(attr, None)
    
    def setAttribute(self, attr, value):
        self.attributes[attr] = value
    
    def removeAttribute(self, attr):
        if attr in self.attributes:
           del self.attributes[attr]

class MockClassList:
  def __init__(self):
    self._classes = []

  def add(self, class_name):
    self._classes.append(class_name)
  
  def remove(self, class_name):
    if class_name in self._classes:
      self._classes.remove(class_name)

  def contains(self, class_name):
    return class_name in self._classes

  def __iter__(self):
    return iter(self._classes)

class MockAttr:
    def __init__(self, name, value, ownerElement=None, ownerDocument=None):
        self.name = name
        self.value = value
        self.ownerElement = ownerElement
        self.ownerDocument = ownerDocument

class MockDocument:
  def __init__(self):
      self.body = MockNode(MockNode.ELEMENT_NODE, 'body')
  
  def createElement(self, tag):
    return MockNode(MockNode.ELEMENT_NODE, tag)
  
  def createDocumentFragment(self):
    return MockNode(MockNode.DOCUMENT_FRAGMENT_NODE)

  def evaluate(self, expr, context, resolver, resultType, result):
     # Mock implementation
    if expr == "//element":
        return MockXPathResult(MockXPathResult.ORDERED_NODE_ITERATOR_TYPE, [MockNode(MockNode.ELEMENT_NODE, 'element')])
    elif expr == "//text()":
       return MockXPathResult(MockXPathResult.ORDERED_NODE_ITERATOR_TYPE, [MockNode(MockNode.TEXT_NODE, textContent="text_node")])
    elif expr == "//number()":
       return MockXPathResult(MockXPathResult.NUMBER_TYPE, 123)
    elif expr == "//string()":
      return MockXPathResult(MockXPathResult.STRING_TYPE, "test_string")
    elif expr == "//boolean()":
      return MockXPathResult(MockXPathResult.BOOLEAN_TYPE, True)

    elif expr == "//attr()":
        return MockXPathResult(MockXPathResult.ORDERED_NODE_ITERATOR_TYPE, [MockAttr("attr_name", "attr_value")])

    elif expr == "//element_snapshot":
        return MockXPathResult(MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE, [MockNode(MockNode.ELEMENT_NODE, 'element_snapshot_1'),
        MockNode(MockNode.ELEMENT_NODE, 'element_snapshot_2')])
    
    elif expr == "//single_node":
      return MockXPathResult(MockXPathResult.FIRST_ORDERED_NODE_TYPE, MockNode(MockNode.ELEMENT_NODE, 'single_node'))
    
    return MockXPathResult(MockXPathResult.ANY_TYPE, [])

  def querySelector(self, expr):
    if expr == '.test':
      return MockNode(MockNode.ELEMENT_NODE, 'div', classList=MockClassList())
    return None
  
  def querySelectorAll(self, expr):
     if expr == 'div':
        return [MockNode(MockNode.ELEMENT_NODE, 'div', classList=MockClassList()),
            MockNode(MockNode.ELEMENT_NODE, 'div', classList=MockClassList())]
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

    def __init__(self, resultType, value):
        self.resultType = resultType
        self.value = value
        self.index = 0
        self.snapshotLength = len(value) if isinstance(value, list) else 0

    def iterateNext(self):
        if self.resultType not in [self.ORDERED_NODE_ITERATOR_TYPE, self.UNORDERED_NODE_ITERATOR_TYPE]:
           return None
        if self.index < len(self.value):
            node = self.value[self.index]
            self.index += 1
            return node
        return None
    
    @property
    def numberValue(self):
        if self.resultType == self.NUMBER_TYPE:
          return self.value
        return None
    
    @property
    def stringValue(self):
       if self.resultType == self.STRING_TYPE:
          return self.value
       return None
    
    @property
    def booleanValue(self):
        if self.resultType == self.BOOLEAN_TYPE:
          return self.value
        return None
    
    def snapshotItem(self, index):
        if self.resultType in [self.ORDERED_NODE_SNAPSHOT_TYPE, self.UNORDERED_NODE_SNAPSHOT_TYPE]:
           if index < len(self.value):
              return self.value[index]
        return None
    
    @property
    def singleNodeValue(self):
       if self.resultType in [self.ANY_UNORDERED_NODE_TYPE, self.FIRST_ORDERED_NODE_TYPE]:
           return self.value
       return None

# Create a mock window object
class MockWindow:
    def __init__(self, document=None, frames=None, frameElement=None, location=None):
        self.document = document if document else MockDocument()
        self.frames = frames if frames else []
        self.frameElement = frameElement
        self.location = location if location else MockLocation()

class MockLocation:
    def __init__(self, href="about:blank"):
        self.href = href

# Mock the 'window' object
window = MockWindow()

# Mock the tryxpath and tryxpath.functions namespaces
tryxpath = {}
tryxpath.functions = {}
tx = tryxpath
fu = tryxpath.functions
fu.done = False


# load the code to test
exec(open("hypotez/src/webdriver/chrome/extentions/try_path_1.3.5/scripts/try_xpath_functions.js").read())
fu = tryxpath.functions

# Fixture for creating a test element
@pytest.fixture
def test_element():
    return MockNode(MockNode.ELEMENT_NODE, 'div', textContent='Test Content')

@pytest.fixture
def test_attr():
    return MockAttr("test_attr", "test_value")

@pytest.fixture
def test_document():
    return MockDocument()

@pytest.fixture
def mock_window():
    return MockWindow()

# Tests for fu.execExpr
def test_execExpr_evaluate_valid(test_document):
    """Test 'evaluate' method with valid context and expression."""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr("//element", "evaluate", {"context": context, "document": test_document})
    assert result["method"] == "evaluate"
    assert len(result["items"]) == 1
    assert result["items"][0].nodeName == "element"
    assert result["resultType"] == MockXPathResult.ORDERED_NODE_ITERATOR_TYPE

def test_execExpr_evaluate_invalid_context(test_document):
  """Test 'evaluate' method with invalid context (not Node or Attr)."""
  context = 123
  with pytest.raises(Error, match="The context is either Nor nor Attr."):
        fu.execExpr("//element", "evaluate", {"context": context, "document": test_document})

def test_execExpr_evaluate_custom_resolver(test_document):
    """Test 'evaluate' with a custom resolver."""
    def resolver(prefix):
        if prefix == "test":
            return "test_namespace"
        return ""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr("//test:element", "evaluate", {"context": context, "resolver": resolver, "document": test_document})
    assert result["method"] == "evaluate"
    assert len(result["items"]) == 0 #resolver is mock

def test_execExpr_querySelector_valid(test_document):
    """Test 'querySelector' with valid context and expression."""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr(".test", "querySelector", {"context": context, "document": test_document})
    assert result["method"] == "querySelector"
    assert len(result["items"]) == 1
    assert result["items"][0].nodeName == "div"
    assert result["resultType"] == None
    

def test_execExpr_querySelector_invalid_context(test_document):
    """Test 'querySelector' with invalid context (not Document or Element)."""
    context = 123
    with pytest.raises(Error, match="The context is either Document nor Element."):
      fu.execExpr(".test", "querySelector", {"context": context, "document": test_document})
    
def test_execExpr_querySelector_not_found(test_document):
    """Test 'querySelector' when no element is found."""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr(".notfound", "querySelector", {"context": context, "document": test_document})
    assert result["method"] == "querySelector"
    assert len(result["items"]) == 0
    assert result["resultType"] == None


def test_execExpr_querySelectorAll_valid(test_document):
    """Test 'querySelectorAll' with valid context and expression."""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr("div", "querySelectorAll", {"context": context, "document": test_document})
    assert result["method"] == "querySelectorAll"
    assert len(result["items"]) == 2
    assert result["items"][0].nodeName == "div"
    assert result["resultType"] == None

def test_execExpr_querySelectorAll_invalid_context(test_document):
  """Test 'querySelectorAll' with invalid context (not Document or Element)."""
  context = 123
  with pytest.raises(Error, match="The context is neither Document nor Element."):
      fu.execExpr("div", "querySelectorAll", {"context": context, "document": test_document})

def test_execExpr_querySelectorAll_not_found(test_document):
    """Test 'querySelectorAll' when no elements are found."""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr("span", "querySelectorAll", {"context": context, "document": test_document})
    assert result["method"] == "querySelectorAll"
    assert len(result["items"]) == 0
    assert result["resultType"] == None
    
def test_execExpr_default_method(test_document):
    """Test default method which is querySelectorAll."""
    context = MockNode(MockNode.ELEMENT_NODE, 'div', ownerDocument=test_document)
    result = fu.execExpr("div", None, {"context": context, "document": test_document})
    assert result["method"] == "querySelectorAll"
    assert len(result["items"]) == 2
    assert result["items"][0].nodeName == "div"
    assert result["resultType"] == None

# Tests for fu.resToArr
def test_resToArr_number_type():
    """Test resToArr with NUMBER_TYPE result."""
    res = MockXPathResult(MockXPathResult.NUMBER_TYPE, 123)
    arr = fu.resToArr(res)
    assert arr == [123]

def test_resToArr_string_type():
  """Test resToArr with STRING_TYPE result."""
  res = MockXPathResult(MockXPathResult.STRING_TYPE, "test_string")
  arr = fu.resToArr(res)
  assert arr == ["test_string"]
  
def test_resToArr_boolean_type():
  """Test resToArr with BOOLEAN_TYPE result."""
  res = MockXPathResult(MockXPathResult.BOOLEAN_TYPE, True)
  arr = fu.resToArr(res)
  assert arr == [True]
  
def test_resToArr_ordered_node_iterator_type():
  """Test resToArr with ORDERED_NODE_ITERATOR_TYPE result."""
  nodes = [MockNode(MockNode.ELEMENT_NODE, 'element_1'),
           MockNode(MockNode.ELEMENT_NODE, 'element_2')]
  res = MockXPathResult(MockXPathResult.ORDERED_NODE_ITERATOR_TYPE, nodes)
  arr = fu.resToArr(res)
  assert len(arr) == 2
  assert arr[0].nodeName == "element_1"
  assert arr[1].nodeName == "element_2"
  
def test_resToArr_unordered_node_iterator_type():
    """Test resToArr with UNORDERED_NODE_ITERATOR_TYPE result."""
    nodes = [MockNode(MockNode.ELEMENT_NODE, 'element_1'),
             MockNode(MockNode.ELEMENT_NODE, 'element_2')]
    res = MockXPathResult(MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE, nodes)
    arr = fu.resToArr(res)
    assert len(arr) == 2
    assert arr[0].nodeName == "element_1"
    assert arr[1].nodeName == "element_2"

def test_resToArr_ordered_node_snapshot_type():
    """Test resToArr with ORDERED_NODE_SNAPSHOT_TYPE result."""
    nodes = [MockNode(MockNode.ELEMENT_NODE, 'element_1'),
             MockNode(MockNode.ELEMENT_NODE, 'element_2')]
    res = MockXPathResult(MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE, nodes)
    arr = fu.resToArr(res)
    assert len(arr) == 2
    assert arr[0].nodeName == "element_1"
    assert arr[1].nodeName == "element_2"

def test_resToArr_unordered_node_snapshot_type():
    """Test resToArr with UNORDERED_NODE_SNAPSHOT_TYPE result."""
    nodes = [MockNode(MockNode.ELEMENT_NODE, 'element_1'),
             MockNode(MockNode.ELEMENT_NODE, 'element_2')]
    res = MockXPathResult(MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, nodes)
    arr = fu.resToArr(res)
    assert len(arr) == 2
    assert arr[0].nodeName == "element_1"
    assert arr[1].nodeName == "element_2"

def test_resToArr_any_unordered_node_type():
  """Test resToArr with ANY_UNORDERED_NODE_TYPE result."""
  node = MockNode(MockNode.ELEMENT_NODE, 'single_node')
  res = MockXPathResult(MockXPathResult.ANY_UNORDERED_NODE_TYPE, node)
  arr = fu.resToArr(res)
  assert len(arr) == 1
  assert arr[0].nodeName == "single_node"
    
def test_resToArr_first_ordered_node_type():
    """Test resToArr with FIRST_ORDERED_NODE_TYPE result."""
    node = MockNode(MockNode.ELEMENT_NODE, 'single_node')
    res = MockXPathResult(MockXPathResult.FIRST_ORDERED_NODE_TYPE, node)
    arr = fu.resToArr(res)
    assert len(arr) == 1
    assert arr[0].nodeName == "single_node"

def test_resToArr_invalid_type():
    """Test resToArr with an invalid resultType."""
    res = MockXPathResult(-1, None)
    with pytest.raises(Error, match="The resultType is invalid. -1"):
      fu.resToArr(res)

def test_resToArr_any_type():
    """Test resToArr with ANY_TYPE and result is number."""
    res = MockXPathResult(MockXPathResult.ANY_TYPE, 123)
    res.resultType = MockXPathResult.NUMBER_TYPE
    arr = fu.resToArr(res)
    assert arr == [123]

    """Test resToArr with ANY_TYPE and result is string."""
    res = MockXPathResult(MockXPathResult.ANY_TYPE, "test_string")
    res.resultType = MockXPathResult.STRING_TYPE
    arr = fu.resToArr(res)
    assert arr == ["test_string"]

    """Test resToArr with ANY_TYPE and result is boolean."""
    res = MockXPathResult(MockXPathResult.ANY_TYPE, True)
    res.resultType = MockXPathResult.BOOLEAN_TYPE
    arr = fu.resToArr(res)
    assert arr == [True]
    
    """Test resToArr with ANY_TYPE and result is Node list."""
    nodes = [MockNode(MockNode.ELEMENT_NODE, 'element_1'),
             MockNode(MockNode.ELEMENT_NODE, 'element_2')]
    res = MockXPathResult(MockXPathResult.ANY_TYPE, nodes)
    res.resultType = MockXPathResult.ORDERED_NODE_ITERATOR_TYPE
    arr = fu.resToArr(res)
    assert len(arr) == 2
    assert arr[0].nodeName == "element_1"
    assert arr[1].nodeName == "element_2"
    

# Tests for fu.makeResolver
def test_makeResolver_null():
    """Test makeResolver with null input."""
    assert fu.makeResolver(None) is None

def test_makeResolver_function():
    """Test makeResolver with a function."""
    def test_func(str):
        return "test_result"
    assert fu.makeResolver(test_func) == test_func

def test_makeResolver_valid_string():
  """Test makeResolver with valid JSON string."""
  resolver_str = '{"prefix1": "uri1", "prefix2": "uri2"}'
  resolver = fu.makeResolver(resolver_str)
  assert callable(resolver)
  assert resolver("prefix1") == "uri1"
  assert resolver("prefix2") == "uri2"
  assert resolver("prefix3") == ""
  
def test_makeResolver_invalid_string():
    """Test makeResolver with invalid JSON string."""
    with pytest.raises(Error, match="Invalid resolver \\[invalid json\\]. : Unexpected token i in JSON at position 0"):
      fu.makeResolver("invalid json")
      
def test_makeResolver_valid_object():
    """Test makeResolver with valid object."""
    resolver_obj = {"prefix1": "uri1", "prefix2": "uri2"}
    resolver = fu.makeResolver(resolver_obj)
    assert callable(resolver)
    assert resolver("prefix1") == "uri1"
    assert resolver("prefix2") == "uri2"
    assert resolver("prefix3") == ""

def test_makeResolver_invalid_object():
    """Test makeResolver with an invalid object."""
    resolver_obj = {"prefix1": 123}
    with pytest.raises(Error, match='Invalid resolver. {"prefix1":123}'):
      fu.makeResolver(resolver_obj)
    
def test_makeResolver_invalid_type():
    """Test makeResolver with an invalid type."""
    with pytest.raises(Error, match='Invalid resolver. "test"'):
      fu.makeResolver("test")
      
# Tests for fu.isValidDict
def test_isValidDict_valid():
    """Test isValidDict with a valid dictionary."""
    obj = {"key1": "value1", "key2": "value2"}
    assert fu.isValidDict(obj) == True

def test_isValidDict_invalid_not_object():
    """Test isValidDict with a non-object type."""
    assert fu.isValidDict(123) == False
    assert fu.isValidDict("test") == False
    assert fu.isValidDict(None) == False

def test_isValidDict_invalid_value():
  """Test isValidDict with a value that is not string."""
  obj = {"key1": "value1", "key2": 123}
  assert fu.isValidDict(obj) == False

# Tests for fu.objToMap
def test_objToMap():
    """Test objToMap function."""
    obj = {"key1": "value1", "key2": "value2"}
    map_result = fu.objToMap(obj)
    assert isinstance(map_result, Map)
    assert map_result.get("key1") == "value1"
    assert map_result.get("key2") == "value2"

# Tests for fu.isDocOrElem
def test_isDocOrElem_element(test_element):
  """Test isDocOrElem with an Element node."""
  assert fu.isDocOrElem(test_element) == True

def test_isDocOrElem_document(test_document):
  """Test isDocOrElem with a Document node."""
  assert fu.isDocOrElem(test_document) == True

def test_isDocOrElem_invalid():
    """Test isDocOrElem with invalid input."""
    assert fu.isDocOrElem(123) == False
    assert fu.isDocOrElem("test") == False
    assert fu.isDocOrElem(None) == False
    assert fu.isDocOrElem(MockNode(MockNode.TEXT_NODE)) == False


# Tests for fu.listToArr
def test_listToArr():
    """Test listToArr with a valid list."""
    list_obj = [1, 2, 3]
    arr = fu.listToArr(list_obj)
    assert arr == [1, 2, 3]

def test_listToArr_empty():
    """Test listToArr with an empty list."""
    list_obj = []
    arr = fu.listToArr(list_obj)
    assert arr == []

# Tests for fu.getItemDetail
def test_getItemDetail_string():
  """Test getItemDetail with a string item."""
  detail = fu.getItemDetail("test_string")
  assert detail["type"] == "String"
  assert detail["value"] == "test_string"
  assert detail["textContent"] == ""
  
def test_getItemDetail_number():
  """Test getItemDetail with a number item."""
  detail = fu.getItemDetail(123)
  assert detail["type"] == "Number"
  assert detail["value"] == "123"
  assert detail["textContent"] == ""

def test_getItemDetail_boolean():
  """Test getItemDetail with a boolean item."""
  detail = fu.getItemDetail(True)
  assert detail["type"] == "Boolean"
  assert detail["value"] == "true"
  assert detail["textContent"] == ""

def test_getItemDetail_element(test_element):
    """Test getItemDetail with an Element node."""
    detail = fu.getItemDetail(test_element)
    assert detail["type"] == "Node ELEMENT_NODE(nodeType=1)"
    assert detail["name"] == "div"
    assert detail["textContent"] == "Test Content"
    assert detail["value"] == ""

def test_getItemDetail_attr(test_attr):
  """Test getItemDetail with Attr node."""
  detail = fu.getItemDetail(test_attr)
  assert detail["type"] == "Attr"
  assert detail["name"] == "test_attr"
  assert detail["value"] == "test_value"
  assert detail["textContent"] == ""

def test_getItemDetail_text_node():
  """Test getItemDetail with a Text node."""
  node = MockNode(MockNode.TEXT_NODE, 'text', textContent="Text Node")
  detail = fu.getItemDetail(node)
  assert detail["type"] == "Node TEXT_NODE(nodeType=3)"
  assert detail["name"] == "text"
  assert detail["value"] == ""
  assert detail["textContent"] == "Text Node"
  

# Tests for fu.getItemDetails
def test_getItemDetails(test_element, test_attr):
    """Test getItemDetails with a list of items."""
    items = [test_element, "test_string", test_attr]
    details = fu.getItemDetails(items)
    assert len(details) == 3
    assert details[0]["type"] == "Node ELEMENT_NODE(nodeType=1)"
    assert details[1]["type"] == "String"
    assert details[2]["type"] == "Attr"
  
def test_getItemDetails_empty():
    """Test getItemDetails with empty items."""
    details = fu.getItemDetails([])
    assert len(details) == 0

# Tests for fu.getNodeTypeStr
def test_getNodeTypeStr_valid():
    """Test getNodeTypeStr with valid node types."""
    assert fu.getNodeTypeStr(MockNode.ELEMENT_NODE) == "ELEMENT_NODE"
    assert fu.getNodeTypeStr(MockNode.ATTRIBUTE_NODE) == "ATTRIBUTE_NODE"
    assert fu.getNodeTypeStr(MockNode.TEXT_NODE) == "TEXT_NODE"
    assert fu.getNodeTypeStr(MockNode.DOCUMENT_NODE) == "DOCUMENT_NODE"

def test_getNodeTypeStr_invalid():
    """Test getNodeTypeStr with an invalid node type."""
    assert fu.getNodeTypeStr(99) == "Unknown"
  
# Tests for fu.getxpathResultStr
def test_getxpathResultStr_valid():
  """Test getxpathResultStr with a valid resultType."""
  assert fu.getxpathResultStr(MockXPathResult.ANY_TYPE) == "ANY_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.NUMBER_TYPE) == "NUMBER_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.STRING_TYPE) == "STRING_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.BOOLEAN_TYPE) == "BOOLEAN_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE) == "UNORDERED_NODE_ITERATOR_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.ORDERED_NODE_ITERATOR_TYPE) == "ORDERED_NODE_ITERATOR_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE) == "UNORDERED_NODE_SNAPSHOT_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE) == "ORDERED_NODE_SNAPSHOT_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.ANY_UNORDERED_NODE_TYPE) == "ANY_UNORDERED_NODE_TYPE"
  assert fu.getxpathResultStr(MockXPathResult.FIRST_ORDERED_NODE_TYPE) == "FIRST_ORDERED_NODE_TYPE"

def test_getxpathResultStr_invalid():
    """Test getxpathResultStr with an invalid resultType."""
    assert fu.getxpathResultStr(-1) == "Unknown"

# Tests for fu.getxpathResultNum
def test_getxpathResultNum_valid():
  """Test getxpathResultNum with a valid resultType."""
  assert fu.getxpathResultNum("ANY_TYPE") == MockXPathResult.ANY_TYPE
  assert fu.getxpathResultNum("NUMBER_TYPE") == MockXPathResult.NUMBER_TYPE
  assert fu.getxpathResultNum("STRING_TYPE") == MockXPathResult.STRING_TYPE
  assert fu.getxpathResultNum("BOOLEAN_TYPE") == MockXPathResult.BOOLEAN_TYPE
  assert fu.getxpathResultNum("UNORDERED_NODE_ITERATOR_TYPE") == MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE
  assert fu.getxpathResultNum("ORDERED_NODE_ITERATOR_TYPE") == MockXPathResult.ORDERED_NODE_ITERATOR_TYPE
  assert fu.getxpathResultNum("UNORDERED_NODE_SNAPSHOT_TYPE") == MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE
  assert fu.getxpathResultNum("ORDERED_NODE_SNAPSHOT_TYPE") == MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE
  assert fu.getxpathResultNum("ANY_UNORDERED_NODE_TYPE") == MockXPathResult.ANY_UNORDERED_NODE_TYPE
  assert fu.getxpathResultNum("FIRST_ORDERED_NODE_TYPE") == MockXPathResult.FIRST_ORDERED_NODE_TYPE

def test_getxpathResultNum_invalid():
    """Test getxpathResultNum with an invalid resultType string."""
    assert fu.getxpathResultNum("invalid") is not fu.getxpathResultNum("invalid") # NaN check
    
# Tests for fu.isAttrItem
def test_isAttrItem_valid(test_attr):
  """Test isAttrItem with a valid Attr object."""
  assert fu.isAttrItem(test_attr) == True
  
def test_isAttrItem_invalid(test_element):
    """Test isAttrItem with an invalid type."""
    assert fu.isAttrItem(test_element) == False
    assert fu.isAttrItem("test") == False
    assert fu.isAttrItem(123) == False
    assert fu.isAttrItem(None) == False

# Tests for fu.isNodeItem
def test_isNodeItem_valid(test_element):
  """Test isNodeItem with a valid Node."""
  assert fu.isNodeItem(test_element) == True
  assert fu.isNodeItem(MockNode(MockNode.TEXT_NODE)) == True

def test_isNodeItem_invalid(test_attr):
    """Test isNodeItem with invalid types."""
    assert fu.isNodeItem(test_attr) == False
    assert fu.isNodeItem("test") == False
    assert fu.isNodeItem(123) == False
    assert fu.isNodeItem(None) == True

# Tests for fu.isElementItem
def test_isElementItem_valid(test_element):
    """Test isElementItem with a valid Element node."""
    assert fu.isElementItem(test_element) == True

def test_isElementItem_invalid(test_attr):
    """Test isElementItem with an invalid node."""
    assert fu.isElementItem(test_attr) == False
    assert fu.isElementItem(MockNode(MockNode.TEXT_NODE)) == False
    assert fu.isElementItem("test") == False
    assert fu.isElementItem(123) == False
    assert fu.isElementItem(None) == False

# Tests for fu.addClassToItem
def test_addClassToItem_valid(test_element):
    """Test addClassToItem with a valid element."""
    fu.addClassToItem("test_class", test_element)
    assert "test_class" in test_element.classList._classes
    
def test_addClassToItem_invalid():
    """Test addClassToItem with a non-element item."""
    item = "test_string"
    fu.addClassToItem("test_class", item)
    # Check if nothing happens
    assert item == "test_string"

# Tests for fu.addClassToItems
def test_addClassToItems_valid(test_element):
    """Test addClassToItems with a list of valid elements."""
    items = [test_element, MockNode(MockNode.ELEMENT_NODE, 'div', classList=MockClassList())]
    fu.addClassToItems("test_class", items)
    assert "test_class" in items[0].classList._classes
    assert "test_class" in items[1].classList._classes

def test_addClassToItems_empty():
  """Test addClassToItems with empty items."""
  fu.addClassToItems("test_class", [])
  #No exception

# Tests for fu.saveItemClass
def test_saveItemClass_valid(test_element):
  """Test saveItemClass with a valid element and no existing class."""
  saved = fu.saveItemClass(test_element)
  assert saved["elem"] == test_element
  assert saved["origClass"] == None

def test_saveItemClass_valid_with_class(test_element):
    """Test saveItemClass with an element that already has class."""
    test_element.setAttribute("class", "existing_class")
    saved = fu.saveItemClass(test_element)
    assert saved["elem"] == test_element
    assert saved["origClass"] == "existing_class"
    
def test_saveItemClass_invalid(test_attr):
  """Test saveItemClass with a non-element item."""
  saved = fu.saveItemClass(test_attr)
  assert saved == None

# Tests for fu.restoreItemClass
def test_restoreItemClass_valid_with_class(test_element):
    """Test restoreItemClass with saved class."""
    test_element.setAttribute("class", "old_class")
    saved_class = fu.saveItemClass(test_element)
    saved_class["