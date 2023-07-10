# Joshua Soto
# 1553869

car_services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0,
}

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

first_service = input('Select first service:\n')
first_service_cost = car_services[first_service]
second_service = input('Select second service:\n')
second_service_cost = car_services[first_service]
print('')
print('Davy\'s auto shop invoice\n')

if first_service == '-':
    print('Service 1: No service')
else:
    print('Service 1: %s, $%d' % (first_service, car_services.get(first_service)))
if second_service == '-':
    print('Service 2: No service')
else:
    print('Service 2: %s, $%d' % (second_service, car_services.get(second_service)))
invoice_total = car_services.get(first_service) + car_services.get(second_service)
print()
print('Total: $%d' % invoice_total)
