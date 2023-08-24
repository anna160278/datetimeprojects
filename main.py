from datetime import datetime

with open('diary.txt', encoding='UTF8') as f:
    records = f.read().split('\n\n')

for i in range(len(records)):
    records[i] = [records[i][:records[i].find('\n')], records[i][records[i].find('\n') + 1:]]
    records[i][0] = datetime.strptime(records[i][0], '%d.%m.%Y; %H:%M')

records = sorted(records, key=lambda x: x[0])
for line in records:
    print(datetime.strftime(line[0], '%d.%m.%Y; %H:%M') + '\n' + line[1] + '\n')