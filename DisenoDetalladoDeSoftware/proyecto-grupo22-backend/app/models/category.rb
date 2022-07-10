class Category < ApplicationRecord
    has_many :products

    validates :name, length: { minimum: 1, allow_nil: false}
end
