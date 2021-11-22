# Problem statement convert, Hierarcy tree input data to flat tree 
# EG: 
input_data = {
    "Name": "regology",
    "Author": "regology",
    "Company Services": [
        {
            "Service": "Complaince Mangement system",
            "Link": "https://regology.com"
        },
        {
            "Service": "service2",
            "Link": "link2"
        },
        {
            "Service": "service3",
            "Link": "link3"
        }
    ],
    "Address": {
        "Home": {
            "city": "Hyderabad",
            "state": "Telangana",
            "area": "gachibowli"
        },
        "Office": {
            "city": "Pune",
            "state": "Maharastra",
            "area": "Chowk"
        }
    }
}

#output = {
    # 'Name': 'regology',
    # 'Author': 'regology',
    # 'Company Services_0_Service': 'Complaince Mangement system',
    # 'Company Services_0_Link': 'https://regology.com',
    # 'Company Services_1_Service': 'service2',
    # 'Company Services_1_Link': 'link2',
    # 'Company Services_2_Service': 'service3',
    # 'Company Services_2_Link': 'link3',
    # 'Address_Home_city': 'Hyderabad',
    # 'Address_Home_state': 'Telangana',
    # 'Address_Home_area': 'gachibowli',
    # 'Address_Office_city': 'Pune',
    # 'Address_Office_state': 'Maharastra',
    # 'Address_Office_area': 'Chowk'
# }


def get_list(prefix, data):
    ans = {}
    for i in range(len(data)):
        if isinstance(data[i], list):
            res = get_list(prefix + "_" + str(i), data[i])
        elif isinstance(data[i], dict):
            res = get_dict(prefix + "_" + str(i), data[i])
        ans.update(res)

    return ans


def get_dict(prefix, data):
    ans = {}
    for i in data:
        if isinstance(data[i], list):
            res = get_list(prefix + "_" + str(i), data[i])
        elif isinstance(data[i], dict):
            res = get_dict(prefix + "_" + str(i), data[i])
        else:
            res = {prefix + "_" + i: data[i]}
        ans.update(res)
    return ans


def sol(input_data):
    ans = {}
    for i in input_data:
        if isinstance(input_data[i], list):
            res = get_list(i, input_data[i])
        elif isinstance(input_data[i], dict):
            res = get_dict(i, input_data[i])
        else:
            res = {i: input_data[i]}
        ans.update(res)

    return ans


print(sol(input_data))


