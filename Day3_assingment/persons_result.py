def person_result(dictionary):
    for i in dictionary:
        if i['result'] == "pass":
            print(i['name'])


person_result([{'id': 1, 'result': "pass", 'name': 'Ramesh'},
               {'id': 2, 'result': "pass", 'name': 'Suresh'},
               {'id': 3, 'result': "fail", 'name': 'Alex'}])
