import tabula
import fitz
from fastapi import HTTPException

import fitz
import tabula
import uuid
import os

def parsePdf(pdf_bin: object):
    try:
        pdf = fitz.open(None, pdf_bin, "pdf")
    except:
        raise HTTPException(status_code=400, detail="Not a valid pdf")
    
    nameid = str(uuid.uuid4())
    
    pdf.save(f"./temp/{nameid}.pdf")
    pdf.close()
    tables = tabula.read_pdf(f"./temp/{nameid}.pdf", pages="all")
    os.remove(f"./temp/{nameid}.pdf")

    for table in tables:
        columns = table.columns
        table[columns[3]] = table[columns[3]].fillna(0)
        table[columns[2]] = table[columns[2]].fillna("")
        table[columns[1]] = table[columns[1]].fillna("")
        table[columns[0]] = table[columns[0]].fillna(-1)

    return tables

#    tables = tabula.read_pdf(pdf_bin, pages="all")
#    return tables