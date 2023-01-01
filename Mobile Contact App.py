import json

# create a JSON file to store the data

contact_list = {
  "contacts": [
    {
      "name": "John Doe",
      "number": "0123456789",
      "picture": "john_doe.jpg"
    },
    {
      "name": "Jane Doe",
      "number": "9876543210",
      "picture": "jane_doe.jpg"
    }
  ]
}

# write to JSON file
with open('contact_list.json', 'w') as json_file:
  json.dump(contact_list, json_file)

# display contact list
def display_contacts():
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    for contact in contact_list['contacts']:
      print('Name: ' + contact['name'] + '\nNumber: ' + contact['number'] + '\nPicture: ' + contact['picture'])

# create contact
def create_contact():
  name = input('Enter name: ')
  number = input('Enter number: ')
  picture = input('Enter picture: ')
  new_contact = {
    "name": name,
    "number": number,
    "picture": picture
  }
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    contact_list['contacts'].append(new_contact)
  
  with open('contact_list.json', 'w') as json_file:
    json.dump(contact_list, json_file)

# delete contact
def delete_contact():
  name = input('Enter name: ')
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    for contact in contact_list['contacts']:
      if contact['name'] == name:
        contact_list['contacts'].remove(contact)
        break
  
  with open('contact_list.json', 'w') as json_file:
    json.dump(contact_list, json_file)

# update contact
def update_contact():
  name = input('Enter name: ')
  number = input('Enter number: ')
  picture = input('Enter picture: ')
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    for contact in contact_list['contacts']:
      if contact['name'] == name:
        contact['number'] = number
        contact['picture'] = picture
        break
  
  with open('contact_list.json', 'w') as json_file:
    json.dump(contact_list, json_file)

# sort contact list by name
def sort_contact_name():
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    sorted_contacts = sorted(contact_list['contacts'], key=lambda contact: contact['name'])
    for contact in sorted_contacts:
      print('Name: ' + contact['name'] + '\nNumber: ' + contact['number'] + '\nPicture: ' + contact['picture'])

# sort contact list by number
def sort_contact_number():
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    sorted_contacts = sorted(contact_list['contacts'], key=lambda contact: contact['number'])
    for contact in sorted_contacts:
      print('Name: ' + contact['name'] + '\nNumber: ' + contact['number'] + '\nPicture: ' + contact['picture'])

# search contact
def search_contact():
  name = input('Enter name: ')
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    for contact in contact_list['contacts']:
      if contact['name'] == name:
        print('Name: ' + contact['name'] + '\nNumber: ' + contact['number'] + '\nPicture: ' + contact['picture'])
        break

# display picture
def display_picture():
  name = input('Enter name: ')
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    for contact in contact_list['contacts']:
      if contact['name'] == name:
        print('Picture: ' + contact['picture'])
        break

# import contacts
def import_contacts():
  with open('contact_list.json', 'r') as json_file:
    contact_list = json.load(json_file)
    for contact in contact_list['contacts']:
      print('Name: ' + contact['name'] + '\nNumber: ' + contact['number'] + '\nPicture: ' + contact['picture'])

# print menu
def print_menu():
  print('\n1. Display contact list')
  print('2. Create contact')
  print('3. Delete contact')
  print('4. Update contact')
  print('5. Sort contact list by name')
  print('6. Sort contact list by number')
  print('7. Search contact')
  print('8. Display picture')
  print('9. Import contacts')
  print('10. Exit\n')

# main
while True:
  print_menu()
  option = int(input("Enter an option: "))
  if option == 1:
    display_contacts()
  elif option == 2:
    create_contact()
  elif option == 3:
    delete_contact()
  elif option == 4:
    update_contact()
  elif option == 5:
    sort_contact_name()
  elif option == 6:
    sort_contact_number()
  elif option == 7:
    search_contact()
  elif option == 8:
    display_picture()
  elif option == 9:
    import_contacts()
  elif option == 10:
    break
  else:
    print('Invalid option.')