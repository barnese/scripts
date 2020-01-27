# Generates a list of fake first and last names.

require 'Faker'

count = 10

if ARGV.length == 1
  count = Integer(ARGV[0])
end

Faker::Config.locale = 'en-US'

for i in 1..count do
  name = Faker::Name.first_name + " " + Faker::Name.last_name
  puts name
end

