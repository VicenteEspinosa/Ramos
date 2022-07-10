class ProductSerializer < ActiveModel::Serializer
  include JSONAPI::Serializer
  set_key_transform :camel_lower

  attributes :id, :name, :brand, :price, :image

  attribute :category do |product|
    Category.find(product.category_id).name
  end
end
