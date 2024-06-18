#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
# import tkinter as tk
# from tkinter import filedialog
import wx

class J2U:
    chsPMNames = [bytearray(b'\x19\x47\x0A\x63\x11\xB6\x0F\xD6\x50\x50'), bytearray(b'\x19\x47\x0A\x63\x11\xB6\x0F\xD6\x50\x50'), bytearray(b'\x06\xD2\x0F\xD6\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0B\x9E\x50\x50\x50\x50'), bytearray(b'\x0D\xE8\x0D\xE8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\x08\x0E\xD6\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\xDF\x2D\xE4\x07\x23\x0E\xB2\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x06\xCA\x0B\x27\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x0C\xFA\x11\x10\x05\xD9\x50\x50\x50\x50'), bytearray(b'\x12\xEE\x06\xE4\x0F\xEF\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0F\x7A\x10\xE7\x50\x50\x50\x50'), bytearray(b'\x06\xE4\x06\xE4\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x6C\x0D\x68\x50\x50\x50\x50\x50\x50'), bytearray(b'\x08\x8A\x08\xD5\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0B\x90\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x09\x42\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x0B\x81\x0B\x04\x0B\x81\x50\x50'), bytearray(b'\x07\x70\x0A\x63\x11\xB6\x0D\x89\x50\x50'), bytearray(b'\x0B\x81\x0E\x20\x0B\x81\x10\x13\x50\x50'), bytearray(b'\x07\xF5\x10\x37\x08\x9F\x50\x50\x50\x50'), bytearray(b'\x0C\xDA\x09\x85\x50\x50\x50\x50\x50\x50'), bytearray(b'\x05\x31\x0B\xC4\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0F\x7A\x05\x3C\x50\x50\x50\x50'), bytearray(b'\x0C\x98\x28\x0F\x10\x08\x0D\x2A\x50\x50'), bytearray(b'\x08\xD5\x10\x13\x50\x50\x50\x50\x50\x50'), bytearray(b'\x07\xD7\x10\xBE\x2C\xAF\x2C\x91\x50\x50'), bytearray(b'\x08\xE9\x12\x37\x12\x37\x50\x50\x50\x50'), bytearray(b'\x10\x08\x0A\x25\x08\xD2\x50\x50\x50\x50'), bytearray(b'\x0B\x09\x0C\x8C\x10\x13\x50\x50\x50\x50'), bytearray(b'\x0C\xA9\x10\xAB\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x07\x11\x08\x9F\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x12\xB6\x0F\x79\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x19\x49\x0E\xD6\x50\x50\x50\x50'), bytearray(b'\x05\xA4\x05\xA4\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\xCA\x06\xCA\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x13\x80\x09\xBB\x0B\x81\x50\x50\x50\x50'), bytearray(b'\x0C\x39\x0C\x39\x0F\xA7\x50\x50\x50\x50'), bytearray(b'\x09\xCA\x0B\xCF\x06\xE4\x50\x50\x50\x50'), bytearray(b'\x09\x0A\x0B\xD8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x18\x0E\x7D\x0E\xE9\x0D\xA2\x50\x50'), bytearray(b'\x07\xD7\x10\xF8\x0B\x9D\x50\x50\x50\x50'), bytearray(b'\x0B\x62\x0E\xCB\x0B\x9D\x50\x50\x50\x50'), bytearray(b'\x04\xC4\x04\xFA\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x0D\xAF\x0B\x81\x10\x13\x10\xAA\x50\x50'), bytearray(b'\x0B\x29\x06\xC5\x12\xA0\x50\x50\x50\x50'), bytearray(b'\x06\xB5\x0C\xEB\x2D\xD6\x50\x50\x50\x50'), bytearray(b'\x0C\x39\x0C\x39\x12\xB6\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\xA0\x19\x49\x09\xB2\x0F\xD6\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x07\x23\x09\xB9\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x0F\x23\x09\x1C\x13\x01\x06\x9B\x08\xBE'), bytearray(b'\x11\x13\x10\x13\x06\xE3\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x09\x3D\x08\xBE\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x08\xE9\x0F\xA0\x50\x50\x50\x50'), bytearray(b'\x07\x10\x0F\xEB\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x2F\x10\x7B\x0C\x8C\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x06\xA6\x12\xA0\x50\x50\x50\x50'), bytearray(b'\x0C\xB7\x0E\xB2\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x62\x0C\x34\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x1C\xD7\x1C\xD7\x50\x50\x50\x50\x50\x50'), bytearray(b'\x11\x6F\x11\xED\x2C\x98\x2C\x63\x50\x50'), bytearray(b'\x0C\xE0\x06\x93\x0A\x7F\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x12\xCA\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x09\xD1\x07\x63\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x0F\x46\x07\x23\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x04\xFB\x05\x82\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x1C\xB3\x1C\xB3\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0E\x6F\x12\x27\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\x33\x11\x49\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0A\xBF\x11\x49\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\xE8\x0B\x04\x0E\xB0\x50\x50\x50\x50'), bytearray(b'\x0B\xAB\x0E\xB0\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\xE0\x0D\x6B\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x08\xE6\x0B\x2B\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x09\x71\x0F\xA7\x0B\x6E\x50\x50\x50\x50'), bytearray(b'\x0B\xDF\x06\xEA\x0B\x6E\x50\x50\x50\x50'), bytearray(b'\x0D\x1C\x08\xE9\x0C\x9B\x50\x50\x50\x50'), bytearray(b'\x08\xE9\x06\xA2\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x7F\x0F\x42\x0F\xEB\x50\x50\x50\x50'), bytearray(b'\x06\x7F\x0F\x42\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x0A\xCF\x0F\xA7\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x07\x90\x06\xA2\x0A\xCF\x0F\xA7\x0F\xD6'), bytearray(b'\x0D\xBC\x07\x3B\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\xBC\x0B\x29\x07\x3B\x50\x50\x50\x50'), bytearray(b'\x13\x07\x05\xB8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x13\x07\x05\xB8\x50\x50\x50\x50'), bytearray(b'\x0B\xAB\x13\x07\x05\xB8\x50\x50\x50\x50'), bytearray(b'\x10\x08\x13\x07\x05\xB8\x50\x50\x50\x50'), bytearray(b'\x11\x2B\x0B\xD8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x0A\x13\x3E\x2C\x96\x50\x50\x50\x50'), bytearray(b'\x04\xC4\x04\xFA\x0F\x79\x50\x50\x50\x50'), bytearray(b'\x0D\xAF\x0B\x81\x10\x13\x50\x50\x50\x50'), bytearray(b'\x11\x6F\x11\xED\x0A\xF7\x50\x50\x50\x50'), bytearray(b'\x11\x6F\x11\xED\x13\x7C\x0F\xB7\x50\x50'), bytearray(b'\x07\x70\x0A\x63\x06\x49\x50\x50\x50\x50'), bytearray(b'\x10\xCC\x0B\x27\x13\x7A\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x18\x83\x07\xF2\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x1C\xD7\x1C\xD7\x0B\xCF\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x05\x31\x09\x3D\x50\x50\x50\x50'), bytearray(b'\x0F\x23\x07\x10\x0F\xEB\x50\x50\x50\x50'), bytearray(b'\x0D\x17\x0C\x61\x07\x9A\x50\x50\x50\x50'), bytearray(b'\x04\xF9\x08\xE9\x0F\xA0\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\x7A\x0C\xB7\x06\x49\x50\x50\x50\x50'), bytearray(b'\x10\xCC\x09\xF7\x13\x7A\x50\x50\x50\x50'), bytearray(b'\x04\xEF\x06\xC9\x07\x37\x50\x50\x50\x50'), bytearray(b'\x08\xBE\x0B\xD8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x08\x71\x06\xC5\x12\xA0\x50\x50\x50\x50'), bytearray(b'\x13\x48\x0C\xDA\x2D\xD6\x0E\xE9\x50\x50'), bytearray(b'\x06\xC9\x19\x49\x2C\x96\x50\x50\x50\x50'), bytearray(b'\x06\x0A\x0C\xDA\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x05\x66\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x0B\xC4\x13\xA1\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x6C\x06\x6C\x0D\x68\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0A\xD8\x0E\x6F\x12\x27\x50\x50\x50\x50'), bytearray(b'\x06\xA2\x09\xF7\x05\x3C\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x11\x1E\x0D\xE8\x0B\xAB\x06\xE3\x50\x50'), bytearray(b'\x0D\xE8\x0B\x29\x11\xA3\x50\x50\x50\x50'), bytearray(b'\x10\x05\x06\xE3\x11\x13\x10\x13\x50\x50'), bytearray(b'\x0C\xB4\x0B\xA3\x06\xC9\x50\x50\x50\x50'), bytearray(b'\x08\x36\x0B\x86\x08\x36\x0B\x86\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x08\xD5\x10\x13\x10\xD8\x50\x50\x50\x50'), bytearray(b'\x0B\x09\x11\xA3\x50\x50\x50\x50\x50\x50'), bytearray(b'\x09\x49\x07\x10\x50\x50\x50\x50\x50\x50'), bytearray(b'\x05\x66\x05\x66\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x05\x66\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x05\x2E\x0F\xA7\x08\xE9\x12\x37\x50\x50'), bytearray(b'\x0C\xFA\x11\x10\x18\xCC\x19\x2F\x50\x50'), bytearray(b'\x0C\xFA\x11\x10\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x07\x6E\x06\xA2\x10\x08\x0D\x2A\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0A\x63\x0A\x8C\x13\xA1\x50\x50\x50\x50'), bytearray(b'\x0A\x8C\x13\xA1\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x09\xB2\x0C\x9B\x50\x50\x50\x50'), bytearray(b'\x0C\x08\x12\xCA\x0C\x9B\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x0B\x81\x06\xC5\x50\x50\x50\x50'), bytearray(b'\x0B\x81\x06\xC5\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0B\xD8\x0D\x9B\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0D\x3A\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x0E\xCB\x0F\xA7\x50\x50\x50\x50'), bytearray(b'\x07\x90\x05\x7D\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x09\x71\x0F\xA7\x13\x37\x0C\x34\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x06\x9B\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x09\xB2\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0A\x78\x0D\x69\x08\xD2\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x0B\x36\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x1C\xA0\x08\xD2\x50\x50\x50\x50'), bytearray(b'\x0D\xCD\x09\xB2\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x19\x3B\x0C\x65\x05\xD9\x50\x50\x50\x50'), bytearray(b'\x06\x6C\x06\x6C\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x04\xF6\x11\x2D\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x0B\x82\x04\xEA\x12\xA3\x50\x50\x50\x50'), bytearray(b'\x0B\x3A\x06\xCA\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0F\xAB\x09\x6A\x50\x50\x50\x50')]
    engPMNames = [bytearray(b'\x91\x87\x98\x83\x8E\x8D\x50\x50\x50\x50'), bytearray(b'\x91\x87\x98\x83\x8E\x8D\x50\x50\x50\x50'), bytearray(b'\x8A\x80\x8D\x86\x80\x92\x8A\x87\x80\x8D'), bytearray(b'\x8D\x88\x83\x8E\x91\x80\x8D\xEF\x50\x50'), bytearray(b'\x82\x8B\x84\x85\x80\x88\x91\x98\x50\x50'), bytearray(b'\x92\x8F\x84\x80\x91\x8E\x96\x50\x50\x50'), bytearray(b'\x95\x8E\x8B\x93\x8E\x91\x81\x50\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x8A\x88\x8D\x86\x50\x50'), bytearray(b'\x92\x8B\x8E\x96\x81\x91\x8E\x50\x50\x50'), bytearray(b'\x88\x95\x98\x92\x80\x94\x91\x50\x50\x50'), bytearray(b'\x84\x97\x84\x86\x86\x94\x93\x8E\x91\x50'), bytearray(b'\x8B\x88\x82\x8A\x88\x93\x94\x8D\x86\x50'), bytearray(b'\x84\x97\x84\x86\x86\x82\x94\x93\x84\x50'), bytearray(b'\x86\x91\x88\x8C\x84\x91\x50\x50\x50\x50'), bytearray(b'\x86\x84\x8D\x86\x80\x91\x50\x50\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x91\x80\x8D\xF5\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x90\x94\x84\x84\x8D\x50'), bytearray(b'\x82\x94\x81\x8E\x8D\x84\x50\x50\x50\x50'), bytearray(b'\x91\x87\x98\x87\x8E\x91\x8D\x50\x50\x50'), bytearray(b'\x8B\x80\x8F\x91\x80\x92\x50\x50\x50\x50'), bytearray(b'\x80\x91\x82\x80\x8D\x88\x8D\x84\x50\x50'), bytearray(b'\x8C\x84\x96\x50\x50\x50\x50\x50\x50\x50'), bytearray(b'\x86\x98\x80\x91\x80\x83\x8E\x92\x50\x50'), bytearray(b'\x92\x87\x84\x8B\x8B\x83\x84\x91\x50\x50'), bytearray(b'\x93\x84\x8D\x93\x80\x82\x8E\x8E\x8B\x50'), bytearray(b'\x86\x80\x92\x93\x8B\x98\x50\x50\x50\x50'), bytearray(b'\x92\x82\x98\x93\x87\x84\x91\x50\x50\x50'), bytearray(b'\x92\x93\x80\x91\x98\x94\x50\x50\x50\x50'), bytearray(b'\x81\x8B\x80\x92\x93\x8E\x88\x92\x84\x50'), bytearray(b'\x8F\x88\x8D\x92\x88\x91\x50\x50\x50\x50'), bytearray(b'\x93\x80\x8D\x86\x84\x8B\x80\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x86\x91\x8E\x96\x8B\x88\x93\x87\x84\x50'), bytearray(b'\x8E\x8D\x88\x97\x50\x50\x50\x50\x50\x50'), bytearray(b'\x85\x84\x80\x91\x8E\x96\x50\x50\x50\x50'), bytearray(b'\x8F\x88\x83\x86\x84\x98\x50\x50\x50\x50'), bytearray(b'\x92\x8B\x8E\x96\x8F\x8E\x8A\x84\x50\x50'), bytearray(b'\x8A\x80\x83\x80\x81\x91\x80\x50\x50\x50'), bytearray(b'\x86\x91\x80\x95\x84\x8B\x84\x91\x50\x50'), bytearray(b'\x82\x87\x80\x8D\x92\x84\x98\x50\x50\x50'), bytearray(b'\x8C\x80\x82\x87\x8E\x8A\x84\x50\x50\x50'), bytearray(b'\x8C\x91\xE8\x8C\x88\x8C\x84\x50\x50\x50'), bytearray(b'\x87\x88\x93\x8C\x8E\x8D\x8B\x84\x84\x50'), bytearray(b'\x87\x88\x93\x8C\x8E\x8D\x82\x87\x80\x8D'), bytearray(b'\x80\x91\x81\x8E\x8A\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x80\x91\x80\x92\x84\x82\x93\x50\x50'), bytearray(b'\x8F\x92\x98\x83\x94\x82\x8A\x50\x50\x50'), bytearray(b'\x83\x91\x8E\x96\x99\x84\x84\x50\x50\x50'), bytearray(b'\x86\x8E\x8B\x84\x8C\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x80\x86\x8C\x80\x91\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x84\x8B\x84\x82\x93\x80\x81\x94\x99\x99'), bytearray(b'\x8C\x80\x86\x8D\x84\x93\x8E\x8D\x50\x50'), bytearray(b'\x8A\x8E\x85\x85\x88\x8D\x86\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x80\x8D\x8A\x84\x98\x50\x50\x50\x50'), bytearray(b'\x92\x84\x84\x8B\x50\x50\x50\x50\x50\x50'), bytearray(b'\x83\x88\x86\x8B\x84\x93\x93\x50\x50\x50'), bytearray(b'\x93\x80\x94\x91\x8E\x92\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x85\x80\x91\x85\x84\x93\x82\x87\xbb\x50'), bytearray(b'\x95\x84\x8D\x8E\x8D\x80\x93\x50\x50\x50'), bytearray(b'\x83\x91\x80\x86\x8E\x8D\x88\x93\x84\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x83\x8E\x83\x94\x8E\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x8E\x8B\x88\x96\x80\x86\x50\x50\x50'), bytearray(b'\x89\x98\x8D\x97\x50\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x8E\x8B\x93\x91\x84\x92\x50\x50\x50'), bytearray(b'\x80\x91\x93\x88\x82\x94\x8D\x8E\x50\x50'), bytearray(b'\x99\x80\x8F\x83\x8E\x92\x50\x50\x50\x50'), bytearray(b'\x83\x88\x93\x93\x8E\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x84\x8E\x96\x93\x87\x50\x50\x50\x50'), bytearray(b'\x8A\x91\x80\x81\x81\x98\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x95\x94\x8B\x8F\x88\x97\x50\x50\x50\x50'), bytearray(b'\x8D\x88\x8D\x84\x93\x80\x8B\x84\x92\x50'), bytearray(b'\x8F\x88\x8A\x80\x82\x87\x94\x50\x50\x50'), bytearray(b'\x91\x80\x88\x82\x87\x94\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x83\x91\x80\x93\x88\x8D\x88\x50\x50\x50'), bytearray(b'\x83\x91\x80\x86\x8E\x8D\x80\x88\x91\x50'), bytearray(b'\x8A\x80\x81\x94\x93\x8E\x50\x50\x50\x50'), bytearray(b'\x8A\x80\x81\x94\x93\x8E\x8F\x92\x50\x50'), bytearray(b'\x87\x8E\x91\x92\x84\x80\x50\x50\x50\x50'), bytearray(b'\x92\x84\x80\x83\x91\x80\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x92\x80\x8D\x83\x92\x87\x91\x84\x96\x50'), bytearray(b'\x92\x80\x8D\x83\x92\x8B\x80\x92\x87\x50'), bytearray(b'\x8E\x8C\x80\x8D\x98\x93\x84\x50\x50\x50'), bytearray(b'\x8E\x8C\x80\x92\x93\x80\x91\x50\x50\x50'), bytearray(b'\x89\x88\x86\x86\x8B\x98\x8F\x94\x85\x85'), bytearray(b'\x96\x88\x86\x86\x8B\x98\x93\x94\x85\x85'), bytearray(b'\x84\x84\x95\x84\x84\x50\x50\x50\x50\x50'), bytearray(b'\x85\x8B\x80\x91\x84\x8E\x8D\x50\x50\x50'), bytearray(b'\x89\x8E\x8B\x93\x84\x8E\x8D\x50\x50\x50'), bytearray(b'\x95\x80\x8F\x8E\x91\x84\x8E\x8D\x50\x50'), bytearray(b'\x8C\x80\x82\x87\x8E\x8F\x50\x50\x50\x50'), bytearray(b'\x99\x94\x81\x80\x93\x50\x50\x50\x50\x50'), bytearray(b'\x84\x8A\x80\x8D\x92\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x80\x91\x80\x92\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x8E\x8B\x88\x96\x87\x88\x91\x8B\x50'), bytearray(b'\x8F\x8E\x8B\x88\x96\x91\x80\x93\x87\x50'), bytearray(b'\x96\x84\x84\x83\x8B\x84\x50\x50\x50\x50'), bytearray(b'\x8A\x80\x8A\x94\x8D\x80\x50\x50\x50\x50'), bytearray(b'\x81\x84\x84\x83\x91\x88\x8B\x8B\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x83\x8E\x83\x91\x88\x8E\x50\x50\x50\x50'), bytearray(b'\x8F\x91\x88\x8C\x84\x80\x8F\x84\x50\x50'), bytearray(b'\x83\x94\x86\x93\x91\x88\x8E\x50\x50\x50'), bytearray(b'\x95\x84\x8D\x8E\x8C\x8E\x93\x87\x50\x50'), bytearray(b'\x83\x84\x96\x86\x8E\x8D\x86\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x82\x80\x93\x84\x91\x8F\x88\x84\x50\x50'), bytearray(b'\x8C\x84\x93\x80\x8F\x8E\x83\x50\x50\x50'), bytearray(b'\x81\x94\x93\x93\x84\x91\x85\x91\x84\x84'), bytearray(b'\x8C\x80\x82\x87\x80\x8C\x8F\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x86\x8E\x8B\x83\x94\x82\x8A\x50\x50\x50'), bytearray(b'\x87\x98\x8F\x8D\x8E\x50\x50\x50\x50\x50'), bytearray(b'\x86\x8E\x8B\x81\x80\x93\x50\x50\x50\x50'), bytearray(b'\x8C\x84\x96\x93\x96\x8E\x50\x50\x50\x50'), bytearray(b'\x92\x8D\x8E\x91\x8B\x80\x97\x50\x50\x50'), bytearray(b'\x8C\x80\x86\x88\x8A\x80\x91\x8F\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x94\x8A\x50\x50\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8A\x88\x8D\x86\x8B\x84\x91\x50\x50\x50'), bytearray(b'\x82\x8B\x8E\x98\x92\x93\x84\x91\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x84\x8B\x84\x82\x93\x91\x8E\x83\x84\x50'), bytearray(b'\x82\x8B\x84\x85\x80\x81\x8B\x84\x50\x50'), bytearray(b'\x96\x84\x84\x99\x88\x8D\x86\x50\x50\x50'), bytearray(b'\x8F\x84\x91\x92\x88\x80\x8D\x50\x50\x50'), bytearray(b'\x8C\x80\x91\x8E\x96\x80\x8A\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x87\x80\x94\x8D\x93\x84\x91\x50\x50\x50'), bytearray(b'\x80\x81\x91\x80\x50\x50\x50\x50\x50\x50'), bytearray(b'\x80\x8B\x80\x8A\x80\x99\x80\x8C\x50\x50'), bytearray(b'\x8F\x88\x83\x86\x84\x8E\x93\x93\x8E\x50'), bytearray(b'\x8F\x88\x83\x86\x84\x8E\x93\x50\x50\x50'), bytearray(b'\x92\x93\x80\x91\x8C\x88\x84\x50\x50\x50'), bytearray(b'\x81\x94\x8B\x81\x80\x92\x80\x94\x91\x50'), bytearray(b'\x95\x84\x8D\x94\x92\x80\x94\x91\x50\x50'), bytearray(b'\x93\x84\x8D\x93\x80\x82\x91\x94\x84\x8B'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x86\x8E\x8B\x83\x84\x84\x8D\x50\x50\x50'), bytearray(b'\x92\x84\x80\x8A\x88\x8D\x86\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8F\x8E\x8D\x98\x93\x80\x50\x50\x50\x50'), bytearray(b'\x91\x80\x8F\x88\x83\x80\x92\x87\x50\x50'), bytearray(b'\x91\x80\x93\x93\x80\x93\x80\x50\x50\x50'), bytearray(b'\x91\x80\x93\x88\x82\x80\x93\x84\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x91\x88\x8D\x8E\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x91\x88\x8D\x80\x50\x50'), bytearray(b'\x86\x84\x8E\x83\x94\x83\x84\x50\x50\x50'), bytearray(b'\x8F\x8E\x91\x98\x86\x8E\x8D\x50\x50\x50'), bytearray(b'\x80\x84\x91\x8E\x83\x80\x82\x93\x98\x8B'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x80\x86\x8D\x84\x8C\x88\x93\x84\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x82\x87\x80\x91\x8C\x80\x8D\x83\x84\x91'), bytearray(b'\x92\x90\x94\x88\x91\x93\x8B\x84\x50\x50'), bytearray(b'\x82\x87\x80\x91\x8C\x84\x8B\x84\x8E\x8D'), bytearray(b'\x96\x80\x91\x93\x8E\x91\x93\x8B\x84\x50'), bytearray(b'\x82\x87\x80\x91\x88\x99\x80\x91\x83\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8E\x83\x83\x88\x92\x87\x50\x50\x50\x50'), bytearray(b'\x86\x8B\x8E\x8E\x8C\x50\x50\x50\x50\x50'), bytearray(b'\x95\x88\x8B\x84\x8F\x8B\x94\x8C\x84\x50'), bytearray(b'\x81\x84\x8B\x8B\x92\x8F\x91\x8E\x94\x93'), bytearray(b'\x96\x84\x84\x8F\x88\x8D\x81\x84\x8B\x8B'), bytearray(b'\x95\x88\x82\x93\x91\x84\x84\x81\x84\x8B')]
    # root = tk.Tk()
    root = []
    # root.withdraw()

    defaultOTname = bytearray(b'\x80\x92\x87\x50\x50\x50\x50\x50\x50\x50\x50')
    defaultPMname = bytearray(b'\x86\x80\x91\x98\x50\x50\x50\x50\x50\x50\x50')

    jpnSaveArray = None
    usSaveArray = None
    extraBox = []
    outputBox = []

    class PokemonData:
        speciesID = 0
        pkmnData = bytearray(0)
        otName = bytearray(0)
        pkmnName = bytearray(0)

    def convertStr(string):
        byteList = []
        engCharmap = {"A": 0x80, "B": 0x81, "C": 0x82, "D": 0x83, "E": 0x84, "F": 0x85, "G": 0x86, "H": 0x87, "I": 0x88, "J": 0x89, "K": 0x8a, "L": 0x8b, "M": 0x8c, "N": 0x8d, "O": 0x8e, "P": 0x8f, "Q": 0x90, "R": 0x91, "S": 0x92, "T": 0x93, "U": 0x94, "V": 0x95, "W": 0x96, "X": 0x97, "Y": 0x98, "Z": 0x99, "(": 0x9a, ")": 0x9b, ":": 0x9c, ";": 0x9d, "[": 0x9e, "]": 0x9f, "a": 0xa0, "b": 0xa1, "c": 0xa2, "d": 0xa3, "e": 0xa4, "f": 0xa5, "g": 0xa6, "h": 0xa7, "i": 0xa8, "j": 0xa9, "k": 0xaa, "l": 0xab, "m": 0xac, "n": 0xad, "o": 0xae, "p": 0xaf, "q": 0xb0, "r": 0xb1, "s": 0xb2, "t": 0xb3, "u": 0xb4, "v": 0xb5, "w": 0xb6, "x": 0xb7, "y": 0xb8, "z": 0xb9, "×": 0xf1, "♀": 0xf5, "♂": 0xef, "/": 0xf3, ",": 0xf4, ".": 0xe8, "-": 0xe3 }
        if len(string) > 0 and len(string) <= 7:
            for char in string:
                if char in engCharmap:
                    byteList.append(engCharmap[char])
                else:
                    return None
        else:
            return None
        for i in range(11 - len(string)):
            byteList.append(0x50)
            
        # print(byteList)
        return bytearray(byteList)
        


    def readFileAsByteArray(file_path):
        with open(file_path, 'rb') as file:
            byte_array = file.read()
            file.close()
        return bytearray(byte_array)

    def writeValueAt(array,offset,value,count):
        for i in range(count):
            array[offset + i] = value

    def writeArrayAt(array,offset,inputArray):
        for i in range(len(inputArray)):
            char = inputArray[i]
            array[offset + i] = char

    def copyArray(jpOffset,usOffset,usDestination):
        for i in range(usDestination - usOffset):
            # print(jpnSaveArray[jpOffset + i])
            J2U.usSaveArray[usOffset + i] = J2U.jpnSaveArray[jpOffset + i]

    def copyArrayByLength(jpOffset,usOffset,length):
        for i in range(length):
            J2U.usSaveArray[usOffset + i] = J2U.jpnSaveArray[jpOffset + i]

    def calculateChecksum(start,end):
        array = []
        for i in range(start,end + 1):
            array.append(J2U.usSaveArray[i])
        checksum =(~(sum(array) & 0xFF)) & 0xFF
        return checksum

    def setChecksum(start,end,setOffset,desc):
        checksum = J2U.calculateChecksum(start,end)
        print(desc + ' Checksum 是：' + hex(checksum))
        J2U.usSaveArray[setOffset] = checksum
        print()

    def writeByteArrayAsFile(file_path, byte_array):
        with open(file_path, 'wb') as file:
            file.write(byte_array)

    def setBoxChecksums():
        origOffset = 0x4000
        for k in range(2):
            offset = origOffset + k * 0x2000
            for i in range(6):
                boxOffset = offset + i * 0x462
                singleBoxChecksumOffset = offset + 0x1A4D + i
                J2U.setChecksum(boxOffset,boxOffset + 0x462,singleBoxChecksumOffset,'盒子 ' + str(i + 1 + 6 * k))
            J2U.setChecksum(offset,offset + 0x1A4B,offset + 0x1A4C,'Bank ' + str(1 + k))
            # setChecksum(offset,offset + 0x15EA,offset + 0x1A4C,'Bank ' + str(1 + k))


    def parseJPNBoxData(offset):
        speciesIDs = []
        OTNames = []
        pkmnDatas = []
        pkmnCount = J2U.jpnSaveArray[offset]
        if pkmnCount > 30:
            pkmnCount = 0
        for i in range(pkmnCount):
            speciesIDs.append(J2U.jpnSaveArray[offset + 1 + i])

            pkmnData = []
            for k in range(33):
                pkmnData.append(J2U.jpnSaveArray[offset + 0x20 + k + i * 33])
            pkmnDatas.append(pkmnData)

            OTName = []
            for j in range(6):
                OTName.append(J2U.jpnSaveArray[offset + 0x3FE + j + i * 6])
            OTNames.append(OTName)

        
        for i in range(pkmnCount):
            tmpPKMN = J2U.PokemonData()
            tmpPKMN.speciesID = speciesIDs[i]
            tmpPKMN.otName = OTNames[i]
            tmpPKMN.pkmnData = pkmnDatas[i]
            if i <= 19:
                J2U.outputBox.append(tmpPKMN)
            else:
                J2U.extraBox.append(tmpPKMN)
        return J2U.outputBox

    def writeBoxData(boxData,offset,option):
        tmpBoxData = bytearray(0x462)
        tmpBoxData[0] = len(boxData)
        J2U.writeValueAt(tmpBoxData, 1, 0xFF, 21)
        for i in range(len(boxData)):
            currPKMN:J2U.PokemonData = boxData[i]
            tmpBoxData[1 + i] = currPKMN.speciesID
            J2U.writeArrayAt(tmpBoxData, 0x16 + 33 * i,currPKMN.pkmnData)
            J2U.writeArrayAt(tmpBoxData, 0x2AA + 0xB * i,J2U.defaultOTname)
            if option != 2:
                J2U.writeArrayAt(tmpBoxData, 0x386 + 0xB * i,J2U.chsPMNames[currPKMN.speciesID])
            else:
                J2U.writeArrayAt(tmpBoxData, 0x386 + 0xB * i,J2U.engPMNames[currPKMN.speciesID])
        J2U.writeArrayAt(J2U.usSaveArray,offset,tmpBoxData)

    def getBoxOffsets():
        origOffset = 0x4000
        offsetsJPN = []
        for k in range(2):
            offset = origOffset + k * 0x2000
            for i in range(4):
                offsetsJPN.append(offset + i * 0x566)

        offsetsUS = []
        for k in range(2):
            offset = origOffset + k * 0x2000
            for i in range(6):
                offsetsUS.append(offset + i * 0x462)
        return (offsetsUS,offsetsJPN)
        
    def convertJPNtoUSA(path,save_path,optionRAW,otName,rivalName):
        option = optionRAW + 1

        J2U.defaultOTname = J2U.convertStr(otName)
        J2U.defaultPMname = J2U.convertStr(rivalName)

        J2U.jpnSaveArray = J2U.readFileAsByteArray(path)
        J2U.usSaveArray = bytearray(len(J2U.jpnSaveArray))
        J2U.extraBox = []
        J2U.outputBox = []

        J2U.writeArrayAt(J2U.usSaveArray,0x2598,J2U.defaultOTname)
        J2U.copyArray(0x259E,0x25A3,0x25F6)
        J2U.writeArrayAt(J2U.usSaveArray,0x25F6,J2U.defaultPMname)
        J2U.copyArray(0x25F7,0x2601,0x2B33)
        J2U.copyArray(0x2CA0,0x2CED,0x2CF5)
        dayCareSpecies = J2U.jpnSaveArray[0x2CB4]
        if option != 2:
            J2U.writeArrayAt(J2U.usSaveArray,0x2CF5,J2U.chsPMNames[dayCareSpecies])
        else:
            J2U.writeArrayAt(J2U.usSaveArray,0x2CF5,J2U.engPMNames[dayCareSpecies])
        J2U.writeArrayAt(J2U.usSaveArray,0x2D00,J2U.defaultOTname)
        J2U.copyArray(0x2CB4,0x2D0B,0x2F2C)
        J2U.copyArray(0x2C98,0x2CE5,0x2CED)

        J2U.copyArray(0x2C97,0x2CE4,0x2CE5)

        J2U.copyArrayByLength(0x2ED5,0x2F2C,0x110)

        index = 0x2F2C + 0x110
        for i in range(6):
            J2U.writeArrayAt(J2U.usSaveArray,index + i * 0xB ,J2U.defaultOTname)
        index = 0x2F2C + 0x152
        for i in range(6):
            if J2U.usSaveArray[0x2F2C + 1 + i] <= 190:
                if option != 2:
                    J2U.writeArrayAt(J2U.usSaveArray,index + i * 0xB ,J2U.chsPMNames[J2U.usSaveArray[0x2F2C + 1 + i]])
                else:
                    J2U.writeArrayAt(J2U.usSaveArray,index + i * 0xB ,J2U.engPMNames[J2U.usSaveArray[0x2F2C + 1 + i]])

        currentPKMNBox = J2U.parseJPNBoxData(0x302D)
        J2U.writeBoxData(currentPKMNBox,0x30C0,option)
        J2U.setChecksum(0x2598,0x3522,0x3523,'Main Data')


        boxOffsets = J2U.getBoxOffsets()
        for boxno in range(8):
            currentPKMNBox = J2U.parseJPNBoxData(boxOffsets[1][boxno])
            J2U.writeBoxData(currentPKMNBox,boxOffsets[0][boxno],option)

        for boxno in range(8,12):
            count = 0
            tmpPKMNBox = []
            # print(extraBox)
            while len(J2U.extraBox)!= 0 and count < 20:
                tmpPKMNBox.append(J2U.extraBox.pop(0))
                count += 1
            J2U.writeBoxData(tmpPKMNBox,boxOffsets[0][boxno],option)



        J2U.setBoxChecksums()
        J2U.writeByteArrayAsFile(save_path,J2U.usSaveArray)
        print('JPN to USA Conversion done')
        return 0



class U2J:
    root = []
    # root = tk.Tk()
    # root.withdraw()
    defaultOTname = bytearray(b'\x8A\x93\x8B\x50\x50\x50')
    defaultPMname = bytearray(b'\x8B\x08\xA6\x50\x50\x50')
    jpnPMNames = [bytearray(b'\x8A\x81\x13\xAB\x50\x50'), bytearray(b'\x8A\x81\x13\xAB\x50\x50'), bytearray(b'\x05\xA6\xE3\xA5\x50\x50'), bytearray(b'\x95\x13\xA5\xAB\xEF\x50'), bytearray(b'\x41\xAC\x41\x50\x50\x50'), bytearray(b'\x84\x95\x8C\x0C\xA0\x50'), bytearray(b'\x1A\xD8\xD8\x0F\x9D\x50'), bytearray(b'\x95\x13\x86\xAB\x07\x50'), bytearray(b'\xA2\x13\xA5\xAB\x50\x50'), bytearray(b'\x9B\x8B\x06\x8E\x82\x50'), bytearray(b'\x94\xAC\x8B\xE3\x50\x50'), bytearray(b'\x3D\xA8\xD8\xAB\x05\x50'), bytearray(b'\x8F\x9D\x8F\x9D\x50\x50'), bytearray(b'\x3D\x93\x3D\x8F\xE3\x50'), bytearray(b'\x08\xAB\x05\xE3\x50\x50'), bytearray(b'\x95\x13\xA5\xAB\xF5\x50'), bytearray(b'\x95\x13\x87\x81\xAB\x50'), bytearray(b'\x85\xA5\x85\xA5\x50\x50'), bytearray(b'\x8A\x81\x9C\xE3\xAB\x50'), bytearray(b'\xA5\x42\xA5\x8C\x50\x50'), bytearray(b'\x82\x81\xAB\x12\xB0\x50'), bytearray(b'\x9E\xAE\x82\x50\x50\x50'), bytearray(b'\x06\xAD\xA5\x13\x8C\x50'), bytearray(b'\x8B\xEB\xA6\x0F\xE3\x50'), bytearray(b'\xA0\x98\x87\xA5\x08\x50'), bytearray(b'\x09\xE3\x8C\x50\x50\x50'), bytearray(b'\x8C\x93\xA5\x81\x87\x50'), bytearray(b'\x9A\x93\x12\x9D\xAB\x50'), bytearray(b'\x85\xA0\xAC\x87\x8C\x50'), bytearray(b'\x85\x81\xA8\x8C\x50\x50'), bytearray(b'\xA1\xAB\x0B\xAD\xA5\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x05\xE3\x12\xB0\x50\x50'), bytearray(b'\x81\xA9\xE3\x87\x50\x50'), bytearray(b'\x84\x95\x13\xD8\xA6\x50'), bytearray(b'\x43\xAC\x43\x50\x50\x50'), bytearray(b'\xA2\x13\xAB\x50\x50\x50'), bytearray(b'\xA3\xAB\x08\xA5\xE3\x50'), bytearray(b'\x09\xA8\xE3\xAB\x50\x50'), bytearray(b'\xA5\xAC\x86\xE3\x50\x50'), bytearray(b'\x09\xE3\xD8\x86\xE3\x50'), bytearray(b'\x19\xD8\xA2\xE3\x13\x50'), bytearray(b'\x8A\xA9\x9F\xA5\xE3\x50'), bytearray(b'\x83\x1A\xA9\xA5\xE3\x50'), bytearray(b'\x80\xE3\x1C\xAC\x87\x50'), bytearray(b'\x40\xA5\x8D\x87\x93\x50'), bytearray(b'\x89\x0F\xAC\x87\x50\x50'), bytearray(b'\x8C\xD8\xE3\x42\x50\x50'), bytearray(b'\x09\xA8\xE3\x95\xAD\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x1B\xE3\x19\xE3\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x83\xA7\x1B\xE3\x50\x50'), bytearray(b'\xA7\x80\x89\x81\xA6\x50'), bytearray(b'\x13\x05\xE3\x8C\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9D\xAB\x86\xE3\x50\x50'), bytearray(b'\x40\x82\xA9\x82\x50\x50'), bytearray(b'\x12\xB0\x07\x0F\x50\x50'), bytearray(b'\x88\xAB\x8F\xA8\x8C\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x85\xA1\x97\x06\x50\x50'), bytearray(b'\x89\xAB\x40\xAB\x50\x50'), bytearray(b'\x85\x81\xD8\xAE\xE3\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x13\xE3\x13\xE3\x50\x50'), bytearray(b'\x95\xAF\xA8\xA1\x50\x50'), bytearray(b'\xA6\xE3\x0B\xAE\xA5\x50'), bytearray(b'\x9B\xE9\x81\xA2\xE3\x50'), bytearray(b'\x9B\xD8\xE3\x0A\xE3\x50'), bytearray(b'\x8A\xAB\x0F\xE3\x50\x50'), bytearray(b'\xA0\x8F\xA1\xAB\x50\x50'), bytearray(b'\x95\xAD\xE3\x8C\x50\x50'), bytearray(b'\x87\xA5\x1B\x50\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xA8\x89\xAB\x50\x50\x50'), bytearray(b'\x86\xAE\x82\x89\xAB\x50'), bytearray(b'\x41\x85\x90\xAE\x82\x50'), bytearray(b'\xA5\x81\x90\xAE\x82\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9E\x95\xD8\xAE\x82\x50'), bytearray(b'\x99\x87\xD8\xAE\xE3\x50'), bytearray(b'\x85\x1B\x93\x50\x50\x50'), bytearray(b'\x85\x1B\x93\x42\x8C\x50'), bytearray(b'\x8F\xAC\x91\xE3\x50\x50'), bytearray(b'\x8B\xE3\x13\xA5\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x8A\xAB\x13\x50\x50\x50'), bytearray(b'\x8A\xAB\x13\x40\xAB\x50'), bytearray(b'\x84\x9F\x94\x81\x93\x50'), bytearray(b'\x84\x9F\x8C\x8F\xE3\x50'), bytearray(b'\x42\xD8\xAB\x50\x50\x50'), bytearray(b'\x42\x87\xD8\xAB\x50\x50'), bytearray(b'\x81\xE3\x1B\x81\x50\x50'), bytearray(b'\x1B\xE3\x8C\x8F\xE3\x50'), bytearray(b'\x8A\xAB\x0F\xE3\x8C\x50'), bytearray(b'\x8B\xAD\xA9\xE3\x0C\x50'), bytearray(b'\xA9\xAB\xD8\x86\xE3\x50'), bytearray(b'\x0C\x19\xAC\x93\x50\x50'), bytearray(b'\x80\xE3\x1C\x50\x50\x50'), bytearray(b'\x40\xA5\x8C\x50\x50\x50'), bytearray(b'\x95\xAF\xA8\x0E\x50\x50'), bytearray(b'\x95\xAF\xA8\x1C\xAB\x50'), bytearray(b'\x1A\xE3\x13\xA6\x50\x50'), bytearray(b'\x89\x87\xE3\xAB\x50\x50'), bytearray(b'\x8C\x41\x80\xE3\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x13\xE3\x13\xD8\x84\x50'), bytearray(b'\x84\x89\xD8\x0A\xA6\x50'), bytearray(b'\x0F\x07\x93\xD8\x84\x50'), bytearray(b'\xA1\xA6\x9B\xF4\xAB\x50'), bytearray(b'\x0B\xAE\x09\xAB\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x86\xAD\x8F\x41\xE3\x50'), bytearray(b'\x93\xA5\xAB\x8D\xA6\x50'), bytearray(b'\x19\x8F\x9B\xD8\xE3\x50'), bytearray(b'\x85\x81\xD8\x86\xE3\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x09\xA6\x0F\xAC\x87\x50'), bytearray(b'\x8C\xD8\xE3\x40\xE3\x50'), bytearray(b'\x09\xA6\x19\xAC\x93\x50'), bytearray(b'\x9E\xAE\x82\x91\xE3\x50'), bytearray(b'\x85\x1A\x09\xAB\x50\x50'), bytearray(b'\x89\x81\x86\xAB\x07\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x3D\x93\x3D\x93\xAB\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x86\xAB\x07\xA5\xE3\x50'), bytearray(b'\x40\xA6\x8B\xEB\xAB\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9D\xA6\x9D\x81\xAB\x50'), bytearray(b'\x41\x87\x8B\xE3\x50\x50'), bytearray(b'\x9D\x8F\x13\x05\x8C\x50'), bytearray(b'\x47\xA6\x8B\x80\xAB\x50'), bytearray(b'\x05\xA5\x05\xA5\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x09\xE3\x8C\x93\x50\x50'), bytearray(b'\x88\xE3\x8B\xB0\x50\x50'), bytearray(b'\x9B\xE3\x12\xB0\xAB\x50'), bytearray(b'\x41\x0B\xAF\xAB\x50\x50'), bytearray(b'\x41\x0B\xAF\xAC\x93\x50'), bytearray(b'\x8C\x8F\xE3\x9E\xE3\x50'), bytearray(b'\x9B\x8B\x06\x0F\x97\x50'), bytearray(b'\x9B\x8B\x06\x19\x94\x50'), bytearray(b'\x13\x87\x87\xA5\x08\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x93\x8A\x86\xAB\x93\x50'), bytearray(b'\x80\x0C\x9D\x84\x82\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x43\x95\xE3\x8F\x50\x50'), bytearray(b'\x06\xAD\xA8\xAC\x42\x50'), bytearray(b'\x89\xA5\xAC\x8F\x50\x50'), bytearray(b'\xA5\xAC\x8F\x50\x50\x50'), bytearray(b'\x95\x13\xD8\xE3\x98\x50'), bytearray(b'\x95\x13\xD8\xE3\x94\x50'), bytearray(b'\x81\x8B\x91\x1B\x92\x50'), bytearray(b'\x43\xD8\x09\xAB\x50\x50'), bytearray(b'\x42\x92\xA5\x50\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x89\x81\xA6\x50\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x9A\x93\x85\x08\x50\x50'), bytearray(b'\x0D\x95\x05\xA0\x50\x50'), bytearray(b'\xD8\x0A\xE3\x13\x50\x50'), bytearray(b'\x85\xA0\xE3\xA6\x50\x50'), bytearray(b'\xD8\x0A\xE3\x13\xAB\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\xB9\xC2\x3A\xDE\x50\x50'), bytearray(b'\x09\xE3\x8C\x93\x50\x50'), bytearray(b'\x94\x0E\x98\x87\x8A\x50'), bytearray(b'\x87\x8A\x81\x99\x94\x50'), bytearray(b'\xA5\x9B\xA7\x8B\x80\x50'), bytearray(b'\x9D\x0F\x91\x1C\x9E\x50'), bytearray(b'\x82\x91\x13\xAB\x50\x50'), bytearray(b'\x82\x91\x1C\xAC\x93\x50')]
    
    inSaveArray = None
    outSaveArray = None
    extraBox = []

    def convertStr(string):
        byteList = []
        jpnCharmap = {"ガ": 0x05, "ギ": 0x06, "グ": 0x07, "ゲ": 0x08, "ゴ": 0x09, "ザ": 0x0a, "ジ": 0x0b, "ズ": 0x0c, "ゼ": 0x0d, "ゾ": 0x0e, "ダ": 0x0f, "ヂ": 0x10, "ヅ": 0x11, "デ": 0x12, "ド": 0x13, "バ": 0x19, "ビ": 0x1a, "ブ": 0x1b, "ベ": 0x3d, "ボ": 0x1c, "が": 0x26, "ぎ": 0x27, "ぐ": 0x28, "げ": 0x29, "ご": 0x2a, "ざ": 0x2b, "じ": 0x2c, "ず": 0x2d, "ぜ": 0x2e, "ぞ": 0x2f, "だ": 0x30, "ぢ": 0x31, "づ": 0x32, "で": 0x33, "ど": 0x34, "ば": 0x3a, "び": 0x3b, "ぶ": 0x3c, "べ": 0x3d, "ぼ": 0x3e, "パ": 0x40, "ピ": 0x41, "プ": 0x42, "ペ": 0x47, "ポ": 0x43, "ぱ": 0x44, "ぴ": 0x45, "ぷ": 0x46, "ぺ": 0x47, "ぽ": 0x48, "ア": 0x80, "イ": 0x81, "ウ": 0x82, "エ": 0x83, "オ": 0x84, "カ": 0x85, "キ": 0x86, "ク": 0x87, "ケ": 0x88, "コ": 0x89, "サ": 0x8a, "シ": 0x8b, "ス": 0x8c, "セ": 0x8d, "ソ": 0x8e, "タ": 0x8f, "チ": 0x90, "ツ": 0x91, "テ": 0x92, "ト": 0x93, "ナ": 0x94, "ニ": 0x95, "ヌ": 0x96, "ネ": 0x97, "ノ": 0x98, "ハ": 0x99, "ヒ": 0x9a, "フ": 0x9b, "ヘ": 0xcd, "ホ": 0x9c, "マ": 0x9d, "ミ": 0x9e, "ム": 0x9f, "メ": 0xa0, "モ": 0xa1, "ヤ": 0xa2, "ユ": 0xa3, "ヨ": 0xa4, "ラ": 0xa5, "リ": 0xd8, "ル": 0xa6, "レ": 0xa7, "ロ": 0xa8, "ワ": 0xa9, "ヲ": 0xaa, "ン": 0xab, "ッ": 0xac, "ャ": 0xad, "ュ": 0xae, "ョ": 0xaf, "あ": 0xb1, "い": 0xb2, "う": 0xb3, "え": 0xb4, "お": 0xb5, "か": 0xb6, "き": 0xb7, "く": 0xb8, "け": 0xb9, "こ": 0xba, "さ": 0xbb, "し": 0xbc, "す": 0xbd, "せ": 0xbe, "そ": 0xbf, "た": 0xc0, "ち": 0xc1, "つ": 0xc2, "て": 0xc3, "と": 0xc4, "な": 0xc5, "に": 0xc6, "ぬ": 0xc7, "ね": 0xc8, "の": 0xc9, "は": 0xca, "ひ": 0xcb, "ふ": 0xcc, "へ": 0xcd, "ほ": 0xce, "ま": 0xcf, "み": 0xd0, "む": 0xd1, "め": 0xd2, "も": 0xd3, "や": 0xd4, "ゆ": 0xd5, "よ": 0xd6, "ら": 0xd7, "り": 0xd8, "る": 0xd9, "れ": 0xda, "ろ": 0xdb, "わ": 0xdc, "を": 0xdd, "ん": 0xde, "っ": 0xdf, "ゃ": 0xe0, "ゅ": 0xe1, "ょ": 0xe2, "ー": 0xe3}
        if len(string) > 0 and len(string) <= 5:
            for char in string:
                if char in jpnCharmap:
                    byteList.append(jpnCharmap[char])
                else:
                    return None
        else:
            return None
        
        for i in range(6 - len(string)):
            byteList.append(0x50)
        return bytearray(byteList)
    
    class PokemonData:
        speciesID = 0
        pkmnData = bytearray(0)
        otName = bytearray(0)
        pkmnName = bytearray(0)


    def readFileAsByteArray(file_path):
        with open(file_path, 'rb') as file:
            byte_array = file.read()
            file.close()
        return bytearray(byte_array)

    def writeValueAt(array,offset,value,count):
        for i in range(count):
            array[offset + i] = value

    def writeArrayAt(array,offset,inputArray):
        for i in range(len(inputArray)):
            char = inputArray[i]
            array[offset + i] = char

    def copyArray(jpOffset,usOffset,usDestination):
        for i in range(usDestination - usOffset):
            # print(inSaveArray[jpOffset + i])
            U2J.outSaveArray[usOffset + i] = U2J.inSaveArray[jpOffset + i]

    def copyArrayByLength(jpOffset,usOffset,length):
        for i in range(length):
            U2J.outSaveArray[usOffset + i] = U2J.inSaveArray[jpOffset + i]

    def calculateChecksum(start,end):
        array = []
        for i in range(start,end + 1):
            array.append(U2J.outSaveArray[i])
        checksum =(~(sum(array) & 0xFF)) & 0xFF
        return checksum

    def setChecksum(start,end,setOffset,desc):
        checksum = U2J.calculateChecksum(start,end)
        print(desc + ' Checksum 是：' + hex(checksum))
        U2J.outSaveArray[setOffset] = checksum
        print()

    def writeByteArrayAsFile(file_path, byte_array):
        with open(file_path, 'wb') as file:
            file.write(byte_array)

    def setBoxChecksums():
        origOffset = 0x4000
        for k in range(2):
            offset = origOffset + k * 0x2000
            for i in range(4):
                boxOffset = offset + i * 0x566
                singleBoxChecksumOffset = offset + 0x1599 + i
                U2J.setChecksum(boxOffset,boxOffset + 0x566,singleBoxChecksumOffset,'盒子 ' + str(i + 1 + 6 * k))
            U2J.setChecksum(offset,offset + 0x1597,offset + 0x1598,'Bank ' + str(1 + k))

    def getBoxOffsets():
        origOffset = 0x4000
        offsetsJPN = []
        for k in range(2):
            offset = origOffset + k * 0x2000
            for i in range(4):
                offsetsJPN.append(offset + i * 0x566)

        offsetsUS = []
        for k in range(2):
            offset = origOffset + k * 0x2000
            for i in range(6):
                offsetsUS.append(offset + i * 0x462)

        return (offsetsUS,offsetsJPN)
        
    
    def parseUSABoxData(offset,mode):
        speciesIDs = []
        OTNames = []
        pkmnDatas = []
        pkmnCount = U2J.inSaveArray[offset]
        if pkmnCount > 20:
            pkmnCount = 0
        for i in range(pkmnCount):
            speciesIDs.append(U2J.inSaveArray[offset + 1 + i])

            pkmnData = []
            for k in range(33):
                pkmnData.append(U2J.inSaveArray[offset + 0x16 + k + i * 33])
            pkmnDatas.append(pkmnData)

            OTName = []
            for j in range(6):
                OTName.append(U2J.inSaveArray[offset + 0x2AA + j + i * 0xB])
            OTNames.append(OTName)

        outputBox = []
        for i in range(pkmnCount):
            tmpPKMN = U2J.PokemonData()
            tmpPKMN.speciesID = speciesIDs[i]
            tmpPKMN.otName = OTNames[i]
            tmpPKMN.pkmnData = pkmnDatas[i]
            if mode == 1:
                outputBox.append(tmpPKMN)
            else:
                U2J.extraBox.append(tmpPKMN)
        return outputBox

    def writeBoxData(boxData,offset):
        tmpBoxData = bytearray(0x566)
        tmpBoxData[0] = len(boxData)
        U2J.writeValueAt(tmpBoxData, 1, 0xFF, 31)
        for i in range(len(boxData)):
            currPKMN:U2J.PokemonData = boxData[i]
            tmpBoxData[1 + i] = currPKMN.speciesID
            U2J.writeArrayAt(tmpBoxData, 0x20 + 33 * i,currPKMN.pkmnData)
            U2J.writeArrayAt(tmpBoxData, 0x3FE + 0x6 * i,U2J.defaultOTname)
            U2J.writeArrayAt(tmpBoxData, 0x4B2 + 0x6 * i,U2J.jpnPMNames[currPKMN.speciesID])
        U2J.writeArrayAt(U2J.outSaveArray,offset,tmpBoxData)

    def convertUSAtoJPN(path,save_path,otName,rivalName):

        U2J.defaultOTname = U2J.convertStr(otName)
        U2J.defaultPMname = U2J.convertStr(rivalName)

        U2J.inSaveArray = U2J.readFileAsByteArray(path)
        U2J.outSaveArray = bytearray(len(U2J.inSaveArray))
        U2J.extraBox = []

        U2J.writeArrayAt(U2J.outSaveArray,0x2598,U2J.defaultOTname)
        U2J.copyArray(0x25A3,0x259E,0x25F1)
        U2J.writeArrayAt(U2J.outSaveArray,0x25F1,U2J.defaultPMname)
        U2J.copyArray(0x2601,0x25F7,0x2B2A)
        U2J.copyArray(0x2CE4,0x2C97,0x2CA8)
        dayCareSpecies = U2J.inSaveArray[0x2D0B]
        if dayCareSpecies <= 190:
            U2J.writeArrayAt(U2J.outSaveArray,0x2CA8,U2J.jpnPMNames[dayCareSpecies])    
        U2J.writeArrayAt(U2J.outSaveArray,0x2CAE,U2J.defaultOTname)
        U2J.copyArray(0x2D0B,0x2CB4,0x2ED5)

        U2J.copyArrayByLength(0x2F2C,0x2ED5,0x110)
        index = 0x2ED5 + 0x110
        for i in range(6):
            U2J.writeArrayAt(U2J.outSaveArray,index + i * 0x6 ,U2J.defaultOTname)
        index = 0x2ED5 + 0x134
        for i in range(6):
            if U2J.outSaveArray[0x2ED5 + 1 + i] <= 190:
                U2J.writeArrayAt(U2J.outSaveArray,index + i * 0x6 ,U2J.jpnPMNames[U2J.outSaveArray[0x2ED5 + 1 + i]])


        currentBoxNo = U2J.inSaveArray[0x284C] & 0x7F
        print('Current Box No. ' + str(currentBoxNo + 1))
        currentPKMNBox = U2J.parseUSABoxData(0x30C0,1)
        U2J.writeBoxData(currentPKMNBox,0x302D)
        U2J.setChecksum(0x2598,0x3593,0x3594,'Main Data')

        boxOffsets = U2J.getBoxOffsets()
        for boxno in range(12):
            U2J.parseUSABoxData(boxOffsets[0][boxno],2)

        for boxno in range(8):
            if currentBoxNo == boxno:
                continue
            count = 0
            tmpPKMNBox = []
            while len(U2J.extraBox)!= 0 and count < 30:
                tmpPKMNBox.append(U2J.extraBox.pop(0))
                count += 1
            U2J.writeBoxData(tmpPKMNBox,boxOffsets[1][boxno])


        U2J.setBoxChecksums()


        U2J.writeByteArrayAsFile(save_path,U2J.outSaveArray)
        print('USA to JPN Conversion done')
        return 0

class WXWindow(wx.Frame):
    def __init__(self, parent, title):
        super(WXWindow, self).__init__(parent, style = wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU, title=title,
            size=(600, 340))
        
        self.convertMode = 0
        self.converLang = 0
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        # font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        loadST = wx.StaticText(panel, label='读取存档路径\nLoad File Path')
        # loadST.SetFont(font)
        hbox1.Add(loadST, flag=wx.CENTER | wx.LEFT, border=5)

        self.loadTC = wx.TextCtrl(panel)
        hbox1.Add(self.loadTC, flag=wx.CENTER | wx.LEFT, border=5, proportion=1)

        loadBTN = wx.Button(panel, label='选择 / Choose', size=(100, 30))
        loadBTN.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        hbox1.Add(loadBTN, flag=wx.CENTER | wx.LEFT, border=5)
        
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)


        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        saveST = wx.StaticText(panel, label='保存存档路径\nSave File Path')
        # saveST.SetFont(font)
        hbox2.Add(saveST, flag=wx.CENTER | wx.LEFT, border=5)

        self.saveTC = wx.TextCtrl(panel)
        hbox2.Add(self.saveTC, flag=wx.CENTER | wx.LEFT, border=5, proportion=1)

        saveBTN = wx.Button(panel, label='选择 / Choose', size=(100, 30))
        saveBTN.Bind(wx.EVT_BUTTON, self.OnSaveFile)
        hbox2.Add(saveBTN, flag=wx.CENTER | wx.LEFT, border=5)
        
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        convertST = wx.StaticText(panel, label='转换模式\nConvert Mode')
        hbox3.Add(convertST, flag=wx.CENTER | wx.LEFT, border=5)

        distros = ['日转美 / JPN to USA', '美转日 / USA to JPN', ]
        modeCB = wx.ComboBox(panel, choices=distros, 
            style=wx.CB_READONLY)
        modeCB.SetSelection(0)
        hbox3.Add(modeCB, flag=wx.CENTER | wx.LEFT, border=5,  proportion=1)

        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # self.st = wx.StaticText(panel, label='', pos=(50, 140))
        modeCB.Bind(wx.EVT_COMBOBOX, self.OnSelectConvertMode)
        

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        OTnameST = wx.StaticText(panel, label='主角名称\nOT Name')
        hbox6.Add(OTnameST, flag=wx.CENTER | wx.LEFT, border=5)

        self.OTNameTC = wx.TextCtrl(panel)
        
        hbox6.Add(self.OTNameTC, flag=wx.CENTER | wx.LEFT, border=5, proportion=1)

        vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        RivalNameST = wx.StaticText(panel, label='劲敌名称\nRIVAL Name')
        hbox7.Add(RivalNameST, flag=wx.CENTER | wx.LEFT, border=5)

        self.RivalNameTC = wx.TextCtrl(panel)
        hbox7.Add(self.RivalNameTC, flag=wx.CENTER | wx.LEFT, border=5, proportion=1)

        vbox.Add(hbox7, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.OTNameTC.SetValue("ASH")
        self.RivalNameTC.SetValue("GARY")

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        encodingST = wx.StaticText(panel, label='宝可梦名称 / Pokemon Names\n仅限日转美 / JPN to USA Only')
        hbox4.Add(encodingST, flag=wx.CENTER | wx.LEFT, border=5 )

        distrosLang = ['中文名称(2023新版汉化) / for Chinese Translation Pack', '英文名称 / English']
        langCB = wx.ComboBox(panel, choices=distrosLang, 
            style=wx.CB_READONLY)
        langCB.SetSelection(0)
        
        hbox4.Add(langCB, flag=wx.CENTER | wx.LEFT, border=5, proportion=1)

        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        self.st = wx.StaticText(panel, label='', pos=(250, 140))
        langCB.Bind(wx.EVT_COMBOBOX, self.OnSelectConvertLang)
        







        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='帮助', size=(70, 30))
        btn1.Bind(wx.EVT_BUTTON, self.OnOpenHelpCHS)
        hbox5.Add(btn1, flag=wx.LEFT|wx.BOTTOM, border=5)
        btn2 = wx.Button(panel, label='Help', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        btn2.Bind(wx.EVT_BUTTON, self.OnOpenHelpENG)
        btn3 = wx.Button(panel, label='转换 / Convert', size=(120, 30))
        btn3.Bind(wx.EVT_BUTTON, self.OnConvert)
        hbox5.Add(btn3, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)


        panel.SetSizer(vbox)


        self.Centre()

    def OnSelectConvertMode(self, e):
        self.convertMode = e.GetSelection()
        # print(e.GetSelection())
        if e.GetSelection() == 0:
            self.OTNameTC.SetValue("ASH")
            self.RivalNameTC.SetValue("GARY")
        else:
            self.OTNameTC.SetValue("サトシ")
            self.RivalNameTC.SetValue("シゲル")

    def OnOpenFile(self,e):
        # otherwise ask the user what new file to open
        with wx.FileDialog(self, "Open sav file", wildcard="sav files (*.sav)|*.sav",
                        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            self.loadTC.SetValue(pathname)

    def OnSaveFile(self,e):
        with wx.FileDialog(self, "Save sav file", wildcard="sav files (*.sav)|*.sav",
                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            self.saveTC.SetValue(pathname)


    def OnSelectConvertLang(self, e):
         self.converLang = e.GetSelection()

    def OnOpenHelpCHS(self, e):
        helpTextCHS = '注意：\n\n名人堂数据不会被迁移。\n\n存档所有的宝可梦的初训家将会改成主角名字。宝可梦名称会被还原成默认名。\n\n中文名称仅兼容2023新版汉化，不兼容CKN皮卡丘汉化版。\n\n主角/劲敌名字仅能使用英文（日转美）或日文（美转日），长度不超过7个（日转美）或者5个字符（美转日）。\n\n美版存档转日版存档时，当前盒子以外，剩余 11 个盒子的宝可梦若超过 210 只 （最大 220 只），将只迁移前面的 210 只。第210-220只宝可梦会被丢弃！\n\n转换前，请先在宝可梦中心垫子处存档，迁移完成后立刻离开宝可梦中心。\n如果上述方法无法使用，请在迁移前，在城镇外宝可梦中心存档，迁移后立刻使用飞翔离开城镇。'
        wx.MessageBox(helpTextCHS, '注意', wx.OK | wx.ICON_INFORMATION)

    def OnOpenHelpENG(self, e):
        helpTextCHS = 'WARNING: \n\nThe HALL OF FAME Data will not be transferred.\n\nPokémon names will reset to default ones, and the OT names of pokémons will be set to the OT Name in this App.\n\nOT / Rival names are only valid in English or Japanese depending on the target region save file. No longer than 5 characters in Japansese and 7 characters in English.\n\nWhen converting FROM the international save file, only the first 210 pokémons not in the current box will be transferred (11 boxes, 220 in total). '
        wx.MessageBox(helpTextCHS, 'WARNING', wx.OK | wx.ICON_INFORMATION)


    def OnQuit(self, e):
        self.Close()
        
    def OnConvert(self, e):
        openpath = self.loadTC.GetValue()
        savepath = self.saveTC.GetValue()
        otName = self.OTNameTC.GetValue()
        rivalName = self.RivalNameTC.GetValue()
        if self.convertMode == 0:
            try:
                J2U.convertJPNtoUSA(openpath,savepath,self.converLang,otName,rivalName)
                wx.MessageBox('转换完成！\nConversion Complete!', 'Info', wx.OK | wx.ICON_INFORMATION)
            except:
                wx.MessageBox('出错！\nERROR!', 'Error', wx.OK | wx.ICON_INFORMATION)
        else:
            try:
                U2J.convertUSAtoJPN(openpath,savepath,otName,rivalName)
                wx.MessageBox('转换完成！\nConversion Complete!', 'Info', wx.OK | wx.ICON_INFORMATION)
            except:
                wx.MessageBox('出错！\nERROR!', 'Error', wx.OK | wx.ICON_INFORMATION)

        

def main():

    if len(sys.argv) >= 6 and len(sys.argv) <= 7:
        argvDict = dict()
        for item in sys.argv:
            comp = item.split('=')
            if len(comp) > 1:
                argvDict[comp[0]] = comp[1]

        # print(argvDict)

        defargv = ['in','out','mode','lang','otname','rivalname']
        args = [] 
        for index in range(len(defargv)):
            arg = defargv[index]
            if arg in argvDict:
                args.append(argvDict[arg])
                # print(args)
            elif arg != 'lang':
                print('ERROR: argument ' + arg + 'Not Found')
                print('Usage: convert.py in=inputSavePath out=outputSavePath mode=(j2u|u2j) otname=OTNAME rivalname=RIVALNAME [lang=(en|cn)]')
                print('You must specify lang=(en|cn) if mode=j2u')
                exit(-1)
        if args[2] != 'j2u' and args[2] != 'u2j':
                print('Usage: convert.py in=inputSavePath out=outputSavePath mode=(j2u|u2j) otname=OTNAME rivalname=RIVALNAME [lang=(en|cn)]')
                exit(-1)
        if args[2] == 'j2u' and not 'lang' in argvDict:
                print('ERROR: argument ' + 'lang' + ' Not Found')
                print('Usage: convert.py in=inputSavePath out=outputSavePath mode=(j2u|u2j) otname=OTNAME rivalname=RIVALNAME [lang=(en|cn)]')
                print('You must specify lang=(en|cn) if mode=j2u')
                exit(-1)
        if args[2] == 'j2u' and (args[3] != 'cn' and args[3] != 'en'):
                print('Usage: convert.py in=inputSavePath out=outputSavePath mode=(j2u|u2j) otname=OTNAME rivalname=RIVALNAME [lang=(en|cn)]')
                print('You must specify lang=(en|cn) if mode=j2u')
                exit(-1)

        if args[2] == 'j2u':
            lang = 0
            if args[3] == 'en':
                lang = 1
            try:
                J2U.convertJPNtoUSA(args[0],args[1],lang,args[4],args[5])
            except:
                print("ERROR!")
        elif args[2] == 'u2j':
            try:
                U2J.convertUSAtoJPN(args[0],args[1],args[4],args[5])
            except:
                print("ERROR!")

    
    else:
        app = wx.App()
        ex = WXWindow(None, title='Pokemon Gen 1 Save Converter')
        ex.Show()
        app.MainLoop()


if __name__ == '__main__':
    main()



