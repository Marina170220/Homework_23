def create_response(data, cmd, value):
    """
    Принимает 5 параметров из запроса: где 1, 2, 3, 4 - запрос, 5-ый - имя файла, обрабатывает файл,
    следуя написанному запросу, и возвращает ответ клиенту.
    :param data: файл с записями запросов сервера.
    :param cmd: запрос означающий, какая команда будет выполнена.
    :param value: аргумент, с которым выполнится команда cmd.
    :return: Ответ клиенту, содержащий обработанные в соответствии с запросом данные из файла.
    """
    result = map(lambda x: x.strip(), data)

    match cmd:
        case 'filter':
            result = filter(lambda x, txt=value: txt in x, result)
        case 'map':
            result = map(lambda x, idx=int(value): x.split(" ")[idx], result)
        case 'unique':
            result = set(result)
        case 'sort':
            reverse = value == 'desc'
            result = sorted(result, reverse=reverse)
        case 'limit':
            result = list(result)[:int(value)]
    return result
