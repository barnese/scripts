# Generates a list of fake names, phone numbers and addresses.

require 'Faker'

count = 10

if ARGV.length == 1
  count = Integer(ARGV[0])
end

Faker::Config.locale = 'en-US'

for i in 1..count do
  name = Faker::Name.first_name + " " + Faker::Name.last_name
  phone = Faker::PhoneNumber.cell_phone
  address = Faker::Address.street_address + ", " + Faker::Address.city + ", " + Faker::Address.state_abbr + " " + Faker::Address.zip
  printf "%-25s %-15s %s\n", name, phone, address
end

