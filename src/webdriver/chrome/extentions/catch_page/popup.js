## \file hypotez/src/webdriver/chrome/extentions/catch_page/popup.js
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver.chrome.extentions.catch_page """
MODE = 'debug'
document.getElementById("sendUrlButton").addEventListener("click", () => {
    alert("Hello, world!");
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        let activeTab = tabs[0];
        let activeTabUrl = activeTab.url;
        
        chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => {
            if (response.status === "success") {
                alert("URL sent successfully!");
            } else {
                alert("Failed to send URL.");
            }
        });
    });
});
