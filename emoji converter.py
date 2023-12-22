greetings = input('->')
dic = {
    ':)':'😄',
    ':(': '😥'
}
if ':)' in greetings:
    print(greetings.replace(':)' , dic[':)']))
elif ':(' in greetings:
    print(greetings.replace(':(' , dic[':(']))
else:
    print(greetings)