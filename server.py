from aiohttp import web
import xlrd
import json
datafile="D:\MIP\Manchester-housing.xlsx"
async def handle(request):      
    name = request.match_info.get('name', "World!")
    data=parseFile(datafile)
    json_string = json.dumps(data)
    text = "Hello, " + json_string
    print('received request, replying with "{}".'.format(text))
    return web.Response(text=text)

def parseFile(datafile):
    workbook=xlrd.open_workbook(datafile)
    sheet=workbook.sheet_by_name("Sheet1")

    data=[[sheet.cell_value(r,col)
            for col in range(sheet.ncols)]
                for r in range(sheet.nrows)]
    return data

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app, port=5858)