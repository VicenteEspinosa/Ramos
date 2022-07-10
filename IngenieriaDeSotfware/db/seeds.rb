# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

cities = ['Maipu', 'Providencia', 'San Miguel', 'Las Condes', 'Santiago']

cities.each do |ciudad|
    City.create(name: "#{ciudad}")
end

(1..5).each do |i|
    Gusto.create(
        nombre: "Gusto #{i}", 
        descripcion: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
                    'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
                    'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi '\
                    'ut aliquip ex ea commodo consequat.'
    )
end

(1..2).each do |i|
    User.create(
        email: "usuario#{i}@uc.cl",
        password: "123456", password_confirmation: "123456",
        name: "Usuario Prueba #{i}", description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
                                                'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
                                                'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi '\
                                                'ut aliquip ex ea commodo consequat.',
        birthdate: "1995-02-14", phone_number: "945636547",
        admin: true, city_id: 1
    )
end
(3..5).each do |i|
    User.create(
        email: "usuario#{i}@uc.cl",
        password: "123456", password_confirmation: "123456",
        name: "Usuario Prueba #{i}", description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
                                                'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' \
                                                'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi '\
                                                'ut aliquip ex ea commodo consequat.',
        birthdate: "1995-02-14", phone_number: "945636547",
        admin: false, city_id: 1
    )
end

