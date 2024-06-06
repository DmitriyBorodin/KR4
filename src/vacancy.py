from src.hhparser import HHVacancyGetter


class Vacancy:
    name: str
    url: str
    salary: int
    schedule: str
    area: str
    currency: str

    def __init__(self, name, url, salary, schedule, area, currency):
        self.name = name

        if url[:8] != 'https://':
            raise ValueError("Ссылка должна начинаться с https://")
        self.url = url
        self.salary = salary
        self.schedule = schedule
        self.area = area
        self.currency = currency

    def __str__(self):
        return (f"Название вакансии: {self.name}\n"
                f"Занятость: {self.schedule}\n"
                f"Зарплата: {self.salary}\n"
                f"Валюта: {self.currency}\n"
                f"Город: {self.area}\n"
                f"Ссылка: {self.url}\n")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            if self.salary > other.salary:
                return True
            else:
                return False
        raise TypeError("Вакансии можно сравнивать только с другими вакансиями")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            if self.salary < other.salary:
                return True
            else:
                return False
        raise TypeError("Вакансии можно сравнивать только с другими вакансиями")

    @classmethod
    def new_vacancy(cls, vacancy):
        vac_schedule = (f"{vacancy['employment']['name']},"
                        f" {vacancy['schedule']['name']}")

        vac_salary = 0
        if not vacancy.get('salary'):
            vac_salary = 0
        elif vacancy['salary']['to']:
            vac_salary = int(vacancy['salary']['to'])

        vac_curr = 'Не указана'
        if vacancy.get('salary'):
            vac_curr = vacancy['salary']['currency']

        # if not vacancy.get('salary'):
        #     vac_salary = 'ЗП не указана'
        # elif vacancy['salary']['from']:
        #     vac_salary = f"{vacancy['salary']['from']} - {vacancy['salary']['to']}{vacancy['salary']['currency']}"
        # elif vacancy['salary']['to']:
        #     vac_salary = f"{vacancy['salary']['to']}{vacancy['salary']['currency']}"

        return cls(vacancy['name'], vacancy['alternate_url'],
                   vac_salary, vac_schedule, vacancy['area']['name'],
                   vac_curr)


if __name__ == "__main__":
    get_vac = HHVacancyGetter('Python')
    a = get_vac.get_vacancies()

    vac1 = Vacancy.new_vacancy(a["items"][1])
    vac2 = Vacancy.new_vacancy(a["items"][9])
    print(vac1)
    print(vac2)

    print(vac1 > vac2)


