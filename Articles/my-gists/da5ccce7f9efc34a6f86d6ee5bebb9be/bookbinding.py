#!/usr/bin/env python3

import sys
import PyPDF2

output_name = sys.argv[1]  # 出力するPDFファイル名

front_cover = sys.argv[2]  # 表の表紙のPDFファイル名
inner_cover = sys.argv[3]  # 内表紙のPDFファイル名
book_body   = sys.argv[4]  # 文書本体のPDFファイル名
back_cover  = sys.argv[5]  # 裏の表紙のPDFファイル名

with open(front_cover, mode='rb') as fc, \
     open(inner_cover, mode='rb') as ic, \
     open(book_body, mode='rb') as bb, \
     open(back_cover, mode='rb') as bc:
    front_reader = PyPDF2.PdfFileReader(fc)
    inner_reader = PyPDF2.PdfFileReader(ic)
    body_reader  = PyPDF2.PdfFileReader(bb)
    back_reader  = PyPDF2.PdfFileReader(bc)
    writer       = PyPDF2.PdfFileWriter()

    fc_page = front_reader.getPage(0)
    print("Add Front Cover %s"%(front_cover))
    writer.addPage(fc_page)
    writer.addBlankPage()

    ic_page = inner_reader.getPage(0)
    print("Add Inner Cover %s"%(inner_cover))
    writer.addPage(ic_page)

    for i in range(1, body_reader.numPages):
        page = body_reader.getPage(i)
        print("Add page %d"%(i+1))
        writer.addPage(page)

    if body_reader.numPages % 2:
        writer.addBlankPage()

    bc_page = back_reader.getPage(0)
    print("Add Back Cover %s"%(back_cover))
    writer.addBlankPage()
    writer.addPage(bc_page)

    with open(output_name, mode='wb') as output:
        writer.write(output)
