from task3.models import Fp_data
from task3.compareSave import validated_data_from_api


# update rows
def db_changed():
    list_of_changed_data = []
    updated_count = 0

    for my_api_data in validated_data_from_api():
        my_regNo = my_api_data.reg_no

        try:
            my_row = Fp_data.objects.get(reg_no=my_regNo)
            my_row_dict = my_row.__dict__
        except Fp_data.DoesNotExist:
            continue

        list_db = []
        list_api = []

        for key, value in my_row_dict.items():
            if not key.startswith('_'):
                list_db.append((key, value))

        for j in my_api_data:
            list_api.append(j)

        if list_db != list_api:
            list_of_changed_data.append(my_regNo)
            print(f"Updating reg_no: {my_regNo}")

            for i in range(len(list_db)):
                db_key, db_value = list_db[i]
                api_key, api_value = list_api[i]

                if db_key == api_key and db_value != api_value:
                    setattr(my_row, db_key, api_value)
                    print(f"Updated {db_key}: {db_value} -> {api_value}")

            my_row.save()
            updated_count += 1
            print('____________________________________________')

    print(f"Total rows updated: {updated_count}")
    return list_of_changed_data
