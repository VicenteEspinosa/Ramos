class Product < ApplicationRecord
  validates :name, presence: { message: 'El nombre no puede estar vacio' }, length:
    { maximum: 128, message: 'El nombre tiene que ser de menos de 128 caracteres' }
  validates :price, presence: { message: 'Falta el precio' }, numericality:
    {
      only_integer: true,
      greater_than: 0,
      less_than_or_equal_to: 50_000,
      message: 'No puede existir un producto con ese precio'
    }
  validates :category, presence: { message: 'Falta la categoria' }, inclusion:
    {
      in: %w[Bebestible Comestibles Souvenir],
      message: '%<value>s no es una categoria valida'
    }
  validates :amount, presence: { message: 'Falta la cantidad' }, numericality:
    {
      only_integer: true,
      greater_than: 0,
      less_than_or_equal_to: 2_000,
      message: 'No puede existir un producto con esa cantidad'
    }
end
