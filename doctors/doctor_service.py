from .models import Doctors


class Doctor_service:
    def get_all_doctors():
        return Doctors.objects.all()

    def get_all_doctors_map():
        doctors_l = Doctor_service.get_all_doctors()
        doctors_list = [
            {"id": doctors_temp.id, "name": doctors_temp.name}
            for doctors_temp in doctors_l
        ]
        return doctors_list

    def get_doctor(doctor_id):
        try:
            doctor_entry = Doctors.objects.get(pk=doctor_id)
        except:
            raise ("Doctor id not found!")

        return doctor_entry

    def doctor_exists(doctor_name, doctor_age, doctor_adress):
        # django.db.models.query.QuerySet'

        if Doctors.objects.all().filter(
            name=doctor_name, age=doctor_age, address=doctor_adress
        ):
            return True
        else:
            return False

        # return type(doctors)
        # print(type(doctors))


# qwa = Doctor_service
# qwa.doctor_exists("carl", 20, "Grow street 201")
#
