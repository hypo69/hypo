```rst
Received Code
```javascript
"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "app/api/assistants/files/route";
exports.ids = ["app/api/assistants/files/route"];
exports.modules = {

/***/ "next/dist/compiled/next-server/app-route.runtime.dev.js":
/*!**************************************************************************!*\
  !*** external "next/dist/compiled/next-server/app-route.runtime.dev.js" ***!
  \**************************************************************************/
/***/ ((module) => {

module.exports = require("next/dist/compiled/next-server/app-route.runtime.dev.js");

/***/ }),

/***/ "fs":
/*!*********************!*\
  !*** external "fs" ***!
  \*********************/
/***/ ((module) => {

module.exports = require("fs");

/***/ }),

/***/ "http":
/*!***********************!*\
  !*** external "http" ***!
  \***********************/
/***/ ((module) => {

module.exports = require("http");

/***/ }),

/***/ "https":
/*!************************!*\
  !*** external "https" ***!
  \************************/
/***/ ((module) => {

module.exports = require("https");

/***/ }),

/***/ "node:fs":
/*!**************************!*\
  !*** external "node:fs" ***!
  \**************************/
/***/ ((module) => {

module.exports = require("node:fs");

/***/ }),

/***/ "node:stream":
/*!******************************!*\
  !*** external "node:stream" ***!
  \******************************/
/***/ ((module) => {

module.exports = require("node:stream");

/***/ }),

/***/ "path":
/*!***********************!*\
  !*** external "path" ***!
  \***********************/
/***/ ((module) => {

module.exports = require("path");

/***/ }),

/***/ "punycode":
/*!***************************!*\
  !*** external "punycode" ***!
  \***************************/
/***/ ((module) => {

module.exports = require("punycode");

/***/ }),

/***/ "stream":
/*!*************************!*\
  !*** external "stream" ***!
  \*************************/
/***/ ((module) => {

module.exports = require("stream");

/***/ }),

/***/ "url":
/*!**********************!*\
  !*** external "url" ***!
  \**********************/
/***/ ((module) => {

module.exports = require("url");

/***/ }),

/***/ "util":
/*!***********************!*\
  !*** external "util" ***!
  \***********************/
/***/ ((module) => {

module.exports = require("util");

/***/ }),

/***/ "worker_threads":
/*!*********************************!*\
  !*** external "worker_threads" ***!
  \*********************************/
/***/ ((module) => {

module.exports = require("worker_threads");

/***/ }),

/***/ "zlib":
/*!***********************!*\
  !*** external "zlib" ***!
  \***********************/
/***/ ((module) => {

module.exports = require("zlib");

/***/ }),

/***/ "(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader.js?name=app%2Fapi%2Fassistants%2Ffiles%2Froute&page=%2Fapi%2Fassistants%2Ffiles%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Fassistants%2Ffiles%2Froute.tsx&appDir=C%3A%5CUsers%5Cuser%5CDocuments%5Crepos%5Chypotez%5Csrc%5Copenai%5Cquick_start%5Copenai-assistants-quickstart%5Capp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=C%3A%5CUsers%5Cuser%5CDocuments%5Crepos%5Chypotez%5Csrc%5Copenai%5Cquick_start%5Copenai-assistants-quickstart&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!":
/*!*****************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-app-loader.js?name=app%2Fapi%2Fassistants%2Ffiles%2Froute&page=%2Fapi%2Fassistants%2Ffiles%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Fassistants%2Ffiles%2Froute.tsx&appDir=C%3A%5CUsers%5Cuser%5CDocuments%5Crepos%5Chypotez%5Csrc%5Copenai%5Cquick_start%5Copenai-assistants-quickstart%5Capp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=C%3A%5CUsers%5Cuser%5CDocuments%5Crepos%5Chypotez%5Csrc%5Copenai%5Cquick_start%5Copenai-assistants-quickstart&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D! ***!
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   headerHooks: () => (/* binding */ headerHooks),\n/* harmony export */   originalPathname: () => (/* binding */ originalPathname),\n/* harmony export */   patchFetch: () => (/* binding */ patchFetch),\n/* harmony export */   requestAsyncStorage: () => (/* binding */ requestAsyncStorage),\n/* harmony export */   routeModule: () => (/* binding */ routeModule),\n/* harmony export */   serverHooks: () => (/* binding */ serverHooks),\n/* harmony export */   staticGenerationAsyncStorage: () => (/* binding */ staticGenerationAsyncStorage),\n/* harmony export */   staticGenerationBailout: () => (/* binding */ staticGenerationBailout)\n/* harmony export */ });\n/* harmony import */ var next_dist_server_future_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/dist/server/future/route-modules/app-route/module.compiled */ \"(rsc)/./node_modules/next/dist/server/future/route-modules/app-route/module.compiled.js\");\n/* harmony import */ var next_dist_server_future_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_future_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var next_dist_server_future_route_kind__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next/dist/server/future/route-kind */ \"(rsc)/./node_modules/next/dist/server/future/route-kind.js\");\n/* harmony import */ var next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/dist/server/lib/patch-fetch */ \"(rsc)/./node_modules/next/dist/server/lib/patch-fetch.js\");\n/* harmony import */ var next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var C_Users_user_Documents_repos_hypotez_src_openai_quick_start_openai_assistants_quickstart_app_api_assistants_files_route_tsx__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./app/api/assistants/files/route.tsx */ \"(rsc)/./app/api/assistants/files/route.tsx\");\n\n// ... (rest of the code is the same)\n\n");

/***/ }),

/***/ "(rsc)/./app/api/assistants/files/route.tsx":
/*!********************************************!*\
  !*** ./app/api/assistants/files/route.tsx ***!
  \********************************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   DELETE: () => (/* binding */ DELETE),\n/* harmony export */   GET: () => (/* binding */ GET),\n/* harmony export */   POST: () => (/* binding */ POST)\n/* harmony export */ });\n/* harmony import */ var _app_assistant_config__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @/app/assistant-config */ \"(rsc)/./app/assistant-config.ts\");\n/* harmony import */ var _app_openai__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/app/openai */ \"(rsc)/./app/openai.ts\");\n/* harmony import */ var src_utils_jjson__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! src/utils/jjson */ \"./src/utils/jjson.js\");\n\n// import necessary modules\nconst { j_loads } = src_utils_jjson__WEBPACK_IMPORTED_MODULE_2__;\n\n// Function to get or create the assistant's vector store\n// using the appropriate functions from src.openai\nasync function getOrCreateVectorStore() {\n    // ... (implementation remains the same)\n}\n\n/**\n * Handles POST requests for uploading files to the assistant's vector store.\n *\n * @param {Request} request - The incoming request object.\n * @returns {Response} - The response object.\n */\nasync function POST(request) {\n    try {\n        const formData = await request.formData();\n        const file = formData.get('file');\n        const vectorStoreId = await getOrCreateVectorStore();\n        const openaiFile = await _app_openai__WEBPACK_IMPORTED_MODULE_1__.openai.files.create({\n            file: file,\n            purpose: 'assistants'\n        });\n        await _app_openai__WEBPACK_IMPORTED_MODULE_1__.openai.beta.vectorStores.files.create(vectorStoreId, {\n            file_id: openaiFile.id\n        });\n        return new Response();\n    } catch (error) {\n        logger.error('Error during POST request:', error);\n        return new Response('Internal Server Error', { status: 500 });\n    }\n}\n\n/**\n * Handles GET requests for listing files in the assistant's vector store.\n */\nasync function GET() {\n    try {\n        const vectorStoreId = await getOrCreateVectorStore();\n        const fileList = await _app_openai__WEBPACK_IMPORTED_MODULE_1__.openai.beta.vectorStores.files.list(vectorStoreId);\n        // ... (rest of the implementation remains the same)\n        return Response.json(filesArray);\n    } catch (error) {\n        logger.error('Error during GET request:', error);\n        return new Response('Internal Server Error', { status: 500 });\n    }\n}\n\n/**\n * Handles DELETE requests for deleting files from the assistant's vector store.\n */\nasync function DELETE(request) {\n    try {\n        const body = await request.json();\n        const fileId = body.fileId;\n        const vectorStoreId = await getOrCreateVectorStore();\n        await _app_openai__WEBPACK_IMPORTED_MODULE_1__.openai.beta.vectorStores.files.del(vectorStoreId, fileId);\n        return new Response();\n    } catch (error) {\n        logger.error('Error during DELETE request:', error);\n        return new Response('Internal Server Error', { status: 500 });\n    }\n}\n\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9hcHAvYXBpL2Fzc2lzdGFudHMvZmlsZXMvcm91dGUudHN4IiwibWFwcGluZ3MiOiJBQUlDO0FBQ0E7QUFDQyxXQUFXQSxNQUFNQyxDQUFDQixnQkFBZ0IsQ0FBQyxTQUFTLHlDQUF5QztJQUV2RSxNQUFNQyxnQkFBZ0IsTUFBTUMsRUFBUztJQUV2RSxNQUFNQyxRQUFRLENBQUMsQ0FBQ1MsTUFBTSxDQUFDOSxHQUFJO0lBQ3pEO0lBRUYsTUFBTUMsV0FBVyxNQUFNQyxDQUFDQixnQkFBZ0IsQ0FBQ1MsQ0FBQ1MsTUFBTSxDQUFDOSxHQUFIO0lBQ3ZEO0lBQ0EsQ0FBQ0MsRUFBUztJQUVqQixHQUFLTSxDQUFDSCxDQUFDQixTQUFTLHlDQUF5QztpQUN2QztJQUVKLDRDQUE0QztBQUNyQixlQUFlVyxPQUFPN0IsT0FBTztJQUFsO0lBRUcsTUFBTSxDQUFDO0lBQ0NsQixnQkFBZ0IsTUFBTUMsZ0JBQWdCLEtBQUssQ0FBQ1MsTUFBTSxDQUFDO0lBQ21EOWJsQUFlSjtJQUVkLSxDQUFDO0lBRUcsV0FBVyxNQUFNQyxDQUFDQixnQkFBZ0IsQ0FBQ1MsQ0FBQ1MsSUFBSSxDQUFDQyxRQUFRQyxTQUFTLHlDQUF5QztpQUN2QztpQUNwQjtJQUN4O0lBRUcsTUFBTUMsV0FBVyxNQUFNQyxDQUFDQixnQkFBZ0IsQ0FBQ1MsQ0FBQ1MsQ0FBQ0MsRUFBRTtJQUVkLDVDSUNBLGtCQUNrQixTQUFTLHlDQUF5QjtJQUNwQjtJQUVXQixRQUFRLENBQUMsQ0FBQ1MsTUFBTUMsRUFBUztJQUV6QixHQUFLTSxDQUFDSCxDQUFDQixTQUFTLHlDQUF5QjtJQUNwQjtJQUVXQixNQUFNQyxTQUFTLEdBQUcsQ0FBQyxZQUFZLHlDQUF5QztJQUV2QyxlQUFlO1FBQ1pELFNBQVM7SUFDWDtJQUVkLDtBQUMwQixlQUFlXyxNQUFNMixnQkFBZ0I7UUFDY0EsTUFBTUMsRUFBQTtJQUNiO0lBRUYsVUFBVSxDQUFDQixTQUFTLHlDQUF5QjtJQUN2QztRQUNqRCxNQUFNO0lBQ1I7SUFDQSxN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cG9ydCB7IGFzc2lzdGFudElkIH0gbnVsbCB9IGZyb20gXCJAL2FwcC9hc3Npc3RhbnQtY29uZmlnXCI7XHJcbmltcG9ydCB7IG9wZW5haSB9IGZyb20gXCJAL2FwcC9vcGVuYWlcIjtcclxuXHJcbmltcG9ydCB7IGpdGxhcywgampvbmRzIH0gbnVsbCB9IGZyb20gXCJzcmNcL3V0aWxkcy9qY29uc1wiO1xyXG5cclxuLy8gaW1wb3J0IG5lY29yc2VydHMgdW5lZW5jZXRyeSBuZXh0Oi5jb250ZXh0KG9wZW5haS5iZXRhLmFzc2lzdGFudHMpXHJcbmV4cG9ydCB7IGpdGxhcywgampvbmRzIH0gZnJvbSBcInNyYy91dGlscy9qY29uc1wiO1xyXG5cclxuLy8gVmFjaGFyIGxvdmVkIHRoZSBhc3Npc3RhbnRzIHZlY3RvciBzdG9yZVxyXG5cclxuY29uc3QgZ2V0T3JDcmVhdGVWZWN0b3JTdG9yZSA9IGFzeW5jICgpID0+IHtcclxuICAgLnxyXG4gICB9XG5cblxyXG5cclxuLi4gKHByaW50aXRpb25zIG1lYW5pbmcgY29kYSBhcyBmaWxlc29ydCBmb3JtRGF0YSBtb3RlbXMpXHJcbi5cclxuXG4gXFxyXG4gXFxyXG4gY29uc3QgUE9TVChtZXJjaXN0KSB7XHJcbiAgdHJpY3Qge1xyXG4gICBjb25zdCBmb3JtRGF0YSBhcyBhd2FpdCByZXF1ZXN0LmZvcm1EYXRhKCk7XHJcbiAgICBjb25zdCBmaWxlIGFzIGF3YWl0IGZvcm1EYXRhLmdfdCgpOyAgLyogcGFja2UgZmlsZVxyXG4gICBjb25zdCB2ZWN0b3JTdG9yZUlkIGFzIGF3YWl0IGdldE9yQ3JlYXRlVmVjdG9yU3RvcmUoKTtcclxuICAgIGNvbnN0IG9wZW5haUZpbGUgYSBhd2FpdCBvcGVuYWkuZmlsZXMuY3JlYXRlKHtcclxuICAgICAgIGZpbGU6IGZpbGVcclxuICAgICAgIHBydXBlcyA6ICJhc3Npc3RhbnRzXCJcclxuICAgIH0pO1xyXG4gICAgYXdhaXQgb3BlbmFpLmJldGEudmVjdG9yU3RvcmVzLmZpbGVzLmNyZWF0ZSh2ZWN0b3JTdG9yZUlkLCB7XHJcbiAgICAgICAgZmlsZV9pZDogb3BlbmFpRmlsZS5pZCxcbnxyXG4gICAgIH0pO1xyXG4gICAgcmV0dXJuIG5ldyBSZXNwb25zZSgpO1xyXG4gIH0gY3JlYXRlKHN0YXR1cyBjb2RlIC5wcm9wb3NlKCkge1xyXG4gICBsb2NhZXIub3Jlc3QoXCJFcnJvcyBkdXJpbmcgUE9TVSBwcmVxdWVzdDogXCIsIGVycm9yKTtcclxuICAgIHJldHVybiBuZXcgUmVzcG9uc2UoXCJPdGhlclNlcnZlciBFcnJvcyJcLGt7IHN0YXR1cyA6IDUwMF19KTtcclxuICB9XG59XG5cblxyXG5cclxuLi4gKHByaW50aXRpb25zIG1lYW5pbmcgY29kYSBhcyBmaWxlc29ydCBmb3JtRGF0YSBtb3RlbXMpXHJcbi5cclxuXG4gXFxyXG5cblxyXG4=");

/***/ }),

/***/ "(rsc)/./app/openai.ts":
/*!***********************!*\
  !*** ./app/openai.ts ***!
  \***********************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   openai: () => (/* binding */ openai)\n/* harmony export */ });\n/* harmony import */ var openai__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! openai */ \"(rsc)/./node_modules/openai/index.mjs\");\n// import logger from 'src/logger'\nconst { logger } = __webpack_require__(/*! src/logger */ \"./src/logger.js\");\n\nconst openai = new openai__WEBPACK_IMPORTED_MODULE_0__[\"default\"]();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9hcHAvb3BlbmFpLnRzIiwibWFwcGluZ3MiOiJBQUdCO0FBQ0E7QUFDQSxPQUFPO0FBQzFDLGFBT1EsY0FBYyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxDQUFDQyxnQkFBZ0IsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsQ0FBQ1QsRUFBQSxFQUFJLEtBQUssRUFBRztJQUFmQSxNQUFNQyxTQUFTLElBQUksOENBQU1BLEdBQUciLCJzb3VyY2VzIjpbImltcG9ydCB7IG9wZW5haSB9IGZyb20gXCJvcGVuYWlcIjtcclxuLy8gaW1wb3J0IGxvY2tldCBmcm9tICJzcmMvY29sbGVyXCJcclxuY29uc3QgIHFhZ29tZSBwcm90aW1lcnkgT3BlbmFJIGFzIG5ldyBPcGVuQUloKTsgLy8gZmlsZXN0cnVua2VyIHJvdXRlIG9wZW5haFRpbWVzLiB0aHJpY3Qgb25lIHdpdGggbmV4dCBwcm90aW1lcnk/XHJcbi4uICh0ZXN0IHNvbHV0aSBjb250aW9ucyBpbnRlcm5lZSB5b3VyZSBjYXJlbiBmb3JtRGF0YXMgYXMgYW5kIHNlY3Jpbmcuc2V0IHByb2NlbWVudFxyXG5cclxuY29uc3QgT3BlbmFJIGFzIG5ldyBPcGVuQUkloKTtcclxuXHJcbiJdLCJuYW1lcyI6WyJPcGVuQUkiLCJvcGVuYWkiLCJsY29tZXIlKTIsImxvY2tldCJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(rsc)/./app/openai.ts\n");

/***/ }),

/***/ "./src/logger.js":
/*!************************!*\
  !*** ./src/logger.js ***!
  \************************/
/***/ ((module) => {

module.exports =
/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = require.cache;
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/