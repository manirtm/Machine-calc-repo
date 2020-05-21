from collections import Counter
from pprint import pprint



countries = {
        'New York':[{'size': 'Large', 'unit': 10,'costs': 120},
                    {'size':'XLarge', 'unit': 20,'costs': 230},
                    {'size': '2XLarge', 'unit': 40, 'costs': 450},
                    {'size':'4XLarge', 'unit': 80, 'costs': 774},
                    {'size': '8XLarge', 'unit': 160, 'costs': 1400},
                    {'size': '10XLarge', 'unit': 320, 'costs': 2820}],
        'India': [{'size': 'Large', 'unit': 10,'costs': 140},
            {'size':'XLarge', 'unit': 20,'costs': None},
            {'size': '2XLarge', 'unit': 40, 'costs': 413},
            {'size': '4XLarge', 'unit': 80, 'costs': 890},
            {'size': '8XLarge', 'unit': 160, 'costs': 1300},
            {'size': '10XLarge', 'unit': 320, 'costs': 2970}],
        
        'China': [{'size': 'Large', 'unit': 10,'costs': 110},
                    {'size':'XLarge', 'unit': 20,'costs': 200},
                    {'size': '2XLarge', 'unit': 40, 'costs': None},
                    {'size':'4XLarge', 'unit': 80, 'costs': 670},
                    {'size': '8XLarge', 'unit': 160, 'costs': 1180},
                    {'size': '10XLarge', 'unit': 320, 'costs': None}]
                    }


def new_york(ny_lis):
    output_ny = {}
    newyork_list = []
    for data in ny_lis:
        newyork_total = 0
        for key in data:
            for country in countries:
                units = countries[country]
                for data in units:
                    size = data.get('size')
                    unit = data.get('unit')
                    costs = data.get('costs')
                    if key == unit:
                        if country == 'New York':
                            if not costs == None:
                                newyork_total+= (costs * hours)
        newyork_list.append(newyork_total)
    new_york_pos = [i for i, j in enumerate(newyork_list) if j == min(newyork_list)]
    for i in new_york_pos:
        index = i
        ny_machine= ny_lis[index]
    frequency_ = {ny_freq:ny_machine.count(ny_freq) for ny_freq in ny_machine}
    frequency_ny = dict((size_dict[key], value) for (key, value) in frequency_.items())
    output_ny['region'] = 'New York'
    output_ny['total_cost'] = min(newyork_list)
    output_ny['machines'] = list(frequency_ny.items())
    # print(output_ny)
    return output_ny


def india(ind_lis):
    output_ind = {}
    india_list= []
    for data in ind_lis:
        india_total = 0
        for key in data:
            for country in countries:
                units = countries[country]
                for data in units:
                    size = data.get('size')
                    unit = data.get('unit')
                    costs = data.get('costs')
                    if key == unit:
                        if country == 'India':
                            if not costs == None:
                                india_total+= (costs * hours)
        india_list.append(india_total)
    india_pos= [i for i, j in enumerate(india_list) if j == min(india_list)]
    for i in india_pos:
        index = i
        ind_machine = ind_lis[index]
    frequency_ = {ind_freq:ind_machine.count(ind_freq) for ind_freq in ind_machine}
    frequency_ind = dict((size_dict[key], value) for (key, value) in frequency_.items())
    output_ind['region'] = 'India'
    output_ind['total_cost'] = min(india_list)
    output_ind['machines'] = list(frequency_ind.items())
    # print(output_ind)
    return output_ind

def china(china_lis):
    output_china = {}
    china_list = []
    for data in china_lis:
        china_total = 0
        for key in data:
            for country in countries:
                units = countries[country]
                for data in units:
                    size = data.get('size')
                    unit = data.get('unit')
                    costs = data.get('costs')
                    if key == unit:
                        if country == 'China':
                            if not costs == None:
                                china_total+= (costs * hours)
        china_list.append(china_total)
    china_pos = [i for i, j in enumerate(china_list) if j == min(china_list)]
    for i in china_pos:
        index = i
        china_machine = china_lis[index]
    frequency_ = {china_freq:china_machine.count(china_freq) for china_freq in china_machine}
    frequency_china = dict((size_dict[key], value) for (key, value) in frequency_.items())
    output_china['region'] = 'China'
    output_china['total_cost'] = min(china_list)
    output_china['machines'] = list(frequency_china.items())
    # print(output_china)
    return output_china

def cost_calculator(result,hours):
    lis_1 = []
    lis_2 = []
    lis_3 = []
    final_output = []
    final_dict = {}
    for res in result:
        for country in countries:
            units = countries[country]
            if country == 'New York':
                lis_1.append(res)
            if country == 'India':
                if not 20 in res:
                    lis_2.append(res)
            if country == 'China':
                if not 320 in res:
                    if not 40 in res:
                        lis_3.append(res)
                elif not 40 in res:
                    if not 320 in res:
                        lis_3.append(res)
    final_output.append(new_york(lis_1))
    final_output.append(india(lis_2))
    final_output.append(china(lis_3))
    final_dict['Output'] = final_output
    pprint(final_dict)


def resource_allocator(unit_list, capacity, with_replacement=False):
    
    def resource(index, inner_list, list_, capacity , with_replacement):
        if capacity == sum(inner_list): 
            list_.append(inner_list)
        elif capacity < sum(inner_list): 
            return
        for u in range(index, len(unit_list)):
            resource(u if with_replacement else (u + 1), inner_list + [unit_list[u]], list_, capacity, with_replacement)
        return list_
    return resource(0, [], [], capacity, with_replacement)


unit_list = [320, 160, 80, 40, 20, 10] 
size_dict = {320 :'10XLarge', 160 :'8XLarge', 80 :'4XLarge', 40 :'2XLarge', 20 :'XLarge', 10 :'Large'}

capacity = int(input('No of units are required: '))
if capacity%10 == 0:
    hours = int(input('No of hours the machine is required to run: '))
    result= resource_allocator(unit_list, capacity, True)
    cost_calculator(result,hours)
else:
    print('No of units will always be multiple of 10')

 

