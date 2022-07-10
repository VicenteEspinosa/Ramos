class AddRestaurantIdToCitum < ActiveRecord::Migration[5.2]
  def change
    add_reference :cita, :restaurant, foreign_key: true
  end
end
