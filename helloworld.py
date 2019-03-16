from bs4 import BeautifulSoup
import pandas as pd
course = ['医学伦理学', '医学统计学', '循证医学', '感官系统疾病', '流行病学', '现场调查与信息处理实验',
          '血液及免疫系统疾病', '预防医学']
for sub in course:
    sensory_sys_file = open(sub+'.html', "r")
    sensory_sys = sensory_sys_file.read()
    soup = BeautifulSoup(sensory_sys, 'html.parser')
    table = soup.find_all("table", attrs={"id":"myTable"})[0]
    rows = table.find_all("tr")
    data = {'Subject': [],
            'Start Date': [],
            'Start Time': [],
            'End Date': [],
            'End Time': [],
            'Description': []
            }
    column = ''
    subject = ''
    date = ''
    st = ['',
          '8:30',
          '9:15',
          '10:05',
          '10:55',
          '11:40',
          '12:20',
          '13:20',
          '14:00',
          '14:45',
          '15:35',
          '16:20',
          '17:00',
          '17:40',
          '18:20',
          '19:00',
          '19:45',
          '20:30',
          '21:10']

    et = ['',
          '9:10',
          '9:55',
          '10:45',
          '11:35',
          '12:20',
          '13:00',
          '14:00',
          '14:40',
          '15:25',
          '16:15',
          '17:00',
          '17:40',
          '18:20',
          '19:00',
          '19:40',
          '20:25',
          '21:10',
          '21:50']

    for row in rows:
        columns = row.find_all("td")
        if len(columns) != 0:
            for x in range(len(columns)):
                if x == 2:
                    column = str(columns[2].get_text()[:10])
                    date = column
                    data['Start Date'].append(date)
                    data['End Date'].append(date)
                if x == 5:
                    column = str(columns[5])
                    subject = column.split('\n	')[0][4:]
                    data['Subject'].append('[' + sub +'] ' + subject)
                if x == 6:
                    column = int(columns[6].get_text())
                    lec_num = column
                if x == 9:
                    column = str(columns[9])
                    description = str(columns[9].get_text())
                    data['Description'].append(description)
                if x == 3:
                    column = str(columns[3].get_text())
                    if column.find('-') != -1:
                        start_lecture = column.split('-')[0]
                        end_lecture = column.split('-')[1]
                    else:
                        start_lecture = column
                        end_lecture = column
                    start_time = st[int(start_lecture)]
                    end_time = et[int(end_lecture)]

                    data['Start Time'].append(start_time)
                    data['End Time'].append(end_time)

    print(data)

    export = pd.DataFrame(data).to_csv(sub +'.csv', encoding="utf-8")

print("Done! you can added the csv into Google Calendar")