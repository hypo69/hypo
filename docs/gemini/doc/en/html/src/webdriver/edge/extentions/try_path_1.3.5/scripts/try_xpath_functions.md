html
<h1>try_xpath_functions.js</h1>

<h2>Overview</h2>
<p>This JavaScript file defines functions for evaluating XPath expressions, querying elements using querySelector and querySelectorAll, and manipulating DOM elements.  It provides methods to interact with the DOM, extract data from XPath results, and handle different data types returned by XPath queries.  The functions are designed to be reusable and handle various error scenarios.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#execExpr"><code>execExpr</code></a></li>
  <li><a href="#resToArr"><code>resToArr</code></a></li>
  <li><a href="#makeResolver"><code>makeResolver</code></a></li>
  <li><a href="#isValidDict"><code>isValidDict</code></a></li>
  <li><a href="#objToMap"><code>objToMap</code></a></li>
  <li><a href="#isDocOrElem"><code>isDocOrElem</code></a></li>
  <li><a href="#listToArr"><code>listToArr</code></a></li>
  <li><a href="#getItemDetail"><code>getItemDetail</code></a></li>
  <li><a href="#getItemDetails"><code>getItemDetails</code></a></li>
  <li><a href="#getNodeTypeStr"><code>getNodeTypeStr</code></a></li>
  <li><a href="#getxpathResultStr"><code>getxpathResultStr</code></a></li>
  <li><a href="#getxpathResultNum"><code>getxpathResultNum</code></a></li>
  <li><a href="#isAttrItem"><code>isAttrItem</code></a></li>
  <li><a href="#isNodeItem"><code>isNodeItem</code></a></li>
  <li><a href="#isElementItem"><code>isElementItem</code></a></li>
  <li><a href="#addClassToItem"><code>addClassToItem</code></a></li>
  <li><a href="#addClassToItems"><code>addClassToItems</code></a></li>
  <li><a href="#saveItemClass"><code>saveItemClass</code></a></li>
  <li><a href="#restoreItemClass"><code>restoreItemClass</code></a></li>
  <li><a href="#saveItemClasses"><code>saveItemClasses</code></a></li>
  <li><a href="#restoreItemClasses"><code>restoreItemClasses</code></a></li>
  <li><a href="#setAttrToItem"><code>setAttrToItem</code></a></li>
  <li><a href="#removeAttrFromItem"><code>removeAttrFromItem</code></a></li>
  <li><a href="#removeAttrFromItems"><code>removeAttrFromItems</code></a></li>
  <li><a href="#setIndexToItems"><code>setIndexToItems</code></a></li>
  <li><a href="#getParentElement"><code>getParentElement</code></a></li>
  <li><a href="#getAncestorElements"><code>getAncestorElements</code></a></li>
  <li><a href="#getOwnerDocument"><code>getOwnerDocument</code></a></li>
  <li><a href="#createHeaderRow"><code>createHeaderRow</code></a></li>
  <li><a href="#createDetailTableHeader"><code>createDetailTableHeader</code></a></li>
  <li><a href="#createDetailRow"><code>createDetailRow</code></a></li>
  <li><a href="#appendDetailRows"><code>appendDetailRows</code></a></li>
  <li><a href="#updateDetailsTable"><code>updateDetailsTable</code></a></li>
  <li><a href="#emptyChildNodes"><code>emptyChildNodes</code></a></li>
  <li><a href="#saveAttrForItem"><code>saveAttrForItem</code></a></li>
  <li><a href="#saveAttrForItems"><code>saveAttrForItems</code></a></li>
  <li><a href="#restoreItemAttrs"><code>restoreItemAttrs</code></a></li>
  <li><a href="#getFrameAncestry"><code>getFrameAncestry</code></a></li>
  <li><a href="#isNumberArray"><code>isNumberArray</code></a></li>
  <li><a href="#onError"><code>onError</code></a></li>
  <li><a href="#isBlankWindow"><code>isBlankWindow</code></a></li>
  <li><a href="#collectBlankWindows"><code>collectBlankWindows</code></a></li>
  <li><a href="#findFrameElement"><code>findFrameElement</code></a></li>
  <li><a href="#findFrameIndex"><code>findFrameIndex</code></a></li>
  <li><a href="#makeDetailText"><code>makeDetailText</code></a></li>
</ul>

<h2 id="execExpr"><code>execExpr</code></h2>

<h3>Description</h3>
<p>Executes an XPath expression or CSS selector on a given context.</p>

<h3>Parameters</h3>
<ul>
  <li><code>expr</code> (str): The XPath expression or CSS selector.</li>
  <li><code>method</code> (str): The method to use ("evaluate", "querySelector", or "querySelectorAll").</li>
  <li><code>opts</code> (Optional[object], optional): An optional object containing options.  Defaults to an empty object.  It can include <code>context</code>, <code>resolver</code> and <code>document</code> attributes. </li>
</ul>

<h3>Returns</h3>
<ul>
  <li><code>object</code>: An object containing the results.</li>
</ul>

<h3>Raises</h3>
<ul>
  <li><code>Error</code>: An error object describing the issue in case of invalid context type or resolver.</li>
</ul>

<h2 id="resToArr"><code>resToArr</code></h2>
<!-- Function documentation for resToArr -->
<!-- ... -->

<h2 id="makeResolver"><code>makeResolver</code></h2>
<!-- Function documentation for makeResolver -->
<!-- ... -->

<!-- Similar documentation for all other functions follows -->
<!-- ... -->

```