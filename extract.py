#!/usr/bin/env python
# encoding: utf-8

import xlrd

book = xlrd.open_workbook('Workbook1.xlsx');
sh = book.sheet_by_index(0)
sql = "INSERT INTO milestone (country, indicator, milestone, quarter, audience, status, alerts, recommendation, agreements, activitypoa) values ('{country}', '{indicator}', '{milestone}', '{quarter}', '{audience}', '{status}', '{alerts}', '{recommendation}', '{agreements}', '{activitypoa}');"
line = 0
for rx in range(sh.nrows):
	text = sh.row(rx)
	pais = sh.cell_value(line,0).encode('utf-8')
	indicator = sh.cell_value(line,1).encode('utf-8')
	milestone = sh.cell_value(line,2).encode('utf-8')
	quarter = sh.cell_value(line,3).encode('utf-8')
	audience = sh.cell_value(line,4).encode('utf-8')
	status = sh.cell_value(line,5).encode('utf-8')
	alerts = sh.cell_value(line,6).encode('utf-8')
	recommendation = sh.cell_value(line,7).encode('utf-8')
	agreements = sh.cell_value(line,8).encode('utf-8')
	activitypoa = str(sh.cell_value(line,9))
	line += 1
	print sql.replace('{country}', pais).replace('{indicator}', indicator).replace('{milestone}', milestone).replace('{quarter}', quarter).replace('{audience}', audience).replace('{status}', status).replace('{alerts}', alerts).replace('{recommendation}', recommendation).replace('{agreements}', agreements).replace('{activitypoa}', activitypoa)