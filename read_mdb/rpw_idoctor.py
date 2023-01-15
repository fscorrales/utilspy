#!/usr/bin/env python3
"""
Author: Fernando Corrales <fscorrales@gmail.com>
Purpose: Conversión de idoctor.mdb a xlsx
"""

import argparse
import os

import pandas as pd
import xlwings as xw
from sqlalchemy import MetaData, create_engine, engine, select


# --------------------------------------------------
def connect_mdb():
    """Inicializa la conexión a la BD de idoctor y refleja las tablas de la misma"""
    parser = argparse.ArgumentParser(description='Convert idoctor.mdb file to .xlsx')
    parser.add_argument('-f', '--file', metavar='Name', default='Fichas.mdb', help='.mdb File to convert')
    args = parser.parse_args()
    metadata = MetaData()
    connection_string = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=D:\Datos INVICO\Python INVICO\Lectura archivos\read_mdb"
        + "\\" + args.file +
        r";"
        r"ExtendedAnsiSQL=1;"
    )

    connection_url = engine.URL.create(
        "access+pyodbc",
        query={"odbc_connect": connection_string}
    )

    engine_mdb = create_engine(connection_url)
    metadata.reflect(bind=engine_mdb)
    return engine_mdb, metadata

# --------------------------------------------------
def get_tables():
    engine_mdb, metadata = connect_mdb()
    tables = {}
    for table_name in metadata.tables.keys():
        table = metadata.tables[table_name]
        s = select([table])
        if table_name != "HISTORIAL":
            tables[table_name] = pd.DataFrame(engine_mdb.execute(s).fetchall())
        else:
            tables['HIST'] = pd.DataFrame(engine_mdb.execute(s).fetchall())

    return tables

# --------------------------------------------------
def create_excel():
    tables = get_tables()
    print(tables.get("INGRESOS").head())
    nombre_archivo = "idoctor.xlsx"
    if os.path.exists(nombre_archivo):
        print(f'El archivo {nombre_archivo} ya existe en la carpeta. \n' + 
        'Si desea sobreescribir el archivo, deberá eliminarlo primero')
    else:
        wb = xw.Book()
        try:
            for k in tables.keys():
                if k != 'INGRESOS':
                    sheet = wb.sheets.add()
                    sheet.name = k
                    filas_blanco = 2
                    t = tables.get(k)
                    sheet.range(f'B{filas_blanco}').value = t
                    # sheet.range('A1').column_width = 5
                    # sheet.range('L1').column_width = 5
                    # sheet.range('M1').column_width = 5
                    # sheet.range('N1').column_width = 65
                    # sheet.range(f'J{filas_blanco + 1}:K{len(ppto_obras_siif) + filas_blanco}').number_format = '#,##0.00'
                    # #sheet.range(f'O{filas_blanco + 1}:Q{len(ppto_obras) + filas_blanco}').number_format = '#,##0.00'
                    table = sheet.tables.add(source=sheet[f'B{filas_blanco}'].expand(), name= k)
        finally:
            wb.save(nombre_archivo)
            wb.close()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    create_excel()


# --------------------------------------------------
if __name__ == '__main__':
    main()
