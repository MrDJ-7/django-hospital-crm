from .models import Cards, Patient


class Card_service:
    def get_all_doctors():
        return Cards.objects.all()

    def get_all_doctors_map():
        doctors_l = Cards.get_all_doctors()
        doctors_list = [
            {"id": doctors_temp.id, "name": doctors_temp.name}
            for doctors_temp in doctors_l
        ]
        return doctors_list

    def get_doctor(doctor_id):
        try:
            doctor_entry = Cards.objects.get(pk=doctor_id)
        except:
            raise ("Doctor id not found!")

        return doctor_entry

    def doctor_exists(doctor_name, doctor_age, doctor_adress):
        # django.db.models.query.QuerySet'

        if Cards.objects.all().filter(
            name=doctor_name,
            age=doctor_age,
            address=doctor_adress,
        ):
            return True
        else:
            return False
        # return type(doctors)
        # print(type(doctors))

    def add_doctor_data(doctor_name, doctor_age, doctor_address, doctor_salary):
        doctor = Cards(
            name=doctor_name,
            age=doctor_age,
            address=doctor_address,
            salary=doctor_salary,
        )
        doctor.save()
