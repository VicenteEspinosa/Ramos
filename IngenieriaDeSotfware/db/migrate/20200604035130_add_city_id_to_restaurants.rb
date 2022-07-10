class AddCityIdToRestaurants < ActiveRecord::Migration[5.2]
  def change
    add_reference :restaurants, :city, foreign_key: true
  end
end
