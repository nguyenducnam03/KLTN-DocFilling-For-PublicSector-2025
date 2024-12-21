import pickle
import copy


def load_tagname_dict(save_path = 'tagname_dict.pkl'):
    with open(save_path, 'rb') as f:
        return pickle.load(f)

def sum_all_tag_names(tag_name_dict = None):
    if tag_name_dict is None:
        tag_name_dict = load_tagname_dict()
    list_count_tag_name = []
    for key in tag_name_dict.keys():
        type_form = tag_name_dict[key]
        total_count = 0
        for count in type_form.values():
            total_count += count
        list_count_tag_name.append(total_count)
    return tag_name_dict, list_count_tag_name


def frequency_tag_name_each_type():
    tag_name_dict, list_count_tag_name = sum_all_tag_names()
    frequency_tag_name_dict = copy.deepcopy(tag_name_dict)
    for index, key in enumerate(tag_name_dict.keys()):
        type_form = frequency_tag_name_dict[key]
        a = 0.0
        for key1, count in type_form.items():
            frequency_tag_name_dict[key][key1] = count/list_count_tag_name[index]
            a += count/list_count_tag_name[index]
    return frequency_tag_name_dict



popular_tagnames = [
"full_name",
"alias_name",
"dob",
"dob_text",
"dob_day",
"dob_month",
"dob_year",
"gender",
"id_number",
"id_issue_date",
"id_issue_day",
"id_issue_month",
"id_issue_year",
"id_issue_place",
"ethnicity",
"religion",
"nationality",
"marital_status",
"blood_type",
"birth_registration_place",
"birthplace",
"birth_registration_place_village"
"birth_registration_place_ward",
"birth_registration_place_district",
"birth_registration_place_province",
"hometown",
"permanent_address",
"current_address",
"current_address_ward",
"current_address_district",
"current_address_province",
"occupation",
"passport_number",
"passport_issue_date",
"passport_issue_day",
"passport_issue_month",
"passport_issue_year",
"passport_issue_place",
"passport_expiry_date",
"receiver",
"place",
"day",
"month",
"year"
]


def count_popular_tagnames(tag_name_dict = None, popular_tagnames = popular_tagnames):
    if tag_name_dict is None:
        tag_name_dict = load_tagname_dict()
    popular_tagname_dict = {}
    count = 0
    count1 = 0
    for index, key in enumerate(tag_name_dict.keys()):
        type_form = tag_name_dict[key]
        for key, value in type_form.items():
            if key in popular_tagnames:
                count += value
                count1 += 1
                if key not in popular_tagname_dict.keys():
                    popular_tagname_dict[key] = value
                else:
                    popular_tagname_dict[key] += value
    return popular_tagname_dict, count, count1

popular_tagname_dict, count, count1 = count_popular_tagnames()
tag_name_dict, list_count_tag_name = sum_all_tag_names()
_sum = sum(list_count_tag_name)
print(count)
print(popular_tagname_dict)
print(_sum)
print(count/_sum)
