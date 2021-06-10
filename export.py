import sys
import ckanapi_exporter.exporter as exporter
csv_string = exporter.export('https://transportdata.be', 'columns.json')
sys.stdout.write(csv_string)