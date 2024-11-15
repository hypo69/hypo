## \file hypotez/src/bots/openai_bots/chatgpt-telegram/src/utils.js
# -*- coding: utf-8 -*-

""" module: src.bots.openai_bots.chatgpt-telegram.src """
MODE = 'debug'
import { unlink } from 'fs/promises'
export async function removeFile(path) {
    try {
        await unlink(path)
    } catch (e) {
        console.log('Error while removing file', e.message)
    }
}