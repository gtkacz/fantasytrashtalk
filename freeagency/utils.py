import gspread

gc = gspread.service_account(filename='static/freeagency/docs/credentials.json')
sh = gc.open_by_key('1mpbT0im_4yjwhJ5HscqUdSqCqtMUI9oqqwY7aO5V38U')
worksheet = sh.sheet1
res = worksheet.get_all_records()

print(res)