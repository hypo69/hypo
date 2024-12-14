```python
import pytest
from unittest.mock import MagicMock, patch

# Mock the necessary browser API objects and functions
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

    def __init__(self, nodeType, nodeName, nodeValue=None, textContent=None, ownerDocument=None, parentElement=None, parentNode=None, ownerElement=None):
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.textContent = textContent
        self.ownerDocument = ownerDocument
        self.parentElement = parentElement
        self.parentNode = parentNode
        self.ownerElement = ownerElement
        self.attributes = {}
        self.classList = MockClassList()

    def hasAttribute(self, name):
        return name in self.attributes

    def getAttribute(self, name):
        return self.attributes.get(name)

    def setAttribute(self, name, value):
        self.attributes[name] = value

    def removeAttribute(self, name):
        if name in self.attributes:
           del self.attributes[name]
    
class MockClassList:
    def __init__(self):
        self.classes = set()
    
    def add(self, cls):
        self.classes.add(cls)

class MockAttr:
    def __init__(self, name, value, ownerElement):
        self.name = name
        self.value = value
        self.ownerElement = ownerElement

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

    def __init__(self, resultType, value=None, nodes=None):
        self.resultType = resultType
        self.numberValue = value if resultType == MockXPathResult.NUMBER_TYPE else None
        self.stringValue = value if resultType == MockXPathResult.STRING_TYPE else None
        self.booleanValue = value if resultType == MockXPathResult.BOOLEAN_TYPE else None
        self.singleNodeValue = value if resultType in [MockXPathResult.ANY_UNORDERED_NODE_TYPE, MockXPathResult.FIRST_ORDERED_NODE_TYPE] else None
        self.nodes = nodes if nodes is not None else []
        self.snapshotLength = len(self.nodes)
        self._iter_index = 0
    
    def iterateNext(self):
       if self.resultType in [MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE, MockXPathResult.ORDERED_NODE_ITERATOR_TYPE]:
           if self._iter_index < len(self.nodes):
               node = self.nodes[self._iter_index]
               self._iter_index += 1
               return node
       return None

    def snapshotItem(self, index):
      if self.resultType in [MockXPathResult.ORDERED_NODE_SNAPSHOT_TYPE, MockXPathResult.UNORDERED_NODE_SNAPSHOT_TYPE] and index < len(self.nodes):
         return self.nodes[index]
      return None

class MockDocument:
    def __init__(self):
        self.body = MockNode(MockNode.ELEMENT_NODE, "body", textContent="body")
        self.childNodes = []

    def createElement(self, tag):
      return MockNode(MockNode.ELEMENT_NODE, tag)
      
    def createTextNode(self, text):
        return MockNode(MockNode.TEXT_NODE, "#text", nodeValue=text)
    
    def createDocumentFragment(self):
      return MockDocumentFragment()
    
    def querySelector(self, selector):
        if selector == "div":
            return MockNode(MockNode.ELEMENT_NODE, "div", textContent="div_content")
        return None

    def querySelectorAll(self, selector):
      if selector == "p":
         return [
            MockNode(MockNode.ELEMENT_NODE, "p", textContent="p1_content"),
            MockNode(MockNode.ELEMENT_NODE, "p", textContent="p2_content")
         ]
      return []

    def evaluate(self, expr, context, resolver, resultType, _):
       if expr == "//p" and resultType == MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE:
           return MockXPathResult(resultType, nodes=[MockNode(MockNode.ELEMENT_NODE, "p", textContent="p1_content"),
                                             MockNode(MockNode.ELEMENT_NODE, "p", textContent="p2_content")])
       if expr == "//a" and resultType == MockXPathResult.ANY_UNORDERED_NODE_TYPE:
          return MockXPathResult(resultType, value = MockNode(MockNode.ELEMENT_NODE, "a", textContent="a_content"))
       if expr == "//b" and resultType == MockXPathResult.NUMBER_TYPE:
          return MockXPathResult(resultType, value = 123)
       if expr == "//c" and resultType == MockXPathResult.STRING_TYPE:
          return MockXPathResult(resultType, value = "abc")
       if expr == "//d" and resultType == MockXPathResult.BOOLEAN_TYPE:
           return MockXPathResult(resultType, value=True)
       return MockXPathResult(resultType)
       
class MockDocumentFragment:
    def __init__(self):
        self.childNodes = []
    
    def appendChild(self, node):
        self.childNodes.append(node)

class MockWindow:
    def __init__(self):
        self.document = MockDocument()
        self.frames = []
        self.frameElement = None
        self.location = MockLocation()
    
    def add_frame(self, win):
      self.frames.append(win)
      
    def set_frame_element(self, frame):
        self.frameElement = frame

class MockLocation:
    def __init__(self, href=""):
      self.href = href

# Initialize tryxpath and its functions
tryxpath = {}
tryxpath.functions = {}
tx = tryxpath
fu = tryxpath.functions

# Load the JavaScript code into the namespace for tests to use
exec("""
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

// namespace
if (!tryxpath) {
    var tryxpath = {};
}
if (!tryxpath.functions) {
    tryxpath.functions = {};
}

(function (window, undefined) {
    "use strict";

    // alias
    var tx = tryxpath;
    var fu = tryxpath.functions;

    // prevent multiple execution
    if (fu.done) {
        return;
    }
    fu.done = true;

    fu.execExpr = function(expr, method, opts) {
        opts = opts || {};
        var context = opts.context || document;
        var resolver = ("resolver" in opts) ? opts.resolver : null;
        var doc = opts.document || fu.getOwnerDocument(context) || context;

        var items, resultType;

        switch (method) {
        case "evaluate":
            if (!fu.isNodeItem(context) && !fu.isAttrItem(context)) {
                throw new Error("The context is either Nor nor Attr.");
            }
            resolver = fu.makeResolver(resolver);
            resultType = opts.resultType || xpathResult.ANY_TYPE;
            let result = doc.evaluate(expr, context, resolver, resultType,
                                      null);
            items = fu.resToArr(result, resultType);
            if (resultType === xpathResult.ANY_TYPE) {
                resultType = result.resultType;
            }
            break;

        case "querySelector":
            if (!fu.isDocOrElem(context)) {
                throw new Error("The context is either Document nor Element.");
            }
            let elem = context.querySelector(expr);
            items = elem ? [elem] : [];
            resultType = null;
            break;

        case "querySelectorAll":
        default:
            if (!fu.isDocOrElem(context)) {
                throw new Error(
                    "The context is neither Document nor Element.");
            }
            let elems = context.querySelectorAll(expr);
            items = fu.listToArr(elems);
            resultType = null;
            break;
        }

        return {
            "items": items,
            "method": method,
            "resultType": resultType
        };
    };

    fu.resToArr = function (res, type) {
        if (type === undefined || (type === xpathResult.ANY_TYPE)) {
            type = res.resultType;
        }

        var arr = [];
        switch(type) {
        case xpathResult.NUMBER_TYPE :
            arr.push(res.numberValue);
            break;
        case xpathResult.STRING_TYPE :
            arr.push(res.stringValue);
            break;
        case xpathResult.BOOLEAN_TYPE :
            arr.push(res.booleanValue);
            break;
        case xpathResult.ORDERED_NODE_ITERATOR_TYPE :
        case xpathResult.UNORDERED_NODE_ITERATOR_TYPE :
            for (var node = res.iterateNext()
                 ; node !== null
                 ; node = res.iterateNext()) {
                arr.push(node);
            }
            break;
        case xpathResult.ORDERED_NODE_SNAPSHOT_TYPE :
        case xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE :
            for (var i = 0; i < res.snapshotLength; i++) {
                arr.push(res.snapshotItem(i));
            }
            break;
        case xpathResult.ANY_UNORDERED_NODE_TYPE :
        case xpathResult.FIRST_ORDERED_NODE_TYPE :
            arr.push(res.singleNodeValue);
            break;
        default :
            throw new Error("The resultType is invalid. " + type);
        }
        return arr;
    };
    
    fu.makeResolver = function (obj) {
        if (obj === null) {
            return null;
        }
        if (typeof(obj) === "function") {
            return obj;
        }

        var dict;
        if (typeof(obj) === "string") {
            try {
                dict = JSON.parse(obj);
            } catch (e) {
                throw new Error("Invalid resolver [" + obj + "]. : "
                                + e.message);                
            }
        } else {
            dict = obj;
        }

        if (fu.isValidDict(dict)) {
            let map = fu.objToMap(dict);
            return function (str) {
                if (map.has(str)) {
                    return map.get(str);
                }
                return "";
            };
        }
        throw new Error("Invalid resolver. "
                        + JSON.stringify(dict, null));
    };

    fu.isValidDict = function (obj) {
        if ((obj === null) || (typeof(obj) !== "object")) {
            return false;
        }
        for (var key of Object.keys(obj)) {
            if (typeof(obj[key]) !== "string") {
                return false;
            }
        }
        return true;
    };

    fu.objToMap = function (obj) {
        var map = new Map();
        Object.keys(obj).forEach(function(item) {
            map.set(item, obj[item]);
        });
        return map;
    };

    fu.isDocOrElem = function(obj) {
        if ((obj.nodeType === 1) || (obj.nodeType === 9)) {
            return true;
        }
        return false;
    };

    fu.listToArr = function(list) {
        var elems = [];
        for (var i = 0; i < list.length; i++) {
            elems.push(list[i]);
        }
        return elems;
    };

    fu.getItemDetail = function (item) {
        var typeStr = typeof(item);

        switch (typeof(item)) {
        case "string":
            return {
                "type": "String",
                "name": "",
                "value": item,
                "textContent": ""
            };
        case "number":
            return {
                "type": "Number",
                "name": "",
                "value": item.toString(),
                "textContent": ""
            };
        case "boolean":
            return {
                "type": "Boolean",
                "name": "",
                "value": item.toString(),
                "textContent": ""
            };
        }

        // item is Element
        if (fu.isElementItem(item)) {
            return {
                "type": "Node " + fu.getNodeTypeStr(item.nodeType)
                    + "(nodeType=" + item.nodeType + ")",
                "name": item.nodeName,
                "value": "",
                "textContent": item.textContent
            };
        }
        
        // item is Attr
        if (fu.isAttrItem(item)) {
            return {
                "type": "Attr",
                "name": item.name,
                "value": item.value,
                "textContent": ""
            };
        }

        // item is Node
        return {
            "type": "Node " + fu.getNodeTypeStr(item.nodeType) + "(nodeType="
                + item.nodeType + ")",
            "name": item.nodeName,
            "value": item.nodeValue || "",
            "textContent": item.textContent || ""
        };
    };

    fu.getItemDetails = function (items) {
        var details = [];
        for (var i = 0; i < items.length; i++) {
            details.push(fu.getItemDetail(items[i]));
        }
        return details;
    };

    const nodeTypeMap = new Map([
        [Node.ELEMENT_NODE, "ELEMENT_NODE"],
        [Node.ATTRIBUTE_NODE, "ATTRIBUTE_NODE"],
        [Node.TEXT_NODE, "TEXT_NODE"],
        [Node.CDATA_SECTION_NODE, "CDATA_SECTION_NODE"],
        [Node.ENTITY_REFERENCE_NODE, "ENTITY_REFERENCE_NODE"],
        [Node.ENTITY_NODE, "ENTITY_NODE"],
        [Node.PROCESSING_INSTRUCTION_NODE, "PROCESSING_INSTRUCTION_NODE"],
        [Node.COMMENT_NODE, "COMMENT_NODE"],
        [Node.DOCUMENT_NODE, "DOCUMENT_NODE"],
        [Node.DOCUMENT_TYPE_NODE, "DOCUMENT_TYPE_NODE"],
        [Node.DOCUMENT_FRAGMENT_NODE, "DOCUMENT_FRAGMENT_NODE"],
        [Node.NOTATION_NODE, "NOTATION_NODE"]
    ]);

    fu.getNodeTypeStr = function(nodeType) {
        if (nodeTypeMap.has(nodeType)) {
            return nodeTypeMap.get(nodeType);
        }
        return "Unknown";
    };

    const xpathResultMaps = {
        "numToStr" : new Map([
            [xpathResult.ANY_TYPE, "ANY_TYPE"],
            [xpathResult.NUMBER_TYPE , "NUMBER_TYPE"],
            [xpathResult.STRING_TYPE , "STRING_TYPE"],
            [xpathResult.BOOLEAN_TYPE , "BOOLEAN_TYPE"],
            [xpathResult.UNORDERED_NODE_ITERATOR_TYPE ,
             "UNORDERED_NODE_ITERATOR_TYPE"],
            [xpathResult.ORDERED_NODE_ITERATOR_TYPE ,
             "ORDERED_NODE_ITERATOR_TYPE"],
            [xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE ,
             "UNORDERED_NODE_SNAPSHOT_TYPE"],
            [xpathResult.ORDERED_NODE_SNAPSHOT_TYPE ,
             "ORDERED_NODE_SNAPSHOT_TYPE"],
            [xpathResult.ANY_UNORDERED_NODE_TYPE, "ANY_UNORDERED_NODE_TYPE"],
            [xpathResult.FIRST_ORDERED_NODE_TYPE, "FIRST_ORDERED_NODE_TYPE"]
        ]),

        "strToNum" : new Map([
            ["ANY_TYPE", xpathResult.ANY_TYPE],
            ["NUMBER_TYPE", xpathResult.NUMBER_TYPE],
            ["STRING_TYPE", xpathResult.STRING_TYPE],
            ["BOOLEAN_TYPE", xpathResult.BOOLEAN_TYPE],
            ["UNORDERED_NODE_ITERATOR_TYPE",
             xpathResult.UNORDERED_NODE_ITERATOR_TYPE],
            ["ORDERED_NODE_ITERATOR_TYPE",
             xpathResult.ORDERED_NODE_ITERATOR_TYPE],
            ["UNORDERED_NODE_SNAPSHOT_TYPE",
             xpathResult.UNORDERED_NODE_SNAPSHOT_TYPE],
            ["ORDERED_NODE_SNAPSHOT_TYPE",
             xpathResult.ORDERED_NODE_SNAPSHOT_TYPE],
            ["ANY_UNORDERED_NODE_TYPE", xpathResult.ANY_UNORDERED_NODE_TYPE],
            ["FIRST_ORDERED_NODE_TYPE", xpathResult.FIRST_ORDERED_NODE_TYPE]
        ])
    };

    fu.getxpathResultStr = function (resultType) {
        if (xpathResultMaps.numToStr.has(resultType)) {
            return xpathResultMaps.numToStr.get(resultType);
        }
        return "Unknown";
    };

    fu.getxpathResultNum = function (resultTypeStr) {
        if (xpathResultMaps.strToNum.has(resultTypeStr)) {
            return xpathResultMaps.strToNum.get(resultTypeStr);
        }
        return NaN;
    };

    fu.isAttrItem = function (item) {
        return Object.prototype.toString.call(item) === "[object Attr]";
    };

    fu.isNodeItem = function (item) {
        if (fu.isAttrItem(item)) {
            return false;
        }

        switch (typeof(item)) {
        case "string":
        case "number":
            return false;
        default:
            return true;
        }
    };
    
    fu.isElementItem = function (item) {
        if (fu.isNodeItem(item)
            && (item.nodeType === Node.ELEMENT_NODE)) {
            return true;
        }
        return false;
    };

    fu.addClassToItem = function (clas, item) {
        if (fu.isElementItem(item)) {
            item.classList.add(clas);
        }
    };

    fu.addClassToItems = function (clas, items) {
        for (var item of items) {
            fu.addClassToItem(clas, item);
        }
    };

    fu.saveItemClass = function (item) {
        if (!fu.isElementItem(item)) {
            return null;
        }

        var clas;
        if (item.hasAttribute("class")) {
            clas = item.getAttribute("class");
        } else {
            clas = null;
        }
        return {
            "elem": item,
            "origClass": clas
        }
    };

    fu.restoreItemClass = function (savedClass) {
        if (savedClass === null) {
            return null;
        }

        if (savedClass.origClass === null) {
            savedClass.elem.removeAttribute("class");
        } else {
            savedClass.elem.setAttribute("class", savedClass.origClass);
        }
    };

    fu.saveItemClasses = function (items) {
        var savedClasses = [];
        for (var item of items) {
            savedClasses.push(fu.saveItemClass(item));
        }
        return savedClasses;
    };

    fu.restoreItemClasses = function (savedClasses) {
        for (var savedClass of savedClasses) {
            fu.restoreItemClass(savedClass);
        }
    };

    fu.setAttrToItem = function(name, value, item) {
        if (fu.isElementItem(item)) {
            item.setAttribute(name, value);
        }
    };

    fu.removeAttrFromItem = function(name, item) {
        if (fu.isElementItem(item)) {
            item.removeAttribute(name);
        }
    };

    fu.removeAttrFromItems = function(name, items) {
        items.forEach(item => {
            fu.removeAttrFromItem(name, item);
        });
    };

    fu.setIndexToItems = function(name, items) {
        for (var i = 0; i < items.length; i++) {
            fu.setAttrToItem(name, i, items[i]);
        }
    };

    fu.getParentElement = function (item) {
        if (fu.isAttrItem(item)) {
            let parent = item.ownerElement;
            return parent ? parent : null;
        }

        if (fu.isNodeItem(item)) {
            let parent = item.parentElement;
            if (parent) {
                return parent;
            }
            parent = item.parentNode;
            if (parent && (parent.nodeType === Node.ELEMENT_NODE)) {
                return parent;
            }
        }
        return null;
    };

    fu.getAncestorElements = function (elem) {
        var ancs = [];

        var cur = elem;
        var parent = cur.parentElement;
        while (parent) {
            ancs.push(parent);
            cur = parent;
            parent = cur.parentElement;
        }

        parent = cur.parentNode;
        while (parent && (parent.nodeType === Node.ELEMENT_NODE)) {
            ancs.push(cur);
            cur = parent;
            parent = cur.parentNode;
        }
        
        return ancs;
    };

    fu.getOwnerDocument = function (item) {
        if (fu.isAttrItem(item)) {
            let elem = item.ownerElement;
            if (elem) {
                return elem.ownerDocument;
            }
            return item.ownerDocument;
        }

        if (fu.isNodeItem(item)) {
            return item.ownerDocument;
        }

        return null;
    };

    fu.createHeaderRow = function (values, opts) {
        opts = opts || {};
        var doc = opts.document || document;

        var tr = doc.createElement("tr");
        for (let value of values) {
            let th = doc.createElement("th");
            th.textContent = value;
            tr.appendChild(th);
        }
        return tr;
    };

    fu.createDetailTableHeader = function (opts) {
        opts = opts || {};
        var doc = opts.document || document;

        var tr = doc.createElement("tr");
        var th = doc.createElement("th");
        th.textContent = "Index";
        tr.appendChild(th);
        
        th = doc.createElement("th");
        th.textContent = "Type";
        tr.appendChild(th);

        th = doc.createElement("th");
        th.textContent = "Name";
        tr.appendChild(th);

        th = doc.createElement("th");
        th.textContent = "Value";
        tr.appendChild(th);

        th = doc.createElement("th");
        th.textContent = "Focus";
        tr.appendChild(th);

        return tr;
    };

    fu.createDetailRow = function (index, detail, opts) {
        opts = opts || {};
        var doc = opts.document || document;
        var keys = opts.keys || ["type", "name", "value"];

        var tr = doc.createElement("tr");

        var td = doc.createElement("td");
        td.textContent = index;
        tr.appendChild(td);

        for (let key of keys) {
            let td = doc.createElement("td");
            td.textContent = detail[key];
            tr.appendChild(td);
        }

        td = doc.createElement("td");
        var button = doc.createElement("button");
        button.textContent = "Focus";
        button.setAttribute("data-index", index);
        td.appendChild(button);
        tr.appendChild(td);

        return tr;
    };

    fu.appendDetailRows = function (parent, details, opts) {
        return Promise.resolve().then(() => {
            opts = opts || {};
            var chunkSize = opts.chunkSize || 1000;
            var begin = opts.begin || 0;
            var end = opts.end || details.length;
            var createRow = opts.createRow || fu.createDetailRow.bind(fu);
            var detailKeys = opts.detailKeys || undefined;

            var doc = parent.ownerDocument;
            var frag = doc.createDocumentFragment();
            var index = Math.max(begin, 0);
            var chunkEnd = Math.min(index + chunkSize, details.length, end);

            for ( ; index < chunkEnd; index++) {
                frag.appendChild(createRow(index, details[index], {
                    "document": doc,
                    "keys": detailKeys
                }));
            }
            parent.appendChild(frag);

            if ((index < end) && (index < details.length)) {
                return fu.appendDetailRows(parent, details, {
                    "chunkSize": chunkSize,
                    "begin": index,
                    "end": end,
                    "createRow": createRow,
                    "detailKeys": detailKeys
                });
            } else {
                return ;
            }
        });
    };

    fu.updateDetailsTable = function (parent, details, opts) {
        opts = opts || {};
        var chunkSize = opts.chunkSize || 1000;
        var begin = opts.begin || 0;
        var end = opts.end || details.length;
        var detailKeys = opts.detailKeys || undefined;
        var headerValues;
        if (opts.headerValues) {
            headerValues = ["Index"].concat(opts.headerValues, ["Focus"]);
        } else {
            headerValues = ["Index", "Type", "Name", "Value", "Focus"];
        }

        var doc = parent.ownerDocument;

        fu.emptyChildNodes(parent);
        parent.appendChild(fu.createHeaderRow(headerValues,
                                              { "document": doc }));

        return fu.appendDetailRows(parent, details, {
            "chunkSize": chunkSize,
            "begin": begin,
            "end": end,
            "detailKeys": detailKeys
        });
    };

    fu.emptyChildNodes = function (elem) {
        while (elem.firstChild) {
            elem.removeChild(elem.firstChild);
        }
    };

    fu.saveAttrForItem = function(item, attr, storage, overwrite) {
        storage = storage || new Map();
        
        if (!fu.isElementItem(item)) {
            return storage;
        }

        var elemStor;
        if (storage.has(item)) {
            elemStor = storage.get(item);
        } else {
            elemStor = new Map();
            storage.set(item, elemStor);
        }
        
        var val = item.hasAttribute(attr) ? item.getAttribute(attr)
            : null;

        if (overwrite || !elemStor.has(attr)) {
            elemStor.set(attr, val);
        }

        return storage;
    };

    fu.saveAttrForItems = function(items, attr, storage, overwrite) {
        storage = storage || new Map();

        for (var item of items) {
            fu.saveAttrForItem(item, attr, storage, overwrite);
        }

        return storage;
    };

    fu.restoreItemAttrs = function (storage) {
        for (var [elem, elemStor] of storage) {
            for (var [attr, value] of elemStor) {
                if (value === null) {
                    elem.removeAttribute(attr);
                } else {
                    elem.setAttribute(attr, value);
                }
            }
        }
    };

    fu.getFrameAncestry = function (inds, win) {
        win = win || window;

        var frames = [];
        for (let i = 0; i < inds.length; i++) {
            win = win.frames[inds[i]];
            if (!win) {
                throw new Error("The specified frame does not exist.");
            }
            let frame;
            try {
                frame = win.frameElement;
            } catch (e) {
                throw new Error("Access denied.");
            }
            frames.push(frame);
        };
        return frames;
    };

    // If arr is empty this function returns true.
    fu.isNumberArray = function (arr) {
        if (!Array.isArray(arr)) {
            return false;
        }

        for (var item of arr) {
            if (typeof(item) !== "number") {
                return false;
            }
        }

        return true;
    };

    fu.onError = function (err) {
        // console.log(err);
    };

    fu.isBlankWindow = function (win) {
        try {
            return (win.location.href === "about:blank");
        } catch (e) {
        }
        return false;
    };

    fu.collectBlankWindows = function (top) {
        var wins = [];
        var frames = top.frames;
        for (let i = 0; i < frames.length; i++) {
            let win = frames[i];
            if (fu.isBlankWindow(win)) {
                wins.push(win);
                wins = wins.concat(fu.collectBlankWindows(win));
            }
        }
        return wins;
    };

    fu.findFrameElement = function (win, parent) {
        try {
            var frames = parent.document.getElementsByTagName("iframe");
            for (let i = 0; i < frames.length; i++) {
                if (win === frames[i].contentWindow) {
                    return frames[i];
                }
            }
        } catch (e) {
        }
        return null;
    };

    fu.findFrameIndex = function (win, parent) {
        try {
            var wins = parent.frames;
            for (let i = 0; i < wins.length; i++) {
                if (win === wins[i]) {
                    return i;
                }
            }
        } catch (e) {
        }
        return -1;
    };

    fu.makeDetailText = function (detail, keys, separator = ",",
                                  replacers = Object.create(null)) {
        let texts = [];

        keys.forEach(key => {
            let val = detail[key];
            if (replacers[key]) {
                val = replacers[key](val);\
            }
            texts.push(val);
        })
        return texts.join(separator);
    };

})(window);
""")

@pytest.fixture
def mock_document():
    """Provides a mock document for testing."""
    return MockDocument()

@pytest.fixture
def mock_window():
    """Provides a mock window for testing."""
    return MockWindow()

def test_execExpr_evaluate_valid_node_context(mock_document):
    """Checks correct behavior of execExpr with evaluate method and valid node context."""
    context = MockNode(MockNode.ELEMENT_NODE, "div", ownerDocument = mock_document)
    result = fu.execExpr("//p", "evaluate", {"context": context, "resultType": MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE, "document": mock_document})
    assert result["method"] == "evaluate"
    assert result["resultType"] == MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE
    assert len(result["items"]) == 2
    assert result["items"][0].nodeName == "p"
    assert result["items"][0].textContent == "p1_content"
    
def test_execExpr_evaluate_valid_attr_context(mock_document):
    """Checks correct behavior of execExpr with evaluate method and valid attr context."""
    context = MockAttr("test", "value", MockNode(MockNode.ELEMENT_NODE, "div", ownerDocument = mock_document))
    result = fu.execExpr("//p", "evaluate", {"context": context, "resultType": MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE, "document": mock_document})
    assert result["method"] == "evaluate"
    assert result["resultType"] == MockXPathResult.UNORDERED_NODE_ITERATOR_TYPE
    assert len(result["items"]) == 2
    assert result["items"][0].nodeName == "p"
    assert result["items"][0].textContent == "p1_content"

def test_execExpr_evaluate_invalid_context():
    """Checks execExpr throws an error when context is not node or attr."""
    context = "invalid_context"
    with pytest.raises(Error, match="The context is either Nor nor Attr."):
        fu.execExpr("//p", "evaluate", {"context": context})

def test_execExpr_evaluate_number_result(mock_document):
   """Checks correct number result with evaluate method."""
   context = MockNode(MockNode.ELEMENT_NODE, "div", ownerDocument = mock_document)
   result = fu.execExpr("//b", "evaluate", {"context": context, "resultType": MockXPathResult.NUMBER_TYPE, "document": mock_document})
   assert result["items"] == [123]
   assert result["resultType"] == MockXPathResult.NUMBER_TYPE

def test_execExpr_evaluate_string_result(mock_