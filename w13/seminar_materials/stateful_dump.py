import pickle


class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

    def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "{}: {}".format(self.lineno, line)

    def __getstate__(self):
        # Копируем состояние объекта из self.__dict__, который
        # содержит все атрибуты. Всегда используйте dict.copy()
        # во избежании модификации состояния самого объекта.
        state = self.__dict__.copy()
        # Удаляем несериализуемые атрибуты.
        del state['file']
        return state

    def __setstate__(self, state):
        # Восстанавливаем атрибуты объекта.
        self.__dict__.update(state)
        # Восстанавливаем состояние открытого ранее файла. Для этого нам надо
        # заного открыть его и пропустить необходимое количество строк.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Создаем атрибут для file.
        self.file = file

if __name__ == "__main__":
    reader = TextReader('text_to_read.txt')
    print(reader.__dict__)
    dump = pickle.dumps(reader)
    with open('stateful_dump.pickle', 'wb') as f:
        f.write(dump)
    print(dump)
    reader_restored = pickle.loads(dump)
    print(reader_restored.__dict__)

