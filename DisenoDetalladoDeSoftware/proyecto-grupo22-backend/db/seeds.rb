# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)

user = User.create(email: "hola@hola.com", password: "hola1234")

cart = ShoppingCart.create(user_id: 1)

pcs = Category.create(name: "Computadores y Tablets")
games = Category.create(name: "Juegos y Consolas")
tvs = Category.create(name: "TV y Smart TV")

Product.create(name: 'ProArt StudioBook 16', price: 3299990, brand: 'Asus', category_id: pcs.id, image: 'https://www.pcfactory.cl/public/foto/44677/1.jpg?t=1648144088000')
Product.create(name: 'MacBook Pro 14" M1', price: 2229990, brand: 'Apple', category_id: pcs.id, image: 'https://www.pcfactory.cl/public/foto/44110/1.jpg?t=1640618279000')
Product.create(name: 'Ultraliviano Yoga Slim 9 14"', price: 1589990, brand: 'Lenovo', category_id: pcs.id, image: 'https://www.pcfactory.cl/public/foto/40626/1.jpg?t=1615842728511')

Product.create(name: 'Xbox Series X', price: 589990, brand: 'Microsoft', category_id: games.id, image: 'https://www.pcfactory.cl/public/foto/45955/1.jpg?t=1653485903960')
Product.create(name: 'PlayStation 5', price: 689990, brand: 'Sony', category_id: games.id, image: 'https://www.pcfactory.cl/public/foto/43431/1.jpg?t=1631720633290')
Product.create(name: 'Nintendo Switch', price: 429990, brand: 'Nintendo', category_id: games.id, image: 'https://www.pcfactory.cl/public/foto/43349/1.jpg?t=1630592389980')

Product.create(name: 'Neo QLED Smart TV 65QN800A 65'' 8K 120Hz', price: 1679990, brand: 'Samsung', category_id: tvs.id, image: 'https://www.pcfactory.cl/public/foto/41437/1.jpg?t=1644500952877')
Product.create(name: 'Smart TV 75X80J 75'' Ultra HD 4K WiFi', price: 899990, brand: 'Sony', category_id: tvs.id, image: 'https://www.pcfactory.cl/public/foto/42855/1.jpg?t=1652124822576')
Product.create(name: 'Smart TV NanoCell 55" 55NANO80 Ultra HD 4K', price: 469990, brand: 'LG', category_id: tvs.id, image: 'https://www.pcfactory.cl/public/foto/42176/1.jpg?t=1652295535313')

Coupon.create(name: 'ENTREGA3', value: 10000, category_id: pcs.id)
