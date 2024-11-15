## \file hypotez/src/webdriver/chrome/extentions/openai/background.js
# -*- coding: utf-8 -*-

""" module: src.webdriver.chrome.extentions.openai """
MODE = 'debug'
chrome.runtime.onInstalled.addListener(() => {
    console.log('OpenAI Model Interface Extension Installed');
});
