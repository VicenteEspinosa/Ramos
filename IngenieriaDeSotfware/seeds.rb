# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

cities = ['Maipu', 'Providencia', 'San Miguel', 'Las Condes', 'Santiago']

users = {
    1 => {
        :name => 'Marcos Barrero',
        :email => 'marcos_barrero@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '995478523',
        :birthdate => "1995-02-14",
        :city_id => 1,
        :admin => true,
        :description => 'Arquitecto | Me gustan los videojuegos indie, el cine y el anime',
        :avatar => 'marcos_barrero.jpg'
    },
    2 => {
        :name => 'Francisco Mengual',
        :email => 'francisco_mengual@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '995413699',
        :birthdate => "1995-07-12",
        :city_id => 2,
        :admin => true,
        :description => 'Nací en Punta Arenas, vivo en Santiago pero estoy refugiado en mi isla de Animal Crossing.',
        :avatar => 'francisco_mengual.jpg'
    },
    3 => {
        :name => 'Felipe Couse',
        :email => 'felipe_couse@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '945698745',
        :birthdate => "1994-21-02",
        :city_id => 3,
        :admin => true,
        :description => 'Egresado de Derecho. Amante de la naturaleza, el deporte, Colo-Colo.',
        :avatar => 'felipe_couse.jpg'
    },
    4 => {
        :name => 'Francisco Duque',
        :email => 'francisco_duque@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '955881127',
        :birthdate => "1994-21-02",
        :city_id => 4,
        :admin => false,
        :description => 'No tengo apéndice, me creo bacán y creo en la paz mundial. Becky Lynch es más grande que Jesús.',
        :avatar => 'francisco_duque.jpg'
    },
    5 => {
        :name => 'Alvaro Palma',
        :email => 'alvaro_palma@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '915919511',
        :birthdate => "1994-21-02",
        :city_id => 5,
        :admin => false,
        :description => 'Opinólogo, librepensador, de ideas libres, sin prejuicios. Fumador, cafeadicto, conversador. Con pocas virtudes morales redentoras.',
        :avatar => 'alvaro_palma.jpg'
    },
    6 => {
        :name => 'Elena Romera',
        :email => 'elena_romera@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '945669877',
        :birthdate => "1994-21-02",
        :city_id => 1,
        :admin => false,
        :description => 'Parodista conocida por ser excesivamente tolerante',
        :avatar => 'elena_romera.jpg'
    },
    7 => {
        :name => 'Isabel Barón',
        :email => 'isabel_baron@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '912351475',
        :birthdate => "1994-21-02",
        :city_id => 2,
        :admin => false,
        :description => 'Estudiante de medicina que le gusta la política, y lectora por vocación. Amante de muchísimas series, demasiadas.',
        :avatar => 'isabel_baron.jpg'
    },
    8 => {
        :name => 'Carla Zabala',
        :email => 'carla_zabala@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '996336545',
        :birthdate => "1994-21-02",
        :city_id => 3,
        :admin => false,
        :description => 'Diseñadora & Creativa - Viajera del Tiempo - Oposición & Libertaria',
        :avatar => 'carla_zabala.jpg'
    },
    9 => {
        :name => 'Alicia Martorrel',
        :email => 'alicia_martorrel@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '998781599',
        :birthdate => "1994-21-02",
        :city_id => 4,
        :admin => false,
        :description => 'Cuando los ánimos vuelan alto, los días me fluyen bien.',
        :avatar => 'alicia_martorrel.jpg'
    },
    10 => {
        :name => 'Javiera Mendizabal',
        :email => 'javiera_mendizabal@gmail.com',
        :password => '123456',
        :password_confirmation => '123456',
        :phone_number => '914742142',
        :birthdate => "1994-21-02",
        :city_id => 5,
        :admin => false,
        :description => 'We are all in the gutter, but some of us are looking at the stars. Across the universe.',
        :avatar => 'javiera_mendizabal.jpg'
    }
}

restaurants = {
    1 => {
        :name => 'Mama Chaus',
        :description => 'Mama Chaus es un pequeño local en General Holley, donde encuentras dumplings, baos y shandong crepe.',
        :location => 'Gral. Holley 50',
        :user_id => 1,
        :city_id => 2,
        :is_approved => true,
        :is_pending => false,
        :latitude => -33.419928,
        :longitude => -70.609047,
        :avatar => 'mama_chaus.jpg'
    },
    2 => {
        :name => 'Niu Sushi',
        :description => 'La más amplia carta de sushi en local y delivery. Queremos brindarte el mejor servicio',
        :location => 'Gran Avenida Jose Miguel Carrera 5001',
        :user_id => 2,
        :city_id => 3,
        :is_approved => true,
        :is_pending => false,
        :latitude => -33.499511,
        :longitude => -70.653985,
        :avatar => 'niu_sushi.jpg'
    },
    3 => {
        :name => 'Holy Moly',
        :description => 'Voted best burger in town by some guy who likes burgers. The top burger 2019.',
        :location => 'Merced 318',
        :user_id => 3,
        :city_id => 5,
        :is_approved => true,
        :is_pending => false,
        :latitude => -33.436550,
        :longitude => -70.641393,
        :avatar => 'holy_moly.jpg'
    },
    4 => {
        :name => 'Fritkot',
        :description => 'Fritkot es un pequeño local de papas fritas caseras al estilo belga.',
        :location => 'Av. Holanda 067',
        :user_id => 4,
        :city_id => 2,
        :is_approved => true,
        :is_pending => false,
        :latitude => -33.417582,
        :longitude => -70.604388,
        :avatar => 'fritkot.jpg'
    },
    5 => {
        :name => 'Street Burger',
        :description => 'Nuestras burgers están hechas con los mejores ingredientes, con nuestra carne americana Black Angus 100% natural.',
        :location => 'Isidora Goyenechea 3199',
        :user_id => 5,
        :city_id => 4,
        :is_approved => true,
        :is_pending => false,
        :latitude => -33.412621,
        :longitude => -70.597049,
        :avatar => 'street_burger.jpg'
    }
}

gustos = 
{
    1 => {
        :nombre => 'Comida italiana',
        :descripcion => 'Me gustan las pastas o pizzas principalemente'
    },
    2 => {
        :nombre => 'Comida China',
        :descripcion => 'Comida con más sal de lo normal (no confundir con comida japonesa)'
    },
    3 => {
        :nombre => 'Videojuegos',
        :descripcion => 'Soy fanático/a de los videojuegos en general, independiente de la plataforma'
    },
    4 => {
        :nombre => 'Programación',
        :descripcion => 'Me gusta la computación, y sobre todo el crear programas útiles'
    },
    5 => {
        :nombre => 'Netflix',
        :descripcion => 'Me gusta estar en algún lugar cómodo viendo Netflix, sobre todo con compañía.'
    }
}

cities.each do |ciudad|
    City.create(name: "#{ciudad}")
end

users.each do |user, data|
    User.create(
        name: data[:name],
        email: data[:email],
        password: data[:password],
        password_confirmation: data[:password_confirmation],
        phone_number: data[:phone_number],
        birthdate: data[:birthdate],
        city_id: data[:city_id],
        admin: data[:admin],
        description: data[:description],
        avatar: data[:avatar]
    )
end

restaurants.each do |restaurant, data|
    Restaurant.create(
        name: data[:name],
        description: data[:description],
        location: data[:location],
        user_id: data[:user_id],
        city_id: data[:city_id],
        is_approved: data[:is_approved],
        is_pending: data[:is_pending],
        latitude: data[:latitude],
        longitude: data[:longitude],
        avatar: data[:avatar]
    )
end

gustos.each do |gusto, data|
    Gusto.create(
        nombre: data[:nombre], 
        descripcion: data[:descripcion]
    )
end
