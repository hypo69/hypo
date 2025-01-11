## Анализ кода `try_xpath_functions.js`

### 1. <алгоритм>

#### Основная цель
Код предоставляет набор функций для выполнения XPath-выражений, работы с DOM, получения деталей об элементах и их атрибутах, а также управления стилями и атрибутами.

#### Блок-схема

```mermaid
graph TD
    A[Start] --> B{`tryxpath` namespace initialized?};
    B -- No --> C[Initialize `tryxpath` namespace and `functions`];
    B -- Yes --> D{`tryxpath.functions.done`?};
    D -- Yes --> E[End function execution];
    D -- No --> F[Set `tryxpath.functions.done` = `true`];
    F --> G[Define `fu.execExpr`];
    G --> H{Method = "evaluate"?};
    H -- Yes --> I{Is `context` a Node or Attr?};
    I -- No --> J[Throw Error: "The context is either Nor nor Attr."];
    I -- Yes --> K[Make Resolver];
    K --> L[Evaluate XPath];
    L --> M[Convert result to array];
    M --> N[Return result];
    H -- No --> O{Method = "querySelector"?};
    O -- Yes --> P{Is `context` a Document or Element?};
    P -- No --> Q[Throw Error: "The context is either Document nor Element."];
    P -- Yes --> R[Execute `querySelector`];
    R --> S[Convert Element to array];
    S --> N;
    O -- No --> T{Is `context` a Document or Element?};
    T -- No --> U[Throw Error: "The context is neither Document nor Element."];
    T -- Yes --> V[Execute `querySelectorAll`];
    V --> W[Convert NodeList to array];
    W --> N;
    N --> X[Define `fu.resToArr`];
        X --> Y{resultType is ANY_TYPE?};
    Y -- Yes --> Z[Set type = result.resultType];
    Y -- No --> Z;
    Z --> AA{resultType is NUMBER_TYPE?};
    AA -- Yes --> AB[Push res.numberValue to array];
    AA -- No --> AC{resultType is STRING_TYPE?};
    AC -- Yes --> AD[Push res.stringValue to array];
    AC -- No --> AE{resultType is BOOLEAN_TYPE?};
    AE -- Yes --> AF[Push res.booleanValue to array];
    AE -- No --> AG{resultType is ORDERED_NODE_ITERATOR_TYPE or UNORDERED_NODE_ITERATOR_TYPE?};
   AG -- Yes --> AH[Iterate through nodes];
    AH --> AI[Push node to array];
    AI --> AG;
    AG -- No --> AJ{resultType is ORDERED_NODE_SNAPSHOT_TYPE or UNORDERED_NODE_SNAPSHOT_TYPE?};
    AJ -- Yes --> AK[Iterate through snapshot];
   AK --> AL[Push snapshot item to array];
    AL --> AJ;
    AJ -- No --> AM{resultType is ANY_UNORDERED_NODE_TYPE or FIRST_ORDERED_NODE_TYPE?};
    AM -- Yes --> AN[Push res.singleNodeValue to array];
    AM -- No --> AO[Throw Error: "The resultType is invalid."];
    AN --> AP[Return array];
     AB --> AP;
     AD --> AP;
     AF --> AP;
     AO --> AP;
    AP --> AQ[Define `fu.makeResolver`];
    AQ --> AR{obj is null?};
    AR -- Yes --> AS[Return null];
    AR -- No --> AT{obj is function?};
    AT -- Yes --> AU[Return obj];
    AT -- No --> AV{obj is string?};
    AV -- Yes --> AW[Parse JSON];
    AW --> AX{JSON is valid?};
    AX -- No --> AY[Throw error: "Invalid resolver"];
    AX -- Yes --> AZ;
    AV -- No --> AZ;
    AZ --> BA{Is dict valid?};
    BA -- No --> BB[Throw Error: "Invalid resolver"];
    BA -- Yes --> BC[Create Map];
        BC --> BD[Return resolver function];
    AS --> BD;
    AU --> BD;
    BD --> BE[Define `fu.isValidDict`];
    BE --> BF{obj is null or not object?};
    BF -- Yes --> BG[Return false];
    BF -- No --> BH[Iterate through object keys];
    BH --> BI{Is value string?};
    BI -- No --> BG;
    BI -- Yes --> BH;
    BH -- end --> BJ[Return true];
      BG --> BJ;
    BJ --> BK[Define `fu.objToMap`];
    BK --> BL[Create new Map];
        BL --> BM[Iterate through object keys];
    BM --> BN[Set key-value to map];
    BN --> BM;
    BM --end--> BO[Return map];
    BO --> BP[Define `fu.isDocOrElem`];
    BP --> BQ{Is nodeType 1 or 9?};
    BQ -- Yes --> BR[Return true];
    BQ -- No --> BS[Return false];
    BR --> BT[Define `fu.listToArr`];
    BS --> BT;
    BT --> BU[Create array];
    BU --> BV[Iterate through list];
    BV --> BW[Push item to array];
    BW --> BV;
     BV -- end --> BX[Return array];
    BX --> BY[Define `fu.getItemDetail`];
    BY --> BZ{typeof(item) is "string"?};
    BZ -- Yes --> CA[Return String details];
    BZ -- No --> CB{typeof(item) is "number"?};
    CB -- Yes --> CC[Return Number details];
    CB -- No --> CD{typeof(item) is "boolean"?};
    CD -- Yes --> CE[Return Boolean details];
    CD -- No --> CF{Is `item` an Element?};
    CF -- Yes --> CG[Return Element details];
    CF -- No --> CH{Is `item` an Attr?};
    CH -- Yes --> CI[Return Attr details];
    CH -- No --> CJ[Return Node details];
    CA --> CK[Define `fu.getItemDetails`];
    CC --> CK;
    CE --> CK;
    CG --> CK;
    CI --> CK;
    CJ --> CK;
    CK --> CL[Create array];
    CL --> CM[Iterate through items];
        CM --> CN[Push result of `fu.getItemDetail`];
    CN --> CM;
    CM --end--> CO[Return array];
        CO --> CP[Define `nodeTypeMap`];
      CP --> CQ[Define `fu.getNodeTypeStr`];
   CQ --> CR{nodeTypeMap has nodeType?};
    CR -- Yes --> CS[Return mapped string];
    CR -- No --> CT[Return "Unknown"];
   CS --> CU[Define `xpathResultMaps`];
   CT --> CU;
    CU --> CV[Define `fu.getxpathResultStr`];
    CV --> CW{`xpathResultMaps.numToStr` has `resultType`?};
    CW -- Yes --> CX[Return mapped string];
    CW -- No --> CY[Return "Unknown"];
    CX --> CZ[Define `fu.getxpathResultNum`];
    CY --> CZ;
    CZ --> DA{`xpathResultMaps.strToNum` has `resultTypeStr`?};
    DA -- Yes --> DB[Return mapped number];
    DA -- No --> DC[Return `NaN`];
    DB --> DD[Define `fu.isAttrItem`];
    DC --> DD;
   DD --> DE[Check if item is Attr];
   DE --> DF[Return result];
    DF --> DG[Define `fu.isNodeItem`];
    DG --> DH{isAttrItem?};
    DH -- Yes --> DI[Return false];
    DH -- No --> DJ{typeof item is "string" or "number"?};
    DJ -- Yes --> DK[Return false];
    DJ -- No --> DL[Return true];
     DK --> DM[Define `fu.isElementItem`];
    DL --> DM;
    DM --> DN{isNodeItem and nodeType is `Node.ELEMENT_NODE`?};
   DN -- Yes --> DO[Return true];
    DN -- No --> DP[Return false];
        DO --> DQ[Define `fu.addClassToItem`];
        DP --> DQ;
     DQ --> DR{isElementItem?};
    DR -- Yes --> DS[Add class to item];
    DR -- No --> DT;
       DT --> DU[Define `fu.addClassToItems`];
     DU --> DV[Iterate through items];
      DV --> DW[Call `fu.addClassToItem`];
        DW --> DV;
        DV --end--> DX[Define `fu.saveItemClass`];
    DX --> DY{isElementItem?};
    DY -- No --> DZ[Return null];
   DY -- Yes --> EA{Check for "class" attribute};
    EA -- Yes --> EB[Save class attribute];
    EA -- No --> EC[Set class to null];
    EB --> ED[Return object with element and class];
    EC --> ED;
    DZ --> ED;
    ED --> EE[Define `fu.restoreItemClass`];
    EE --> EF{savedClass is null?};
    EF -- Yes --> EG[Return null];
    EF -- No --> EH{savedClass.origClass is null?};
    EH -- Yes --> EI[Remove class attribute];
    EH -- No --> EJ[Set class attribute];
    EI --> EK[Define `fu.saveItemClasses`];
    EJ --> EK;
    EG --> EK;
    EK --> EL[Create array];
    EL --> EM[Iterate through items];
    EM --> EN[Save class using `fu.saveItemClass`];
    EN --> EM;
    EM --end--> EO[Return array of saved classes];
        EO --> EP[Define `fu.restoreItemClasses`];
    EP --> EQ[Iterate through savedClasses];
    EQ --> ER[Restore class using `fu.restoreItemClass`];
    ER --> EQ;
    EQ --end--> ES[Define `fu.setAttrToItem`];
    ES --> ET{isElementItem?};
    ET -- Yes --> EU[Set attribute to element];
    ET -- No --> EV;
       EV --> EW[Define `fu.removeAttrFromItem`];
    EW --> EX{isElementItem?};
    EX -- Yes --> EY[Remove attribute from element];
    EX -- No --> EZ[Define `fu.removeAttrFromItems`];
    EY --> EZ;
    EZ --> FA[Iterate through items];
    FA --> FB[Remove attribute using `fu.removeAttrFromItem`];
    FB --> FA;
    FA --end--> FC[Define `fu.setIndexToItems`];
    FC --> FD[Iterate through items];
    FD --> FE[Set index as attribute using `fu.setAttrToItem`];
    FE --> FD;
     FD --end--> FF[Define `fu.getParentElement`];
   FF --> FG{isAttrItem?};
    FG -- Yes --> FH[Get ownerElement];
    FH --> FI{ownerElement exists?};
        FI -- Yes --> FJ[Return ownerElement];
        FI -- No --> FK[Return null];
    FJ --> FL;
    FK --> FL;
     FG -- No --> FM{isNodeItem?};
    FM -- Yes --> FN[Get parentElement];
        FN --> FO{parentElement exists?};
        FO -- Yes --> FP[Return parentElement];
        FO -- No --> FQ[Get parentNode];
    FP --> FL;
        FQ --> FR{parentNode exists and nodeType is ELEMENT_NODE?};
    FR -- Yes --> FS[Return parentNode];
        FR -- No --> FT[Return null];
        FS --> FL;
        FT --> FL;
       FL --> FU[Define `fu.getAncestorElements`];
   FU --> FV[Create array];
        FV --> FW[Get current and parent element];
        FW --> FX{parentElement exists?};
        FX -- Yes --> FY[Push parent element and update parent];
        FY --> FW;
        FX -- No --> FZ[Get parentNode];
       FZ --> GA{parentNode exists and is ELEMENT_NODE?};
        GA -- Yes --> GB[Push node and update parent];
        GB --> GA;
        GA -- No --> GC[Return ancestor array];
         GC --> GD[Define `fu.getOwnerDocument`];
    GD --> GE{isAttrItem?};
    GE -- Yes --> GF[Get ownerElement];
    GF --> GG{ownerElement exists?};
        GG -- Yes --> GH[Return ownerDocument];
        GG -- No --> GI[Return item.ownerDocument];
    GH --> GJ;
    GI --> GJ;
    GE -- No --> GK{isNodeItem?};
    GK -- Yes --> GL[Return ownerDocument];
    GK -- No --> GM[Return null];
        GL --> GJ;
      GM --> GJ;
    GJ --> GN[Define `fu.createHeaderRow`];
    GN --> GO[Create new row];
    GO --> GP[Iterate through values];
    GP --> GQ[Create new header element];
    GQ --> GR[Set text content to header];
    GR --> GS[Append header to row];
    GS --> GP;
    GP --end--> GT[Return row];
        GT --> GU[Define `fu.createDetailTableHeader`];
     GU --> GV[Create new row and header elements];
      GV --> GW[Set header text content];
      GW --> GX[Append header to row];
      GX --> GW;
       GW --end--> GY[Return row];
      GY --> GZ[Define `fu.createDetailRow`];
       GZ --> HA[Create new row];
       HA --> HB[Create new td element];
       HB --> HC[Set index as text content];
       HC --> HD[Append to row];
       HD --> HE[Iterate through keys];
       HE --> HF[Create td and set value as text content];
       HF --> HG[Append td to row];
       HG --> HE;
      HE --end--> HH[Create button and set text content];
     HH --> HI[Set data index to button];
    HI --> HJ[Append button to td];
    HJ --> HK[Append td to row];
    HK --> HL[Return row];
         HL --> HM[Define `fu.appendDetailRows`];
     HM --> HN[Create Promise];
      HN --> HO[Set options];
      HO --> HP[Set `chunkSize`, `begin`, `end`, `createRow`, `detailKeys` variables];
      HP --> HQ[Get document, fragment and index];
      HQ --> HR[Calculate `chunkEnd`];
      HR --> HS[Iterate through elements (index < chunkEnd)];
     HS --> HT[Append row to fragment];
     HT --> HS;
    HS --end--> HU[Append fragment to parent];
    HU --> HV{index < end and index < details.length?};
   HV -- Yes --> HW[Call `fu.appendDetailRows` recursively with updated parameters];
    HV -- No --> HX[Return];
     HW --> HX;
         HX --> HY[Define `fu.updateDetailsTable`];
         HY --> HZ[Set options, `chunkSize`, `begin`, `end`, `detailKeys` variables];
     HZ --> IA{Check for headerValues};
      IA -- Yes --> IB[Set header values with "Index" and "Focus"];
     IA -- No --> IC[Set default header values];
    IB --> ID;
    IC --> ID;
    ID --> IE[Get document];
      IE --> IF[Empty child nodes from parent];
      IF --> IG[Create header row];
    IG --> IH[Call `fu.appendDetailRows`];
        IH --> II[Define `fu.emptyChildNodes`];
     II --> IJ{elem has first child?};
     IJ -- Yes --> IK[Remove first child];
        IK --> IJ;
     IJ -- No --> IL[Define `fu.saveAttrForItem`];
        IL --> IM[Set storage default value];
     IM --> IN{isElementItem?};
      IN -- No --> IO[Return storage];
       IN -- Yes --> IP[Get element storage or create new];
      IP --> IQ[Get attribute or null];
     IQ --> IR{overwrite or storage has no attribute?};
    IR -- Yes --> IS[Set attribute value to storage];
    IR -- No --> IT[Return storage];
       IS --> IT;
    IT --> IU[Define `fu.saveAttrForItems`];
      IU --> IV[Set storage default value];
       IV --> IW[Iterate through items];
     IW --> IX[Call `fu.saveAttrForItem`];
       IX --> IW;
        IW --end--> IY[Return storage];
   IY --> IZ[Define `fu.restoreItemAttrs`];
  IZ --> JA[Iterate through storage];
   JA --> JB[Iterate through attribute storage];
  JB --> JC{value is null?};
     JC -- Yes --> JD[Remove attribute from element];
       JC -- No --> JE[Set attribute to element];
     JD --> JB;
    JE --> JB;
  JB --end--> JA;
    JA --end--> JF[Define `fu.getFrameAncestry`];
   JF --> JG[Set window];
   JG --> JH[Create empty frames array];
    JH --> JI[Iterate through indexes];
     JI --> JJ[Get frame by index];
   JJ --> JK{Frame exists?};
    JK -- No --> JL[Throw Error: "The specified frame does not exist."];
    JK -- Yes --> JM[Get frame element];
      JM --> JN[Push frame element to frames array];
       JN --> JI;
    JI --end--> JO[Return frames array];
      JO --> JP[Define `fu.isNumberArray`];
     JP --> JQ{is array?};
   JQ -- No --> JR[Return false];
  JQ -- Yes --> JS[Iterate through array];
  JS --> JT{typeof item is "number"?};
     JT -- No --> JR;
    JT -- Yes --> JS;
    JS --end--> JU[Return true];
        JR --> JU;
     JU --> JV[Define `fu.onError`];
        JV --> JW[Define `fu.isBlankWindow`];
        JW --> JX{Get location.href of window, catch errors};
         JX -- Yes --> JY[Return (win.location.href === "about:blank")];
         JX -- No --> JZ[Return false];
     JY --> KA[Define `fu.collectBlankWindows`];
        JZ --> KA;
     KA --> KB[Create array of blank windows];
      KB --> KC[Get frames of window];
       KC --> KD[Iterate through frames];
       KD --> KE[Get frame];
      KE --> KF{`fu.isBlankWindow`(frame) is true?};
   KF -- Yes --> KG[Push frame to `wins` array];
  KG --> KH[Recursive call `fu.collectBlankWindows`];
   KH --> KI[Merge recursive result with `wins`];
  KI --> KD;
   KF -- No --> KD;
     KD --end--> KJ[Return `wins` array];
      KJ --> KL[Define `fu.findFrameElement`];
     KL --> KM[Get iframes of parent document];
      KM --> KN[Iterate through iframes];
     KN --> KO{iframe.contentWindow === win?};
      KO -- Yes --> KP[Return iframe element];
      KO -- No --> KN;
    KN --end--> KQ[Return null];
        KP --> KR[Define `fu.findFrameIndex`];
       KQ --> KR;
   KR --> KS[Get frames of parent];
  KS --> KT[Iterate through frames];
   KT --> KU{win === wins[i]?};
    KU -- Yes --> KV[Return index];
    KU -- No --> KT;
  KT --end--> KW[Return -1];
       KV --> KX[Define `fu.makeDetailText`];
      KW --> KX;
    KX --> KY[Create `texts` array];
  KY --> KZ[Iterate through `keys`];
    KZ --> LA[Get value by key];
   LA --> LB{replacers[key] exists?};
   LB -- Yes --> LC[Replace value using function];
    LC --> LD[Push to texts array];
    LB -- No --> LD;
   LD --> KZ;
   KZ --end--> LE[Join texts array and return];
    LE --> LF[End];
```

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph tryxpath
        A[tryxpath namespace]
        B[tryxpath.functions namespace]
        C{fu.done}
    end
     A --> B
     B --> C
    C -- false --> D[fu.execExpr(expr, method, opts)]
    D --> E{method == "evaluate"}
    E -- true --> F[fu.makeResolver(resolver)]
    F --> G[doc.evaluate(expr, context, resolver, resultType, null)]
    G --> H[fu.resToArr(result, resultType)]
    E -- false --> I{method == "querySelector"}
    I -- true --> J[context.querySelector(expr)]
    J --> K[elem ? [elem] : []]
    I -- false --> L[context.querySelectorAll(expr)]
    L --> M[fu.listToArr(elems)]
    H --> N[return {items, method, resultType}]
    K --> N
    M --> N
    N --> O[fu.resToArr(res, type)]
    O --> P{type == ANY_TYPE}
    P -- true --> Q[type = res.resultType]
    Q --> R{type == NUMBER_TYPE}
    P -- false --> R
    R -- true --> S[arr.push(res.numberValue)]
    R -- false --> T{type == STRING_TYPE}
    T -- true --> U[arr.push(res.stringValue)]
    T -- false --> V{type == BOOLEAN_TYPE}
    V -- true --> W[arr.push(res.booleanValue)]
    V -- false --> X{type == ORDERED_NODE_ITERATOR_TYPE or UNORDERED_NODE_ITERATOR_TYPE}
    X -- true --> Y[for node = res.iterateNext(); node != null; node = res.iterateNext()]
    Y --> Z[arr.push(node)]
    X -- false --> AA{type == ORDERED_NODE_SNAPSHOT_TYPE or UNORDERED_NODE_SNAPSHOT_TYPE}
    AA -- true --> AB[for i = 0; i < res.snapshotLength; i++]
    AB --> AC[arr.push(res.snapshotItem(i))]
     AA -- false --> AD{type == ANY_UNORDERED_NODE_TYPE or FIRST_ORDERED_NODE_TYPE}
     AD -- true --> AE[arr.push(res.singleNodeValue)]
     AD -- false --> AF[throw Error("The resultType is invalid.")]
    S --> AG[return arr]
    U --> AG
    W --> AG
    Z --> Y
    AC --> AB
    AE --> AG
    AF --> AG
    AG --> AH[fu.makeResolver(obj)]
    AH --> AI{obj == null}
    AI -- true --> AJ[return null]
    AI -- false --> AK{typeof obj == "function"}
    AK -- true --> AL[return obj]
    AK -- false --> AM{typeof obj == "string"}
    AM -- true --> AN[JSON.parse(obj)]
    AN --> AO{JSON is valid?}
     AO -- false --> AP[throw new Error("Invalid resolver")]
    AO -- true --> AQ
    AM -- false --> AQ
    AQ --> AR[fu.isValidDict(dict)]
    AR -- false --> AS[throw new Error("Invalid resolver")]
    AR -- true --> AT[map = fu.objToMap(dict)]
     AT --> AU[return function(str) { if (map.has(str)) return map.get(str); return "" }]
    AJ --> AU
    AL --> AU
    AS --> AU
    AU --> AV[fu.isValidDict(obj)]
    AV --> AW{obj == null or typeof obj != "object"}
     AW -- true --> AX[return false]
     AW -- false --> AY[for key of Object.keys(obj)]
     AY --> AZ{typeof obj[key] != "string"}
     AZ -- true --> AX
     AZ -- false --> AY
     AY -- end --> BA[return true]
    AX --> BA
    BA --> BB[fu.objToMap(obj)]
     BB --> BC[map = new Map()]
     BC --> BD[Object.keys(obj).forEach(item => map.set(item, obj[item]))]
     BD --> BE[return map]
    BE --> BF[fu.isDocOrElem(obj)]
     BF --> BG{obj.nodeType == 1 or obj.nodeType == 9}
     BG -- true --> BH[return true]
      BG -- false --> BI[return false]
      BH --> BJ[fu.listToArr(list)]
      BI --> BJ
     BJ --> BK[elems = []]
     BK --> BL[for i = 0; i < list.length; i++]
     BL --> BM[elems.push(list[i])]
     BM --> BL
     BL -- end --> BN[return elems]
      BN --> BO[fu.getItemDetail(item)]
     BO --> BP{typeof item == "string"}
    BP -- true --> BQ[return {type="String",name="",value=item,textContent=""}]
    BP -- false --> BR{typeof item == "number"}
    BR -- true --> BS[return {type="Number",name="",value=item.toString(),textContent=""}]
     BR -- false --> BT{typeof item == "boolean"}
    BT -- true --> BU[return {type="Boolean",name="",value=item.toString(),textContent=""}]
     BT -- false --> BV[fu.isElementItem(item)]
   BV -- true --> BW[return {type=Node,name=item.nodeName,value="",textContent=item.textContent}]
  BV -- false --> BX[fu.isAttrItem(item)]
    BX -- true --> BY[return {type="Attr",name=item.name,value=item.value,textContent=""}]
    BX -- false --> BZ[return {type="Node",name=item.nodeName,value=item.nodeValue,textContent=item.textContent}]
    BQ --> CA[fu.getItemDetails(items)]
    BS --> CA
    BU --> CA
    BW --> CA
    BY --> CA
    BZ --> CA
    CA --> CB[details = []]
    CB --> CC[for i = 0; i < items.length; i++]
    CC --> CD[details.push(fu.getItemDetail(items[i]))]
     CD --> CC
    CC -- end --> CE[return details]
    CE --> CF[nodeTypeMap = new Map()]
    CF --> CG[fu.getNodeTypeStr(nodeType)]
    CG --> CH{nodeTypeMap.has(nodeType)}
    CH -- true --> CI[return nodeTypeMap.get(nodeType)]
     CH -- false --> CJ[return "Unknown"]
     CI --> CK[xpathResultMaps = {numToStr: Map(), strToNum: Map()}]
     CJ --> CK
     CK --> CL[fu.getxpathResultStr(resultType)]
      CL --> CM{xpathResultMaps.numToStr.has(resultType)}
    CM -- true --> CN[return xpathResultMaps.numToStr.get(resultType)]
     CM -- false --> CO[return "Unknown"]
    CN --> CP[fu.getxpathResultNum(resultTypeStr)]
    CO --> CP
    CP --> CQ{xpathResultMaps.strToNum.has(resultTypeStr)}
    CQ -- true --> CR[return xpathResultMaps.strToNum.get(resultTypeStr)]
    CQ -- false --> CS[return NaN]
    CR --> CT[fu.isAttrItem(item)]
    CS --> CT
    CT --> CU[return Object.prototype.toString.call(item) == "[object Attr]"]
     CU --> CV[fu.isNodeItem(item)]
     CV --> CW{fu.isAttrItem(item)}
    CW -- true --> CX[return false]
    CW -- false --> CY{typeof item == "string" or typeof item == "number"}
     CY -- true --> CZ[return false]
     CY -- false --> DA[return true]
     CX --> DB[fu.isElementItem(item)]
      CZ --> DB
    DA --> DB
    DB --> DC{fu.isNodeItem(item) && item.nodeType == Node.ELEMENT_NODE}
    DC -- true --> DD[return true]
    DC -- false --> DE[return false]
     DD --> DF[fu.addClassToItem(clas, item)]
      DE --> DF
      DF --> DG{fu.isElementItem(item)}
     DG -- true --> DH[item.classList.add(clas)]
    DG -- false --> DI
      DH --> DJ[fu.addClassToItems(clas, items)]
      DI --> DJ
     DJ --> DK[for item of items]
     DK --> DL[fu.addClassToItem(clas, item)]
     DL --> DK
      DK -- end --> DM[fu.saveItemClass(item)]
    DM --> DN{fu.isElementItem(item)}
    DN -- true --> DO[item.hasAttribute("class") ? item.getAttribute("class") : null]
     DN -- false --> DP[return null]
     DO --> DQ[return {elem:item,origClass:clas}]
    DP --> DQ
    DQ --> DR[fu.restoreItemClass(savedClass)]
    DR --> DS{savedClass == null}
    DS -- true --> DT[return null]
    DS -- false --> DU{savedClass.origClass == null}
    DU -- true --> DV[savedClass.elem.removeAttribute("class")]
    DU -- false --> DW[savedClass.elem.setAttribute("class", savedClass.origClass)]
    DT --> DX[fu.saveItemClasses(items)]
    DV --> DX
    DW --> DX
    DX --> DY[savedClasses = []]
    DY --> DZ[for item of items]
    DZ --> EA[savedClasses.push(fu.saveItemClass(item))]
    EA --> DZ
      DZ -- end --> EB[return savedClasses]
     EB --> EC[fu.restoreItemClasses(savedClasses)]
     EC --> ED[for savedClass of savedClasses]
    ED --> EE[fu.restoreItemClass(savedClass)]
    EE --> ED
    ED -- end --> EF[fu.setAttrToItem(name, value, item)]
   EF --> EG{fu.isElementItem(item)}
   EG -- true --> EH[item.setAttribute(name, value)]
   EG -- false --> EI[fu.removeAttrFromItem(name, item)]
    EH --> EJ[fu.removeAttrFromItems(name, items)]
    EI --> EJ
   EJ --> EK[items.forEach(item => fu.removeAttrFromItem(name, item))]
   EK --> EL[fu.setIndexToItems(name, items)]
   EL --> EM[for i = 0; i < items.length; i++]
   EM --> EN[fu.setAttrToItem(name, i, items[i])]
   EN --> EM
    EM -- end --> EO[fu.getParentElement(item)]
    EO --> EP{fu.isAttrItem(item)}
   EP -- true --> EQ[parent = item.ownerElement]
     EQ --> ER{parent exists?}
     ER -- true --> ES[return parent]
     ER -- false --> ET[return null]
     ES --> EU
     ET --> EU
   EP -- false --> EV{fu.isNodeItem(item)}
    EV -- true --> EW[parent = item.parentElement]
     EW --> EX{parent exists?}
   EX -- true --> EY[return parent]
    EX -- false --> EZ[parent = item.parentNode]
    EY --> EU
    EZ --> FA{parent && parent.nodeType == Node.ELEMENT_NODE}
    FA -- true --> FB[return parent]
    FA -- false --> FC[return null]
    FB --> EU
    FC --> EU
  EU --> FD[fu.getAncestorElements(elem)]
  FD --> FE[ancs = []]
  FE --> FF[cur = elem, parent = cur.parentElement]
  FF --> FG{parent exists?}
  FG -- true --> FH[ancs.push(parent), cur = parent, parent = cur.parentElement]
  FH --> FG
  FG -- false --> FI[parent = cur.parentNode]
  FI --> FJ{parent && parent.nodeType == Node.ELEMENT_NODE}
  FJ -- true --> FK[ancs.push(cur), cur = parent, parent = cur.parentNode]
  FK --> FJ
  FJ -- false --> FL[return ancs]
  FL --> FM[fu.getOwnerDocument(item)]
 FM --> FN{fu.isAttrItem(item)}
 FN -- true --> FO[elem = item.ownerElement]
  FO --> FP{elem exists?}
  FP -- true --> FQ[return elem.ownerDocument]
   FP -- false --> FR[return item.ownerDocument]
  FQ --> FS
  FR --> FS
 FN -- false --> FT{fu.isNodeItem(item)}
FT -- true --> FU[return item.ownerDocument]
  FT -- false --> FV[return null]
   FU --> FS
   FV --> FS
   FS --> FW[fu.createHeaderRow(values, opts)]
   FW --> FX[tr = doc.createElement("tr")]
   FX --> FY[for value of values]
   FY --> FZ[th = doc.createElement("th")]
   FZ --> GA[th.textContent = value]
   GA --> GB[tr.appendChild(th)]
   GB --> FY
  FY -- end --> GC[return tr]
   GC --> GD[fu.createDetailTableHeader(opts)]
   GD --> GE[tr = doc.createElement("tr")]
   GE --> GF[th = doc.createElement("th")]
   GF --> GG[th.textContent = "Index"]
    GG --> GH[tr.appendChild(th)]
  GH --> GI[th = doc.createElement("th")]
    GI --> GJ[th.textContent = "Type"]
     GJ --> GK[tr.appendChild(th)]
    GK --> GL[th = doc.createElement("th")]
      GL --> GM[th.textContent = "Name"]
    GM --> GN[tr.appendChild(th)]
     GN --> GO[th = doc.createElement("th")]
    GO --> GP[th.textContent = "Value"]
    GP --> GQ[tr.appendChild(th)]
    GQ --> GR[th = doc.createElement("th")]
      GR --> GS[th.textContent = "Focus"]
      GS --> GT[tr.appendChild(th)]
       GT --> GU[return tr]
      GU --> GV[fu.createDetailRow(index, detail, opts)]
     GV --> GW[tr = doc.createElement("tr")]
     GW --> GX[td = doc.createElement("td")]
     GX --> GY[td.textContent = index]
       GY --> GZ[tr.appendChild(td)]