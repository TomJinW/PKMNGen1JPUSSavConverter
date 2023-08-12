import os
import sys
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
chsPMNames = [bytearray(b'\x19\x47\x0A\x63\x11\xB6\x0F\xD6\x50\x50'), bytearray(b'\x19\x47\x0A\x63\x11\xB6\x0F\xD6\x50\x50'), bytearray(b'\x06\xD2\x0F\xD6\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0B\x9E\x50\x50\x50\x50'), bytearray(b'\x0D\xE8\x0D\xE8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\x08\x0E\xD6\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\xDF\x2D\xE4\x07\x23\x0E\xB2\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x06\xCA\x0B\x27\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x0C\xFA\x11\x10\x05\xD9\x50\x50\x50\x50'), bytearray(b'\x12\xEE\x06\xE4\x0F\xEF\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0F\x7A\x10\xE7\x50\x50\x50\x50'), bytearray(b'\x06\xE4\x06\xE4\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x6C\x0D\x68\x50\x50\x50\x50\x50\x50'), bytearray(b'\x08\x8A\x08\xD5\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0B\x90\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x09\x42\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x0B\x81\x0B\x04\x0B\x81\x50\x50'), bytearray(b'\x07\x70\x0A\x63\x11\xB6\x0D\x89\x50\x50'), bytearray(b'\x0B\x81\x0E\x20\x0B\x81\x10\x13\x50\x50'), bytearray(b'\x07\xF5\x10\x37\x08\x9F\x50\x50\x50\x50'), bytearray(b'\x0C\xDA\x09\x85\x50\x50\x50\x50\x50\x50'), bytearray(b'\x05\x31\x0B\xC4\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0F\x7A\x05\x3C\x50\x50\x50\x50'), bytearray(b'\x0C\x98\x28\x0F\x10\x08\x0D\x2A\x50\x50'), bytearray(b'\x08\xD5\x10\x13\x50\x50\x50\x50\x50\x50'), bytearray(b'\x07\xD7\x10\xBE\x2C\xAF\x2C\x91\x50\x50'), bytearray(b'\x08\xE9\x12\x37\x12\x37\x50\x50\x50\x50'), bytearray(b'\x10\x08\x0A\x25\x08\xD2\x50\x50\x50\x50'), bytearray(b'\x0B\x09\x0C\x8C\x10\x13\x50\x50\x50\x50'), bytearray(b'\x0C\xA9\x10\xAB\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x07\x11\x08\x9F\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x12\xB6\x0F\x79\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x19\x49\x0E\xD6\x50\x50\x50\x50'), bytearray(b'\x05\xA4\x05\xA4\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\xCA\x06\xCA\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x13\x80\x09\xBB\x0B\x81\x50\x50\x50\x50'), bytearray(b'\x0C\x39\x0C\x39\x0F\xA7\x50\x50\x50\x50'), bytearray(b'\x09\xCA\x0B\xCF\x06\xE4\x50\x50\x50\x50'), bytearray(b'\x09\x0A\x0B\xD8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x18\x0E\x7D\x0E\xE9\x0D\xA2\x50\x50'), bytearray(b'\x07\xD7\x10\xF8\x0B\x9D\x50\x50\x50\x50'), bytearray(b'\x0B\x62\x0E\xCB\x0B\x9D\x50\x50\x50\x50'), bytearray(b'\x04\xC4\x04\xFA\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x0D\xAF\x0B\x81\x10\x13\x10\xAA\x50\x50'), bytearray(b'\x0B\x29\x06\xC5\x12\xA0\x50\x50\x50\x50'), bytearray(b'\x06\xB5\x0C\xEB\x2D\xD6\x50\x50\x50\x50'), bytearray(b'\x0C\x39\x0C\x39\x12\xB6\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\xA0\x19\x49\x09\xB2\x0F\xD6\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x07\x23\x09\xB9\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x0F\x23\x09\x1C\x13\x01\x06\x9B\x08\xBE'), bytearray(b'\x11\x13\x10\x13\x06\xE3\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x09\x3D\x08\xBE\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x08\xE9\x0F\xA0\x50\x50\x50\x50'), bytearray(b'\x07\x10\x0F\xEB\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x2F\x10\x7B\x0C\x8C\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x06\xA6\x12\xA0\x50\x50\x50\x50'), bytearray(b'\x0C\xB7\x0E\xB2\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x62\x0C\x34\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x1C\xD7\x1C\xD7\x50\x50\x50\x50\x50\x50'), bytearray(b'\x11\x6F\x11\xED\x2C\x98\x2C\x63\x50\x50'), bytearray(b'\x0C\xE0\x06\x93\x0A\x7F\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x12\xCA\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x09\xD1\x07\x63\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x0F\x46\x07\x23\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x04\xFB\x05\x82\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x1C\xB3\x1C\xB3\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0E\x6F\x12\x27\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\x33\x11\x49\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0A\xBF\x11\x49\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\xE8\x0B\x04\x0E\xB0\x50\x50\x50\x50'), bytearray(b'\x0B\xAB\x0E\xB0\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\xE0\x0D\x6B\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x08\xE6\x0B\x2B\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x09\x71\x0F\xA7\x0B\x6E\x50\x50\x50\x50'), bytearray(b'\x0B\xDF\x06\xEA\x0B\x6E\x50\x50\x50\x50'), bytearray(b'\x0D\x1C\x08\xE9\x0C\x9B\x50\x50\x50\x50'), bytearray(b'\x08\xE9\x06\xA2\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x7F\x0F\x42\x0F\xEB\x50\x50\x50\x50'), bytearray(b'\x06\x7F\x0F\x42\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x0A\xCF\x0F\xA7\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x07\x90\x06\xA2\x0A\xCF\x0F\xA7\x0F\xD6'), bytearray(b'\x0D\xBC\x07\x3B\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\xBC\x0B\x29\x07\x3B\x50\x50\x50\x50'), bytearray(b'\x13\x07\x05\xB8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x13\x07\x05\xB8\x50\x50\x50\x50'), bytearray(b'\x0B\xAB\x13\x07\x05\xB8\x50\x50\x50\x50'), bytearray(b'\x10\x08\x13\x07\x05\xB8\x50\x50\x50\x50'), bytearray(b'\x11\x2B\x0B\xD8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x0A\x13\x3E\x2C\x96\x50\x50\x50\x50'), bytearray(b'\x04\xC4\x04\xFA\x0F\x79\x50\x50\x50\x50'), bytearray(b'\x0D\xAF\x0B\x81\x10\x13\x50\x50\x50\x50'), bytearray(b'\x11\x6F\x11\xED\x0A\xF7\x50\x50\x50\x50'), bytearray(b'\x11\x6F\x11\xED\x13\x7C\x0F\xB7\x50\x50'), bytearray(b'\x07\x70\x0A\x63\x06\x49\x50\x50\x50\x50'), bytearray(b'\x10\xCC\x0B\x27\x13\x7A\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x18\x83\x07\xF2\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x1C\xD7\x1C\xD7\x0B\xCF\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x05\x31\x09\x3D\x50\x50\x50\x50'), bytearray(b'\x0F\x23\x07\x10\x0F\xEB\x50\x50\x50\x50'), bytearray(b'\x0D\x17\x0C\x61\x07\x9A\x50\x50\x50\x50'), bytearray(b'\x04\xF9\x08\xE9\x0F\xA0\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0C\x7A\x0C\xB7\x06\x49\x50\x50\x50\x50'), bytearray(b'\x10\xCC\x09\xF7\x13\x7A\x50\x50\x50\x50'), bytearray(b'\x04\xEF\x06\xC9\x07\x37\x50\x50\x50\x50'), bytearray(b'\x08\xBE\x0B\xD8\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x08\x71\x06\xC5\x12\xA0\x50\x50\x50\x50'), bytearray(b'\x13\x48\x0C\xDA\x2D\xD6\x0E\xE9\x50\x50'), bytearray(b'\x06\xC9\x19\x49\x2C\x96\x50\x50\x50\x50'), bytearray(b'\x06\x0A\x0C\xDA\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x05\x66\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x0B\xC4\x13\xA1\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x06\x6C\x06\x6C\x0D\x68\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0A\xD8\x0E\x6F\x12\x27\x50\x50\x50\x50'), bytearray(b'\x06\xA2\x09\xF7\x05\x3C\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x11\x1E\x0D\xE8\x0B\xAB\x06\xE3\x50\x50'), bytearray(b'\x0D\xE8\x0B\x29\x11\xA3\x50\x50\x50\x50'), bytearray(b'\x10\x05\x06\xE3\x11\x13\x10\x13\x50\x50'), bytearray(b'\x0C\xB4\x0B\xA3\x06\xC9\x50\x50\x50\x50'), bytearray(b'\x08\x36\x0B\x86\x08\x36\x0B\x86\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x08\xD5\x10\x13\x10\xD8\x50\x50\x50\x50'), bytearray(b'\x0B\x09\x11\xA3\x50\x50\x50\x50\x50\x50'), bytearray(b'\x09\x49\x07\x10\x50\x50\x50\x50\x50\x50'), bytearray(b'\x05\x66\x05\x66\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x05\x66\x0D\x79\x50\x50\x50\x50'), bytearray(b'\x05\x2E\x0F\xA7\x08\xE9\x12\x37\x50\x50'), bytearray(b'\x0C\xFA\x11\x10\x18\xCC\x19\x2F\x50\x50'), bytearray(b'\x0C\xFA\x11\x10\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x07\x6E\x06\xA2\x10\x08\x0D\x2A\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0A\x63\x0A\x8C\x13\xA1\x50\x50\x50\x50'), bytearray(b'\x0A\x8C\x13\xA1\x11\x2D\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x09\xB2\x0C\x9B\x50\x50\x50\x50'), bytearray(b'\x0C\x08\x12\xCA\x0C\x9B\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x0B\x81\x06\xC5\x50\x50\x50\x50'), bytearray(b'\x0B\x81\x06\xC5\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0B\xD8\x0D\x9B\x50\x50'), bytearray(b'\x0D\x69\x07\x90\x0D\x3A\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x0E\xCB\x0F\xA7\x50\x50\x50\x50'), bytearray(b'\x07\x90\x05\x7D\x0F\xD6\x50\x50\x50\x50'), bytearray(b'\x09\x71\x0F\xA7\x13\x37\x0C\x34\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x06\x9B\x08\xBE\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x12\x0D\x09\xB2\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0A\x78\x0D\x69\x08\xD2\x50\x50\x50\x50'), bytearray(b'\x09\xB2\x0B\x36\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0B\x04\x1C\xA0\x08\xD2\x50\x50\x50\x50'), bytearray(b'\x0D\xCD\x09\xB2\x0C\x34\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x0E\xCF\x09\x0F\x50\x50\x50\x50\x50\x50'), bytearray(b'\x19\x3B\x0C\x65\x05\xD9\x50\x50\x50\x50'), bytearray(b'\x06\x6C\x06\x6C\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x04\xF6\x11\x2D\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x0B\x82\x04\xEA\x12\xA3\x50\x50\x50\x50'), bytearray(b'\x0B\x3A\x06\xCA\x09\x6A\x50\x50\x50\x50'), bytearray(b'\x06\xC9\x0F\xAB\x09\x6A\x50\x50\x50\x50')]
engPMNames = [bytearray(b'\x91\x87\x98\x83\x8E\x8D\x50\x50\x50\x50'), bytearray(b'\x91\x87\x98\x83\x8E\x8D\x50\x50\x50\x50'), bytearray(b'\x8A\x80\x8D\x86\x80\x92\x8A\x87\x80\x8D'), bytearray(b'\x8D\x88\x83\x8E\x91\x80\x8D\xEF\x50\x50'), bytearray(b'\x82\x8B\x84\x85\x80\x88\x91\x98\x50\x50'), bytearray(b'\x92\x8F\x84\x80\x91\x8E\x96\x50\x50\x50'), bytearray(b'\x95\x8E\x8B\x93\x8E\x91\x81\x50\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x8A\x88\x8D\x86\x50\x50'), bytearray(b'\x92\x8B\x8E\x96\x81\x91\x8E\x50\x50\x50'), bytearray(b'\x88\x95\x98\x92\x80\x94\x91\x50\x50\x50'), bytearray(b'\x84\x97\x84\x86\x86\x94\x93\x8E\x91\x50'), bytearray(b'\x8B\x88\x82\x8A\x88\x93\x94\x8D\x86\x50'), bytearray(b'\x84\x97\x84\x86\x86\x82\x94\x93\x84\x50'), bytearray(b'\x86\x91\x88\x8C\x84\x91\x50\x50\x50\x50'), bytearray(b'\x86\x84\x8D\x86\x80\x91\x50\x50\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x91\x80\x8D\xF5\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x90\x94\x84\x84\x8D\x50'), bytearray(b'\x82\x94\x81\x8E\x8D\x84\x50\x50\x50\x50'), bytearray(b'\x91\x87\x98\x87\x8E\x91\x8D\x50\x50\x50'), bytearray(b'\x8B\x80\x8F\x91\x80\x92\x50\x50\x50\x50'), bytearray(b'\x80\x91\x82\x80\x8D\x88\x8D\x84\x50\x50'), bytearray(b'\x8C\x84\x96\x50\x50\x50\x50\x50\x50\x50'), bytearray(b'\x86\x98\x80\x91\x80\x83\x8E\x92\x50\x50'), bytearray(b'\x92\x87\x84\x8B\x8B\x83\x84\x91\x50\x50'), bytearray(b'\x93\x84\x8D\x93\x80\x82\x8E\x8E\x8B\x50'), bytearray(b'\x86\x80\x92\x93\x8B\x98\x50\x50\x50\x50'), bytearray(b'\x92\x82\x98\x93\x87\x84\x91\x50\x50\x50'), bytearray(b'\x92\x93\x80\x91\x98\x94\x50\x50\x50\x50'), bytearray(b'\x81\x8B\x80\x92\x93\x8E\x88\x92\x84\x50'), bytearray(b'\x8F\x88\x8D\x92\x88\x91\x50\x50\x50\x50'), bytearray(b'\x93\x80\x8D\x86\x84\x8B\x80\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x86\x91\x8E\x96\x8B\x88\x93\x87\x84\x50'), bytearray(b'\x8E\x8D\x88\x97\x50\x50\x50\x50\x50\x50'), bytearray(b'\x85\x84\x80\x91\x8E\x96\x50\x50\x50\x50'), bytearray(b'\x8F\x88\x83\x86\x84\x98\x50\x50\x50\x50'), bytearray(b'\x92\x8B\x8E\x96\x8F\x8E\x8A\x84\x50\x50'), bytearray(b'\x8A\x80\x83\x80\x81\x91\x80\x50\x50\x50'), bytearray(b'\x86\x91\x80\x95\x84\x8B\x84\x91\x50\x50'), bytearray(b'\x82\x87\x80\x8D\x92\x84\x98\x50\x50\x50'), bytearray(b'\x8C\x80\x82\x87\x8E\x8A\x84\x50\x50\x50'), bytearray(b'\x8C\x91\xE8\x8C\x88\x8C\x84\x50\x50\x50'), bytearray(b'\x87\x88\x93\x8C\x8E\x8D\x8B\x84\x84\x50'), bytearray(b'\x87\x88\x93\x8C\x8E\x8D\x82\x87\x80\x8D'), bytearray(b'\x80\x91\x81\x8E\x8A\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x80\x91\x80\x92\x84\x82\x93\x50\x50'), bytearray(b'\x8F\x92\x98\x83\x94\x82\x8A\x50\x50\x50'), bytearray(b'\x83\x91\x8E\x96\x99\x84\x84\x50\x50\x50'), bytearray(b'\x86\x8E\x8B\x84\x8C\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x80\x86\x8C\x80\x91\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x84\x8B\x84\x82\x93\x80\x81\x94\x99\x99'), bytearray(b'\x8C\x80\x86\x8D\x84\x93\x8E\x8D\x50\x50'), bytearray(b'\x8A\x8E\x85\x85\x88\x8D\x86\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x80\x8D\x8A\x84\x98\x50\x50\x50\x50'), bytearray(b'\x92\x84\x84\x8B\x50\x50\x50\x50\x50\x50'), bytearray(b'\x83\x88\x86\x8B\x84\x93\x93\x50\x50\x50'), bytearray(b'\x93\x80\x94\x91\x8E\x92\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x85\x80\x91\x85\x84\x93\x82\x87\xbb\x50'), bytearray(b'\x95\x84\x8D\x8E\x8D\x80\x93\x50\x50\x50'), bytearray(b'\x83\x91\x80\x86\x8E\x8D\x88\x93\x84\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x83\x8E\x83\x94\x8E\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x8E\x8B\x88\x96\x80\x86\x50\x50\x50'), bytearray(b'\x89\x98\x8D\x97\x50\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x8E\x8B\x93\x91\x84\x92\x50\x50\x50'), bytearray(b'\x80\x91\x93\x88\x82\x94\x8D\x8E\x50\x50'), bytearray(b'\x99\x80\x8F\x83\x8E\x92\x50\x50\x50\x50'), bytearray(b'\x83\x88\x93\x93\x8E\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x84\x8E\x96\x93\x87\x50\x50\x50\x50'), bytearray(b'\x8A\x91\x80\x81\x81\x98\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x95\x94\x8B\x8F\x88\x97\x50\x50\x50\x50'), bytearray(b'\x8D\x88\x8D\x84\x93\x80\x8B\x84\x92\x50'), bytearray(b'\x8F\x88\x8A\x80\x82\x87\x94\x50\x50\x50'), bytearray(b'\x91\x80\x88\x82\x87\x94\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x83\x91\x80\x93\x88\x8D\x88\x50\x50\x50'), bytearray(b'\x83\x91\x80\x86\x8E\x8D\x80\x88\x91\x50'), bytearray(b'\x8A\x80\x81\x94\x93\x8E\x50\x50\x50\x50'), bytearray(b'\x8A\x80\x81\x94\x93\x8E\x8F\x92\x50\x50'), bytearray(b'\x87\x8E\x91\x92\x84\x80\x50\x50\x50\x50'), bytearray(b'\x92\x84\x80\x83\x91\x80\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x92\x80\x8D\x83\x92\x87\x91\x84\x96\x50'), bytearray(b'\x92\x80\x8D\x83\x92\x8B\x80\x92\x87\x50'), bytearray(b'\x8E\x8C\x80\x8D\x98\x93\x84\x50\x50\x50'), bytearray(b'\x8E\x8C\x80\x92\x93\x80\x91\x50\x50\x50'), bytearray(b'\x89\x88\x86\x86\x8B\x98\x8F\x94\x85\x85'), bytearray(b'\x96\x88\x86\x86\x8B\x98\x93\x94\x85\x85'), bytearray(b'\x84\x84\x95\x84\x84\x50\x50\x50\x50\x50'), bytearray(b'\x85\x8B\x80\x91\x84\x8E\x8D\x50\x50\x50'), bytearray(b'\x89\x8E\x8B\x93\x84\x8E\x8D\x50\x50\x50'), bytearray(b'\x95\x80\x8F\x8E\x91\x84\x8E\x8D\x50\x50'), bytearray(b'\x8C\x80\x82\x87\x8E\x8F\x50\x50\x50\x50'), bytearray(b'\x99\x94\x81\x80\x93\x50\x50\x50\x50\x50'), bytearray(b'\x84\x8A\x80\x8D\x92\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x80\x91\x80\x92\x50\x50\x50\x50\x50'), bytearray(b'\x8F\x8E\x8B\x88\x96\x87\x88\x91\x8B\x50'), bytearray(b'\x8F\x8E\x8B\x88\x96\x91\x80\x93\x87\x50'), bytearray(b'\x96\x84\x84\x83\x8B\x84\x50\x50\x50\x50'), bytearray(b'\x8A\x80\x8A\x94\x8D\x80\x50\x50\x50\x50'), bytearray(b'\x81\x84\x84\x83\x91\x88\x8B\x8B\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x83\x8E\x83\x91\x88\x8E\x50\x50\x50\x50'), bytearray(b'\x8F\x91\x88\x8C\x84\x80\x8F\x84\x50\x50'), bytearray(b'\x83\x94\x86\x93\x91\x88\x8E\x50\x50\x50'), bytearray(b'\x95\x84\x8D\x8E\x8C\x8E\x93\x87\x50\x50'), bytearray(b'\x83\x84\x96\x86\x8E\x8D\x86\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x82\x80\x93\x84\x91\x8F\x88\x84\x50\x50'), bytearray(b'\x8C\x84\x93\x80\x8F\x8E\x83\x50\x50\x50'), bytearray(b'\x81\x94\x93\x93\x84\x91\x85\x91\x84\x84'), bytearray(b'\x8C\x80\x82\x87\x80\x8C\x8F\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x86\x8E\x8B\x83\x94\x82\x8A\x50\x50\x50'), bytearray(b'\x87\x98\x8F\x8D\x8E\x50\x50\x50\x50\x50'), bytearray(b'\x86\x8E\x8B\x81\x80\x93\x50\x50\x50\x50'), bytearray(b'\x8C\x84\x96\x93\x96\x8E\x50\x50\x50\x50'), bytearray(b'\x92\x8D\x8E\x91\x8B\x80\x97\x50\x50\x50'), bytearray(b'\x8C\x80\x86\x88\x8A\x80\x91\x8F\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x94\x8A\x50\x50\x50\x50\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8A\x88\x8D\x86\x8B\x84\x91\x50\x50\x50'), bytearray(b'\x82\x8B\x8E\x98\x92\x93\x84\x91\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x84\x8B\x84\x82\x93\x91\x8E\x83\x84\x50'), bytearray(b'\x82\x8B\x84\x85\x80\x81\x8B\x84\x50\x50'), bytearray(b'\x96\x84\x84\x99\x88\x8D\x86\x50\x50\x50'), bytearray(b'\x8F\x84\x91\x92\x88\x80\x8D\x50\x50\x50'), bytearray(b'\x8C\x80\x91\x8E\x96\x80\x8A\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x87\x80\x94\x8D\x93\x84\x91\x50\x50\x50'), bytearray(b'\x80\x81\x91\x80\x50\x50\x50\x50\x50\x50'), bytearray(b'\x80\x8B\x80\x8A\x80\x99\x80\x8C\x50\x50'), bytearray(b'\x8F\x88\x83\x86\x84\x8E\x93\x93\x8E\x50'), bytearray(b'\x8F\x88\x83\x86\x84\x8E\x93\x50\x50\x50'), bytearray(b'\x92\x93\x80\x91\x8C\x88\x84\x50\x50\x50'), bytearray(b'\x81\x94\x8B\x81\x80\x92\x80\x94\x91\x50'), bytearray(b'\x95\x84\x8D\x94\x92\x80\x94\x91\x50\x50'), bytearray(b'\x93\x84\x8D\x93\x80\x82\x91\x94\x84\x8B'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x86\x8E\x8B\x83\x84\x84\x8D\x50\x50\x50'), bytearray(b'\x92\x84\x80\x8A\x88\x8D\x86\x50\x50\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8F\x8E\x8D\x98\x93\x80\x50\x50\x50\x50'), bytearray(b'\x91\x80\x8F\x88\x83\x80\x92\x87\x50\x50'), bytearray(b'\x91\x80\x93\x93\x80\x93\x80\x50\x50\x50'), bytearray(b'\x91\x80\x93\x88\x82\x80\x93\x84\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x91\x88\x8D\x8E\x50\x50'), bytearray(b'\x8D\x88\x83\x8E\x91\x88\x8D\x80\x50\x50'), bytearray(b'\x86\x84\x8E\x83\x94\x83\x84\x50\x50\x50'), bytearray(b'\x8F\x8E\x91\x98\x86\x8E\x8D\x50\x50\x50'), bytearray(b'\x80\x84\x91\x8E\x83\x80\x82\x93\x98\x8B'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x80\x86\x8D\x84\x8C\x88\x93\x84\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x82\x87\x80\x91\x8C\x80\x8D\x83\x84\x91'), bytearray(b'\x92\x90\x94\x88\x91\x93\x8B\x84\x50\x50'), bytearray(b'\x82\x87\x80\x91\x8C\x84\x8B\x84\x8E\x8D'), bytearray(b'\x96\x80\x91\x93\x8E\x91\x93\x8B\x84\x50'), bytearray(b'\x82\x87\x80\x91\x88\x99\x80\x91\x83\x50'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8C\x88\x92\x92\x88\x8D\x86\x8D\x8E\xE8'), bytearray(b'\x8E\x83\x83\x88\x92\x87\x50\x50\x50\x50'), bytearray(b'\x86\x8B\x8E\x8E\x8C\x50\x50\x50\x50\x50'), bytearray(b'\x95\x88\x8B\x84\x8F\x8B\x94\x8C\x84\x50'), bytearray(b'\x81\x84\x8B\x8B\x92\x8F\x91\x8E\x94\x93'), bytearray(b'\x96\x84\x84\x8F\x88\x8D\x81\x84\x8B\x8B'), bytearray(b'\x95\x88\x82\x93\x91\x84\x84\x81\x84\x8B')]
root = tk.Tk()
root.withdraw()

defaultOTname = bytearray(b'\x80\x92\x87\x50\x50\x50\x50\x50\x50\x50\x50')
defaultPMname = bytearray(b'\x86\x80\x91\x98\x50\x50\x50\x50\x50\x50\x50')

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
        # print(jpnSaveArray[jpOffset + i])
        usSaveArray[usOffset + i] = jpnSaveArray[jpOffset + i]

def copyArrayByLength(jpOffset,usOffset,length):
    for i in range(length):
        usSaveArray[usOffset + i] = jpnSaveArray[jpOffset + i]

def calculateChecksum(start,end):
    array = []
    for i in range(start,end + 1):
        array.append(usSaveArray[i])
    checksum =(~(sum(array) & 0xFF)) & 0xFF
    return checksum

def setChecksum(start,end,setOffset,desc):
    checksum = calculateChecksum(start,end)
    print(desc + ' Checksum 是：' + hex(checksum))
    usSaveArray[setOffset] = checksum
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
            setChecksum(boxOffset,boxOffset + 0x462,singleBoxChecksumOffset,'盒子 ' + str(i + 1 + 6 * k))
        setChecksum(offset,offset + 0x1A4B,offset + 0x1A4C,'Bank ' + str(1 + k))
        # setChecksum(offset,offset + 0x15EA,offset + 0x1A4C,'Bank ' + str(1 + k))

extraBox = []
def parseJPNBoxData(offset):
    speciesIDs = []
    OTNames = []
    pkmnDatas = []
    pkmnCount = jpnSaveArray[offset]
    if pkmnCount > 30:
        pkmnCount = 0
    for i in range(pkmnCount):
        speciesIDs.append(jpnSaveArray[offset + 1 + i])

        pkmnData = []
        for k in range(33):
            pkmnData.append(jpnSaveArray[offset + 0x20 + k + i * 33])
        pkmnDatas.append(pkmnData)

        OTName = []
        for j in range(6):
            OTName.append(jpnSaveArray[offset + 0x3FE + j + i * 6])
        OTNames.append(OTName)

    outputBox = []
    for i in range(pkmnCount):
        tmpPKMN = PokemonData()
        tmpPKMN.speciesID = speciesIDs[i]
        tmpPKMN.otName = OTNames[i]
        tmpPKMN.pkmnData = pkmnDatas[i]
        if i <= 19:
            outputBox.append(tmpPKMN)
        else:
            extraBox.append(tmpPKMN)
    return outputBox

def writeBoxData(boxData,offset):
    global option
    tmpBoxData = bytearray(0x462)
    tmpBoxData[0] = len(boxData)
    writeValueAt(tmpBoxData, 1, 0xFF, 21)
    for i in range(len(boxData)):
        currPKMN:PokemonData = boxData[i]
        tmpBoxData[1 + i] = currPKMN.speciesID
        writeArrayAt(tmpBoxData, 0x16 + 33 * i,currPKMN.pkmnData)
        writeArrayAt(tmpBoxData, 0x2AA + 0xB * i,defaultOTname)
        if option != 2:
            writeArrayAt(tmpBoxData, 0x386 + 0xB * i,chsPMNames[currPKMN.speciesID])
        else:
            writeArrayAt(tmpBoxData, 0x386 + 0xB * i,engPMNames[currPKMN.speciesID])
    writeArrayAt(usSaveArray,offset,tmpBoxData)

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
    
file_path = os.path.abspath(os.path.dirname(__file__))
print()
print(' 宝可梦第一世代 日版存档 -> 美版存档 转换工具(测试版)')
print('日文版 /「红怪兽」/「黄怪兽」汉化版存档转美版/美版汉化存档')
print('-------------------------------------------------------------')
print('由于新版汉化版都是基于美版汉化，无法直接读取日文版存档，故开发此工具将日版存档转换成美版存档')
print()
print('！！！在开始之前，请确认要转换的存档已经在精灵中心门口的垫子处存档，若死机请在其他地方多次尝试')
print('！！！在确认新版存档能使用前请注意备份存档！！！')
print('！！！不保证 100% 可用！！！宝可梦昵称会被还原成默认名字！')
print('！！！主角/所有宝可梦初训家会被重命名为：ASH，劲敌会被重命名为：GARY！！！')
print('！！！前8个盒子中的前20只宝可梦会被原样复制，后10只宝可梦会按顺序放入9-12号盒子！！！')
print('！！！不会迁移名人堂数据！！！')
print()
print('当前目录：' + file_path)
print('即将打开选择文件对话框')
print('按 Enter/Return 键继续')
print('若按下键盘后没反应，请先用鼠标点击窗口，然后再按下键盘')
dummy = input('')
path = filedialog.askopenfilename(title="选择 .sav 文件", filetypes=(("sav 文件", "*.sav"), ("All files", "*.*")))

print('请选择新的宝可梦名称语言')
print('1.中文')
print('2.英文')
print('输入数字，按回车确认')
option = int(input(''))

jpnSaveArray = readFileAsByteArray(path)
usSaveArray = bytearray(len(jpnSaveArray))

writeArrayAt(usSaveArray,0x2598,defaultOTname)
copyArray(0x259E,0x25A3,0x25F6)
writeArrayAt(usSaveArray,0x25F6,defaultPMname)
copyArray(0x25F7,0x2601,0x2B33)
copyArray(0x2CA0,0x2CED,0x2CF5)
dayCareSpecies = jpnSaveArray[0x2CB4]
if option != 2:
    writeArrayAt(usSaveArray,0x2CF5,chsPMNames[dayCareSpecies])
else:
    writeArrayAt(usSaveArray,0x2CF5,engPMNames[dayCareSpecies])
writeArrayAt(usSaveArray,0x2D00,defaultOTname)
copyArray(0x2CB4,0x2D0B,0x2F2C)
copyArray(0x2C98,0x2CE5,0x2CED)

copyArray(0x2C97,0x2CE4,0x2CE5)

copyArrayByLength(0x2ED5,0x2F2C,0x110)

index = 0x2F2C + 0x110
for i in range(6):
    writeArrayAt(usSaveArray,index + i * 0xB ,defaultOTname)
index = 0x2F2C + 0x152
for i in range(6):
    if usSaveArray[0x2F2C + 1 + i] <= 190:
        if option != 2:
            writeArrayAt(usSaveArray,index + i * 0xB ,chsPMNames[usSaveArray[0x2F2C + 1 + i]])
        else:
            writeArrayAt(usSaveArray,index + i * 0xB ,engPMNames[usSaveArray[0x2F2C + 1 + i]])

currentPKMNBox = parseJPNBoxData(0x302D)
writeBoxData(currentPKMNBox,0x30C0)
setChecksum(0x2598,0x3522,0x3523,'Main Data')


boxOffsets = getBoxOffsets()
for boxno in range(8):
    currentPKMNBox = parseJPNBoxData(boxOffsets[1][boxno])
    writeBoxData(currentPKMNBox,boxOffsets[0][boxno])

for boxno in range(8,12):
    count = 0
    tmpPKMNBox = []
    # print(extraBox)
    while len(extraBox)!= 0 and count < 20:
        tmpPKMNBox.append(extraBox.pop(0))
        count += 1
    writeBoxData(tmpPKMNBox,boxOffsets[0][boxno])



setBoxChecksums()


save_path = filedialog.asksaveasfilename(title="请选择保存位置", defaultextension=".sav", filetypes=(("sav 文件", "*.sav"), ("All files", "*.*")))
# writeByteArrayAsFile('red.en.sav',usSaveArray)
writeByteArrayAsFile(save_path,usSaveArray)
# writeByteArrayAsFile(os.path.join(file_path,'YellowNew.sav'),newArray)
print('新存档已经写入到：')
print(save_path)
print()
print('-------------------------------------------------------------')
print('如果转换后在新版中启动死机')
print('请在 CKN 版本中携带会飞翔的宝可梦，前往精灵中心门口（室外）然后存档')
print('然后再重新执行本操作，进入游戏后使用飞翔前往其他地方即可')

if sys.platform == 'win32':
    print('按 Enter/Return 键关闭')
    dummy2 = input('')