class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.photo_le_name = photo_le_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_le_ext(self):
        if str(self.photo_le_name).count('.') != 0:
            photo_type = str(self.photo_le_name).split('.')
        else:
            photo_type = 'Название файла с фото указано без разрешения'
        return photo_type[-1]


class Car(Carbase):
    def __init__(self, car_type, photo_le_name, brand, carrying, passengers_seats_count):
        Carbase.__init__(self, car_type, photo_le_name, brand, carrying)
        self.passengers_seats_count = passengers_seats_count

    def __repr__(self):
        return self.car_type

class Truck(Carbase):
    def __init__(self, car_type, photo_le_name, brand, carrying, body_whl):
        Carbase.__init__(self, car_type, photo_le_name, brand, carrying)
        self.body_whl = body_whl
        if self.body_whl != '':
            whl = self.body_whl.split('x')
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])
        else:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0

    def __repr__(self):
        return self.car_type


class Specmachine(Carbase):
    def __init__(self, car_type, photo_le_name, brand, carrying, extra):
        Carbase.__init__(self, car_type, photo_le_name, brand, carrying)
        self.extra = extra

    def __repr__(self):
        return self.car_type


def get_car_list(filename):
    car_list = []
    car_list1 = []
    types = ['car', 'truck', 'spec_machine']
    with open(filename, 'r', encoding='utf-8') as north:
        for line in north:
            if line.count(';') == 6:
                for i in types:
                    if i == line.split(';')[0]:
                        car_list1.append(line.split(';'))
                        break
                    else:
                        pass
    for i in car_list1:
        if i[-1] != '\n':
            i[-1] = i[-1][:-1]
    for i in car_list1:
        if i[0] == 'car':
            obj = Car(i[0], i[3], i[1], i[5], i[2])
            car_list.append(obj)
        elif i[0] == 'truck':
            obj = Truck(i[0], i[3], i[1], i[5], i[4])
            car_list.append(obj)
        elif i[0] == 'spec_machine':
            obj = Specmachine(i[0], i[3], i[1], i[5], i[6])
            car_list.append(obj)
    return car_list


def main():
    get_car_list('solution.txt')

if __name__ == '__main__':
    main()
